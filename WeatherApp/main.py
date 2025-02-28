import requests
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import messagebox

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_weather():
        CITY = entry_field.get()
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

        try:
            # Make a request to the weather API, timeout of 10 seconds
            response = requests.get(URL, timeout=10)

            # Extract and convert successful request to json, otherwise print error
            if response.status_code == 200:
                weather_data = response.json()

                # Format json appropriately
                temperature = weather_data["main"]["temp"]
                weather_description = weather_data["weather"][0]["description"]
                humidity = weather_data["main"]["humidity"]
                wind_speed = weather_data["wind"]["speed"]

                temperature_label.config(text=f"The temperature in {CITY} is: {temperature} degrees")
                description_label.config(text=f"Description: {weather_description}")
                humidity_label.config(text=f"Humidity: {humidity}")
                wind_label.config(text=f"Wind speed: {wind_speed}")

            # Resource not found
            elif response.status_code == 404:
                messagebox.showerror("Error", f"The city {CITY} does not exist")
            # Unauthorised access to resource
            elif response.status_code == 401:
                messagebox.showerror("Error", "Invalid API Key")
            else:
                messagebox.showerror("Error", f"Something went wrong extracting data (Status Code: {response.status_code})")
        except requests.exceptions.Timeout:
            messagebox.showerror("Error", "The request has timed out!")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "The request has lost connection!")
        except requests.exceptions.RequestException as exception:
            messagebox.showerror("Error", f"Something went wrong: {exception}")

# GUI Window
root = tk.Tk()
root.title("My Weather App")
root.geometry("600x200")

# Input and buttons
tk.Label(root, text="Please enter city: ").pack()
entry_field = tk.Entry(root)
entry_field.pack()
tk.Button(root, text="Enter", command=get_weather).pack()

# Labels to show the returned info
temperature_label = tk.Label(root, text="", font=("Arial", 12))
temperature_label.pack()
description_label = tk.Label(root, text="", font=("Arial", 12))
description_label.pack()
humidity_label = tk.Label(root, text="", font=("Arial", 12))
humidity_label.pack()
wind_label = tk.Label(root, text="", font=("Arial", 12))
wind_label.pack()

# Start the GUI loop
root.mainloop()
