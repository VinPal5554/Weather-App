import requests

# Replace 'your_api_key' with your actual API key
API_KEY = ""
CITY = input("Location: ")
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Make a request to the weather API
response = requests.get(URL)

# Extract and convert successful request to json, otherwise print error
if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
else:
    print(f"Something went wrong extracting data (Status Code: {response.status_code})")



