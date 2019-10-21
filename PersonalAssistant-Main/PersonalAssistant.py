import time
import os
import sys
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
import playsound
import requests, json
import math
import pyttsx3 
from urllib.request import urlopen



def speak(text):
    engine = pyttsx3.init() 
    engine.setProperty('rate', 165)
    engine.say(text) 
    engine.runAndWait() 
    
  

def get_weather_data(city):
    api_key = "API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = math.floor(y["temp"] - 273)
        z = x["weather"]
        weather_description = z[0]["description"]
        return 'Temperature in {} is {} degree celsius with {}.'.format(city, current_temperature, weather_description)

    else:
        return " City Not Found "


def get_audio():
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


def get_weather(text):
    text = text.lower()
    word = text.split()

    if text.find("temperature") > -1:
        pos = word.index('temperature')
        data = get_weather_data(word[pos+2])
        print(data)
        speak(data)

    elif text.find("climate") > -1:
        pos = word.index('climate')
        data = get_weather_data(word[pos+2])
        print(data)
        speak(data)

    elif text.find("weather") > -1:
        pos = word.index('weather')
        data = get_weather_data(word[pos+2])
        print(data)
        speak(data)

    else:
        return None


def check_connection():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
    except:
        return False


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    speak('the time is {}'.format(current_time))

def run():

    if check_connection() == True:
        said_line = get_audio()

        if said_line.find("weather") > -1 or said_line.find("climate") > -1 or said_line.find("temperature") > -1:
            get_weather(said_line)

        elif said_line.find("time") > -1:
            get_time()

        elif said_line.find("go offline") > -1:
            speak("shutting down")
            sys.exit()

    elif check_connection()== False:
        print("Check your Internet Connection!")
        sys.exit()


    
while True:
    run()