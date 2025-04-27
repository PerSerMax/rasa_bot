from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import pytz

class ActionGetTime(Action):
    def name(self) -> Text:
        return "action_get_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            current_time = datetime.now().strftime("%H:%M")
            dispatcher.utter_message(text=f"Сейчас {current_time}")
        except Exception as e:
            dispatcher.utter_message(text="Извините, не могу определить время")
            print(f"Error: {e}")

        return []

class ActionGetDate(Action):
    def name(self) -> Text:
        return "action_get_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            current_date = datetime.now().strftime("%d.%m.%Y")
            dispatcher.utter_message(text=f"Сегодня {current_date}")
        except Exception as e:
            dispatcher.utter_message(text="Извините, не могу определить дату")
            print(f"Error: {e}")

        return []

class ActionGetTemperature(Action):
    def name(self) -> Text:
        return "action_get_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            current_temperature = 25  # Replace with actual temperature data
            dispatcher.utter_message(text=f"Температура сейчас {current_temperature} градусов")
        except Exception as e:
            dispatcher.utter_message(text="Извините, не могу определить температуру")
            print(f"Error: {e}")

        return []
