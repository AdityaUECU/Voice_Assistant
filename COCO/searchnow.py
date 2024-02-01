import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that Again.")
        return "none"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("coco", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found on youtube")
        query = query.replace("coco", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)

def searchWiki(query):
    if "wikipedia" in query:
        speak("Searching form wikipedia....")
        query = query.replace("coco", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia.....")
        print(result)
        speak(result)