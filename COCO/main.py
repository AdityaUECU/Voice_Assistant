import datetime
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import pyautogui
import speedtest


from INTRO import play_gif
play_gif

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



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greet import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you")
                elif "i m fine" in query:
                    speak("that's great sir")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "how r u" in query:
                    speak("Perfect sir")
                elif "thank" in query:
                    speak("you're welcome sir")
                elif "open" in query:
                    from dictApps import open_app
                    open_app(query)
                elif "close" in query:
                    from dictApps import close_app
                    close_app(query)
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "resume video" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video mute")
                elif "volume up" in query:
                    from keyboard import volumeup
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    volumedown()
                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchnow import searchWiki
                    searchWiki(query)
                elif "temperature" in query:
                    search = "temperature in Ujjain"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in Ujjain"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "news" in query:
                    from newsRead import latestNews
                    latestNews()
                elif "whatsapp" in query:
                    from whatsapp import sendMsg
                    sendMsg()

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload = wifi.upload()/1048576
                    down = wifi.download()/1048576
                    print(f"Wifi Upload speed is {upload} MB")
                    print(f"Wifi Download speed is {down} MB")
                    speak(f"Wifi Upload speed is {upload} MB")
                    speak(f"Wifi Download speed is {down} MB")


                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Sir, the time is: {strTime}")
                    speak(f"Sir, the time is: {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep, Sir!")
                    exit()

                elif "remember that" in query:
                    msg = query.replace("remember that", "")
                    msg = query.replace("coco", "")
                    speak("you told me"+ msg)
                    remember = open("remember.txt", "w")
                    remember.write(msg)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("you told me" + remember.read())
