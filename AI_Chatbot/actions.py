from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted
from typing import Any, Text, Dict, List
from rasa_core_sdk.executor import CollectingDispatcher
import requests
import json
import re
import feedparser

def name_cap(text):
    tarr = text.split()
    for idx in range(len(tarr)):
        tarr[idx] = tarr[idx].capitalize()
    return ' '.join(tarr)

class action_get_lottery(Action):
   def name(self):
          return 'action_get_lottery'
   def run(self, dispatcher, tracker, domain):
            url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
            feed_cnt = feedparser.parse(url)
            first_node = feed_cnt['entries']
            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
            dispatcher.utter_message(return_msg)
            return []


# class ActionLookUpWordDictionary(Action):
#     def name(self) -> Text:
#         return 'action_lookUp_en'
# 
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         word = str(tracker.get_slot('enword')).lower()
#         print(word)
#         if not word:
#             dispatcher.utter_message("Đôi lúc sự thông thái của tôi cũng có giới hạn!")
#             return []
#         url = 'https://api.tracau.vn/WBBcwnwQpV89/s/{}/en'.format(word)
#         response = requests.get(url).text
#         json_data = json.loads(response)['tratu'][0]['fields']['fulltext']
#         try:
#             pro = re.search(r"<\s*tr\s+id\s*=\s*\"pa\"[^>]*>.+?<\s*\/\s*tr>", json_data).group()
#             tl = re.search(r"<\s*tr\s+id\s*=\s*\"tl\"[^>]*>.+?<\s*\/\s*tr>", json_data).group()
#         except e1:
#             print(e1)
#
#         try:
#             meanings = re.findall(r"<\s*tr\s+id\s*=\s*\"mn\"[^>]*>.+?<\s*\/\s*tr>", json_data)
#         except Exception:
#             dispatcher.utter_message("Đôi lúc sự thông thái của tôi cũng có giới hạn!")
#             return []
#
#         pro = re.sub(r"<\s*[^>]+>", "", pro)
#         tl = re.sub(r"<\s*[^>]+>", "", tl)
#         for i in range(len(meanings)):
#             meanings[i] = re.sub(r"<\s*[^>]+>", "", meanings[i])
#         text_respond = "=> " + word.title()
#         if pro is not None:
#             text_respond +=  pro.replace("◘", " ")
#         if tl is not None:
#             text_respond += "\n" + tl.replace("*", "* ")
#         if meanings:
#             for mean in meanings:
#                 if mean is not None:
#                     text_respond += "\n" + mean.replace("■", "  -  ")
#
#             dispatcher.utter_message("Bằng sự thông thái của tôi, đây là thứ bạn cần tìm:\n" + text_respond)
#         else:
#             dispatcher.utter_message("Đôi lúc sự thông thái của tôi cũng có giới hạn!")
#             return []
#
#         return []
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []