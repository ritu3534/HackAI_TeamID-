import requests
from uAgent import uAgent

class TemperatureAlertAgent:
    def _init_(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_temperature(self, location):
        params = {"q": location, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            return temperature
        else:
            return None

    def check_temperature_alert(self, location, min_temp, max_temp):
        current_temp = self.get_temperature(location)

        if current_temp is not None:
            if current_temp < min_temp or current_temp > max_temp:
                message = f"Temperature Alert: {current_temp}°C in {location}."
                uAgent.send_notification(message)
            else:
                print(f"Current temperature in {location}: {current_temp}°C")
        else:
            print("Failed to fetch temperature data. Check your location or API key.")

# Example usage
api_key = "e0c449c1faf038b1f24740783a843eb8"
agent = TemperatureAlertAgent(api_key)
agent.check_temperature_alert("City, Country", 20, 30)
