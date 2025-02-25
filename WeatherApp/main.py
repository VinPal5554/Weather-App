import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
program_running = True

while program_running:
    CITY = input("Location: ")
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    # Make a request to the weather API
    response = requests.get(URL)

    # Extract and convert successful request to json, otherwise print error
    if response.status_code == 200:
        weather_data = response.json()

        # Format json appropriately
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"The temperature in {CITY} is: {temperature} degrees")
        print(f"Description: {weather_description}")
        print(f"Humidity: {humidity}")
        print(f"Wind speed: {wind_speed}")

        user_choice = input("Would you like to check again? (Y/N)").lower()

        if user_choice == "n":
            break

    else:
        print(f"Something went wrong extracting data (Status Code: {response.status_code})")



