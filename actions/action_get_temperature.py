import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import pytz



def get_current_temperature(city: str, api_key: str) -> float:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # для получения в °C
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        print(data)
        return data['main']['temp']
    except Exception as e:
        print(f"Ошибка при получении температуры: {e}")
        return 0.0

api_key = "8adfb3bf2336a9a8b4ade07984c8cdd6"  # Получите бесплатный ключ на https://openweathermap.org

class ActionGetTemperature(Action):
    def name(self) -> Text:
        return "action_get_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.latest_message['entities']
        print(city)
        for entity in city:
            if entity['entity'] == 'city':
                city_name = entity['value']
                print(city_name)
                break
        try:
            current_temperature = get_current_temperature(city_name, api_key)
            print(current_temperature)
            dispatcher.utter_message(text=f"The temperature in {city_name} is currently {current_temperature} degrees.")
        except Exception as e:
            dispatcher.utter_message(text="Sorry, I can't determine the temperature.")
            print(f"Error: {e}")

        return []