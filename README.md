# Weather-App

A simple weather forecasting application built using Vue.js for the frontend and Flask for the backend. This app fetches real-time weather data from the OpenWeatherMap API and displays it to the user.

# Features
- Real-time weather data: Fetches current weather details (temperature, description, humidity, wind speed) for any city
- Responsive UI: Built with Vue.js and styled using Tailwind CSS
- Backend API: The backend is built with Flask and handles requests to the OpenWeatherMap API

# Installation steps
**Clone the repository:**
```
git clone https://github.com/VinPal5554/Weather-App
cd Weather-App
```
**Install backend dependencies:**
```
cd WeatherApp
pip install -r requirements.txt
```
**Install frontend dependencies:**
```
cd vue_frontend/vue-weather-app
npm install
```
**Setup API key:**

You will need to use your own OpenWeatherMap API key. 

An env file will need to be created within the project in this format:
```
API_KEY=openweather_api_key
```
**Run the Flask app:**
```
python main.py
```
**Run the Vue.js app:**
```
npm run dev
```
