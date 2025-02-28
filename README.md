# Weather-App

This is a simple weather app that fetches weather data using the OpenWeatherMap API. This includes temperature, weather conditions, and wind speed. It uses a GUI via the Tkinter library. 

# Features
- Fetches weather data for different cities
- Displays conditions such as temperature, windspeed, and humidity
- Error handling (Invalid city, timeout, invalid API, lost connection, etc)

# Installation steps
Clone the repository:
```
git clone https://github.com/VinPal5554/Weather-App
cd Weather-App
```
Install dependencies (Python 3+):
```
pip install requests
```
Setup API key:
You will need to use your own OpenWeatherMap API key. 
A .env file will need to be created within the project in this format:
```
API_KEY=openweather_api_key
```
Run the app:
```
python main.py
```

![Weather App Screenshot](weather_app.png)
