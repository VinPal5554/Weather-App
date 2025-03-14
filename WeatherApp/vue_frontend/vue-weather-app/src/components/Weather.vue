<template>
  <div>
    <h1>Weather App</h1>
    <!-- Input field to enter city name -->
    <input v-model="city" placeholder="Enter city" />
    <button @click="getWeatherData">Get Weather</button>

    <!-- Display the weather data -->
    <div v-if="weatherData">
      <p><strong>Temperature:</strong> {{ weatherData.main.temp }}°C</p>
      <p><strong>Description:</strong> {{ weatherData.weather[0].description }}</p>
      <p><strong>Humidity:</strong> {{ weatherData.main.humidity }}%</p>
      <p><strong>Wind Speed:</strong> {{ weatherData.wind.speed }} m/s</p>
    </div>
  </div>
</template>

<script>
// Import the weatherService to fetch data from Flask backend
import weatherService from "@/services/weatherService";  // Adjust the path if necessary

export default {
  data() {
    return {
      city: "",           // To store the city name entered by the user
      weatherData: null,  // To store the weather data from the API
    };
  },
  methods: {
    // Method to get the weather data by calling the service
    async getWeatherData() {
      try {
        // Call the weatherService to get data from the backend
        const data = await weatherService.getWeather(this.city);
        this.weatherData = data;  // Store the returned data in weatherData
      } catch (error) {
        alert("Error fetching weather data");
      }
    },
  },
};
</script>

<style scoped>
/* You can add some basic styling here */
input {
  padding: 8px;
  margin-right: 10px;
}
button {
  padding: 8px 16px;
}
</style>