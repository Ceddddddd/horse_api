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

## Setting Up a Virtual Environment

1. **Create a Virtual Environment**:
   Navigate to your project directory in the terminal and run:
   ```bash
   python -m venv venv
   ```
   Select python as the working environment
   
3. **Activate Environment**:
   
   On windows:
   ```bash
   venv\Scripts\activate
   ```
   On Linux:
   ```bash
   source venv/bin/activate
   ```

Install the required packages:
```bash
pip install pandas
```
```bash
pip install requests
```

## How to Run
Run the script:(or just click run in the VScode)

```bash
python main.py
# After execution, a CSV file (races_data.csv) with event details will be created in the current directory.
```







