# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json
# from deep_translator import GoogleTranslator
# from weather import get_weather
from deep_translator import GoogleTranslator
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        url = "https://open-weather13.p.rapidapi.com/city/"+city
        headers = {
	"X-RapidAPI-Key": "b7c95a2b0emsh5ab07abe99f3d2bp1c0fc5jsn0ad4e1a3eacf",
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
  }
        response = json.loads(requests.request("GET",url=url, headers=headers,params={'lang':'ar'}).text)
        w=response.get('weather')[0].get('description')
        translated = GoogleTranslator(source='auto', target='ar').translate(w)
  
        
        dispatcher.utter_message(translated)
 
        return []
