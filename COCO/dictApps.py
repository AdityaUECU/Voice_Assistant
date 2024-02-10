import pyttsx3
import pyautogui


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def open_app(query):
    query = query.replace("open", "")
    query = query.replace("coco", "")
    pyautogui.press("super")
    pyautogui.typewrite(query)
    pyautogui.press("enter")
    speak("the app has been opened")
def close_app(query):
    query = query.replace("close", "")
    query = query.replace("coco", "")

    pyautogui.hotkey('alt', 'f4')
    speak("the app has been closed")



