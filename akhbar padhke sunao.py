# from tokenize import Special
import imp
import json
import time
from traceback import print_tb
from typing import final
import requests
def speak(str,str2):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    print("Reading Title")
    speak.Speak(str)
    print("Reading Content")
    time.sleep(1)
    speak.Speak(str2)

url = ('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c326e0ebd7924f2a99f5eb8ab09e8fb2')

response = requests.get(url)
# print(response.content)
data = json.loads(response.content)
finaldata=data['articles'][0]['title']
finaldata2=data['articles'][0]['content']

speak(finaldata,finaldata2)