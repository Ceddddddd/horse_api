# Racing Events Data Fetcher

This project retrieves and filters racing event data from an API, specifically for Australia and New Zealand, and saves it as a CSV file. The file includes details like meeting date, race name, race number, and start time.

## Features
- Fetches upcoming racing events.
- Filters events to show only those in Australia and New Zealand.
- Converts start times from Unix timestamps to a readable format.
- Saves the data to `races_data.csv` in the current directory.

## Prerequisites
- Python 3.6+
- `pandas` library
- `requests` library

Install the required package:
```bash
pip install pandas
pip install requests

## How to Run

Run the script:

Python
Copy code
python main.py
