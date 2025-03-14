<template>
  <div>
    <h1>Weather App</h1>
    <input v-model="city" placeholder="Enter city" />
    <button @click="getWeatherData">Get Weather</button>

    <div v-if="weatherData">
      <p><strong>Temperature:</strong> {{ weatherData.main.temp }}°C</p>
      <p><strong>Description:</strong> {{ weatherData.weather[0].description }}</p>
      <p><strong>Humidity:</strong> {{ weatherData.main.humidity }}%</p>
      <p><strong>Wind Speed:</strong> {{ weatherData.wind.speed }} m/s</p>
    </div>
  </div>
</template>

<script setup>
// Import the weatherService at the top
import weatherService from "./services/weatherService";

// Define your reactive variables
import { ref } from 'vue';

// Create reactive variables for city input and weather data
const city = ref("");
const weatherData = ref(null);

// Create the method to fetch weather data
async function getWeatherData() {
  try {
    // Call the weather service to fetch the weather data
    const data = await weatherService.getWeather(city.value);
    weatherData.value = data;
  } catch (error) {
    alert("Error fetching weather data");
  }
}
</script>

<style scoped>
/* Add your weather app styles here */
input {
  padding: 8px;
  margin-right: 10px;
}
button {
  padding: 8px 16px;
}
</style>