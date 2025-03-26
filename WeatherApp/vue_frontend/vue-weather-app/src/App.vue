<script setup>
import weatherService from "./services/weatherService";
import { ref } from 'vue';

const city = ref("");
const weatherData = ref(null);
const isLoading = ref(false);
const errorMessage = ref("");
const isCelsius = ref(true);

async function getWeatherData() {
  try {
    isLoading.value = true;
    errorMessage.value = "";
    const units = isCelsius.value ? "metric" : "imperial"; // Celsius: metric, Fahrenheit: imperial
    const data = await weatherService.getWeather(city.value, units);
    weatherData.value = data;
  } catch (error) {
    errorMessage.value = "Error fetching weather data.";
  } finally {
    isLoading.value = false;
  }
}

const isDarkMode = ref(false); // Track whether dark mode is active

// Toggle between dark and light mode
function toggleDarkMode() {
  isDarkMode.value = !isDarkMode.value;
  if (isDarkMode.value) {
    document.body.classList.add('dark-mode');
  } else {
    document.body.classList.remove('dark-mode');
  }
}



</script>

<template>
  <div>
    <h1>Weather App - By Vinay Pal</h1>
    <input v-model="city" placeholder="Enter city" />
    <button @click="getWeatherData">Get Weather</button>

    <button @click="toggleDarkMode">
      Switch to {{ isDarkMode ? 'Light' : 'Dark' }} Mode
    </button>

    <div v-if="isLoading">Loading...</div>

    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>

    <div v-if="weatherData">
      <img :src="'http://openweathermap.org/img/wn/' + weatherData.weather[0].icon + '.png'" alt="Weather Icon" />
      <p><strong>Temperature:</strong> {{ weatherData.main.temp }}°{{ isCelsius.value ? 'C' : 'F' }}</p>
      <p><strong>Description:</strong> {{ weatherData.weather[0].description }}</p>
      <p><strong>Humidity:</strong> {{ weatherData.main.humidity }}%</p>
      <p><strong>Wind Speed:</strong> {{ weatherData.wind.speed }} m/s</p>
      <p><strong>Cloudiness:</strong> {{ weatherData.clouds.all }}%</p>
    </div>
  </div>
</template>

<style scoped>
input {
  padding: 8px;
  margin-right: 10px;
}
button {
  padding: 8px 16px;
  margin-top: 10px;
}
.error {
  color: red;
  font-weight: bold;
}

</style>