import os
import pyttsx3
import pyautogui
import webbrowser
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictApp = {"commandline" : "cmd", "paint": "paint", "excel": "excel", "word": "winword", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpoint"}

def openapp(query):
    speak("launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("coco", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")

    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictApp[app]}")

def close_app(query):
    speak("Closing, sir")

    if any(keyword in query for keyword in ["one tab", "1 tab", "two tab", "2 tab", "three tab", "3 tab", "four tab", "4 tab"]):
        tabs_to_close = int(''.join(filter(str.isdigit, query)))
        for _ in range(tabs_to_close):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("All tabs closed")

    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictApp[app]}.exe")