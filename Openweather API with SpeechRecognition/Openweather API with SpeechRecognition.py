import time
import os
import speech_recognition as sr
from gtts import gTTS
import playsound
import requests, json
import math
import pickle

weather_call_type = ["waeather", "temperature", "climate"]


def speak(text):
    tts = gTTS(text = text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_weather_data(city):
    api_key = "Your_API_Key"
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
    if text.find("temperature") and len(word) > 5:
        data = get_weather_data(word[5])
        print(data)
        speak(data)

    elif text.find("climate") and len(word) > 5:
        data = get_weather_data(word[5])
        print(data)
        speak(data)
        
    elif text.find("weather") and len(word) > 5:
        data = get_weather_data(word[5])
        print(data)
        speak(data)

    else:
        return None


get_weather(get_audio())
