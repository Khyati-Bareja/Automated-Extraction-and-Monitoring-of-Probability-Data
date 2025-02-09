# Automated-Extraction-and-Monitoring-of-Probability-Data

The goal of this project is to automate the extraction, transformation, and storage of probability data from the website at regular intervals. This data will be processed, compared against the previous day's last available data, and stored for further analysis. The system should maintain historical records and consolidate daily reports efficiently.


Business Requirement 
<< Perform the below task 1st on-premise and then on GCP >>

1️⃣ Data Import ( xx:xx AM Daily)
Load the last available probability data from the previous day's final consolidated CSV.
This data will serve as the baseline for computing differences throughout the day.
2️⃣ Data Extraction (Every N Minutes/hours, e.g.,  4 hours, can be reduced later to 5 mins)
Scrape the latest probability data from the website.
Convert the extracted data into a structured DataFrame.
3️⃣ Data Processing & Transformation
Add timestamp columns (date, time) to track when the data was captured.
Perform an outer merge between the newly extracted data and the previously imported dataset.
Compute the difference in probabilities for the same "Meeting Date" and "Rate".
4️⃣ Data Storage & Logging
Print the calculated probability differences for real-time visibility.
Export the transformed DataFrame as a CSV file, saving it with a timestamped filename.
This process will repeat every N minutes, generating multiple CSV files throughout the day.
5️⃣ Daily Data Consolidation (  every 12 hours Daily)
Merge all minute-level CSV files generated throughout the day into a single daily CSV file.
Store the consolidated daily CSV for historical tracking and analysis.
Delete individual minute-level CSV files to optimize storage.
6️⃣ Next Day's Initialization
When the process starts the next morning at 7 AM, the system will:
Import the last available probabilities from the previous day's final CSV.
Use this data as the reference point for the new day's probability comparisons.

