import requests
from datetime import datetime, timedelta

# Define the endpoint URL
url = 'http://127.0.0.1:8000/api/timeslots/'

# Define the authentication token
token = 'Token 127abb714dea0b5036d9485ae6295a8c49c6c886'

# Define the start and end time for each time slot
start_time = datetime.strptime("10:00", "%H:%M").time()
end_time = datetime.strptime("14:00", "%H:%M").time()

# Define the start and end date range
start_date = datetime.strptime("2024-04-27", "%Y-%m-%d")
end_date = datetime.strptime("2024-09-30", "%Y-%m-%d")

# Iterate over the date range
while start_date <= end_date:
    # Create start and end datetime objects for the current date
    start_datetime = datetime.combine(start_date, start_time)
    end_datetime = datetime.combine(start_date, end_time)
    
    # Create the data payload
    data = {
        "user": 2,
        "start_date": start_datetime.strftime("%Y-%m-%dT%H:%M:%S+02:00"),
        "end_date": end_datetime.strftime("%Y-%m-%dT%H:%M:%S+02:00"),
        "timedelta": 30
    }
    
    # Send the POST request
    response = requests.post(url, data=data, headers={'Authorization': token})
    
   # print(data)
    
    # Print the response
    print(f"Status code for {start_date}: {response.status_code}")
    
    # Move to the next day
    start_date += timedelta(days=1)
