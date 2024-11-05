import requests # for fetching urls
import pandas as pd #For creating dataframe and saves it in a csv file
from datetime import datetime #for converting meeting date and starting time

# API endpoint
url = "https://www.sportsbet.com.au/apigw/sportsbook-racing/Sportsbook/Racing/NextEvents"

# Parameters I got from the Network's API 
params = {
    "racingFilters": "HR_DOMESTIC,HR_INTERNATIONAL,GH_DOMESTIC,GH_INTERNATIONAL,HA_DOMESTIC,HA_INTERNATIONAL",
    "groupByFilters": "true"
}

# Send GET request
response = requests.get(url, params=params)

# Prepare data
races = []

if response.status_code == 200:
    data = response.json()
    
    for event in data:
        country = event.get("country")
        if country in ["Australia", "New Zealand"]: # Filters Australia and New Zealand
            display_name = event.get("displayName")
            race_number = event.get("raceNumber")
            start_time = event.get("startTime")
            
            # Convert start_time from Unix timestamp to formatted time
            meeting_date = datetime.fromtimestamp(start_time).date()
            race_time = datetime.fromtimestamp(start_time).strftime("%I:%M %p")

            # Append the race details to the list
            races.append({
                "Meeting Date": meeting_date,
                "Race Name": display_name,
                "Race Number": f"Race {race_number}",
                "Race Time": race_time
            })
            
else:
    print(f"Error fetching data: {response.status_code} - {response.text}")

# Create DataFrame
df = pd.DataFrame(races)

# Save DataFrame to CSV file in the current directory
file_path = "races_data.csv"
df.to_csv(file_path, index=False)

print(df)
print(f"Data saved to {file_path}")
