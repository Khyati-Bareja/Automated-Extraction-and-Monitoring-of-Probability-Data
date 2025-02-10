# Transforms the extracted data:
# (i) adds timestamps
# (ii) compares it with previous day's data.

from kafka import KafkaConsumer
import json
from datetime import time
import pandas as pd
import os

Kafka_BROKER = "localhost:9092"
TOPIC = "cme_probabilities"
OUTPUT_DIR = "data/raw/"

os.makredirs(OUTPUT_DIR, exist_ok=True)

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=Kafka_BROKER,
    auto_offset_reset= "earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

raw_data = []
for message in consumer:
    raw_data.append(message.value)
    print(f"Received message: {message.value}") # Print the message

df = pd.DataFrame(raw_data)
df.to_csv("output.csv", index=False)
