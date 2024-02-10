import datetime
import pyttsx3
import speech_recognition as sr
import os
from datetime import timedelta
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import pywhatkit

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-us")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that Again.\n")
        return "none"
    return query


strtime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))


def sendMsg():
    speak("who do you want to message")
    a = int(input("Press 1(Rushil)\nPress 2(Aditya): "))
    if a == 1:
        speak("what's the message")
        msg = str(input("Enter the Message: "))
        pywhatkit.sendwhatmsg("+91000000000", msg, time_hour=strtime, time_min=update)
    elif a == 2:
        speak("what's the message")
        msg = str(input("Enter the Message: "))
        pywhatkit.sendwhatmsg("+916261692458", msg, time_hour=strtime, time_min=update)
