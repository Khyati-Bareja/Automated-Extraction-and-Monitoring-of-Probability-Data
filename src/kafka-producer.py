# Extracts probability data from the website

# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from datetime import datetime
# import os

# def extract():
#     url = "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"
#     response.get(url)

#     if response.status_code == 200:
#         print("Failed To Retrieve Data")
#         return None
    
#     soup = BeautifulSoup(response.text, "html.parser")
#     #  Now we assume there is a table in the website
#     table = soup.find("table")

#     if not table:
#         print("Table not found on the page")
#         return None
    
#     headers = 

# This script extracts data and publishes it to a Kafka topic
from datetime import time
from kafka import KafkaProducer
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


KAFKA_BROKER = "localhost:9092"  # Kafka broker address
TOPIC = "cme_probabilities"    # Name of the Kafka topic where we will publish messages

# KAFKA PRODUCER
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER, # Bootstarp_servers define where Kafka is running Connect to Kafka broker
    value_serializer=lambda x: json.dumps(x).encode("utf-8") # Serialize JSON messages
)

def extract_data():
    url = "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve data")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all("table")
    # now find the table which contains Meeting Date
    target_table = None
    for table in tables: 
        headers = [th.text.strip() for th in table.find_all("th")]
        if "Meeting Date" in headers:
            target_table = table
            break
        
    if not target_table:
        print("Table not found on the page")
        return None
    headers = [th.text.strip() for th in target_table.finad_all("th")]
    rows = target_table.find_all("tr")
    for row in target_table.find_all("tr")[1:]:
        cells = row.find_all("td")
        row_data = {headers[i]: cells[i].text.strip() for i in range (len(cells))}
        rows.rows_appened(row_data)
    
    for row in rows:
        producer.send(TOPIC, row)
        print(f"Published to {TOPIC}: {row}")
    producer.flush()
    producer.close()

if __name__ == "__main__":
    extract_data()
    time.sleep(3600) # will run every hour 
    