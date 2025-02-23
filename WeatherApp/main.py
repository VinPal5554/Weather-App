import requests

# Replace 'your_api_key' with your actual API key
API_KEY = ""
CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Make a request to the weather API
response = requests.get(URL)

# Convert response to JSON
weather_data = response.json()

# Print the weather details
print(weather_data)