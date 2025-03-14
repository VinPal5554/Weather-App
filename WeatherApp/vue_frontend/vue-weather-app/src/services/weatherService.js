import axios from "axios";

// API URL of your Flask backend
const API_URL = "http://localhost:5000/weather";

export default {
  async getWeather(city) {
    try {
      // Make GET request to Flask backend
      const response = await axios.get(API_URL, {
        params: {
          city: city,
        },
      });
      return response.data;
    } catch (error) {
      console.error("Error fetching weather data", error);
      throw error;
    }
  },
};