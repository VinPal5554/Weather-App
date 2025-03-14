import requests
from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# Environmental variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

CORS(app)

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL, timeout=10)

        if response.status_code == 200:
            weather_data = response.json()
            return jsonify(weather_data)
        else:
            return jsonify({"error": "City not found or API error"}), 404
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timeout"}), 408
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error fetching data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

