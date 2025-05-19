from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime


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






