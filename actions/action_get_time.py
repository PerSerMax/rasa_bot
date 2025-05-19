from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime



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