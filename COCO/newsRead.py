import requests
import pyttsx3
import json

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestNews():
    apidict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c1d719bcf678479cb59084f74cf1d99a",
               "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c1d719bcf678479cb59084f74cf1d99a",
               "technology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c1d719bcf678479cb59084f74cf1d99a",
               "sports" : "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c1d719bcf678479cb59084f74cf1d99a",
               "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=c1d719bcf678479cb59084f74cf1d99a",
               "science" : "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c1d719bcf678479cb59084f74cf1d99a"
}
    content = None
    url = None
    speak("which field of news do you want, type it please")
    type = input("Type the field of news you want among [Business, Entertainment, Health, Science, Sports, Technology]: ")
    for key, value in apidict.items():
        if key.lower() in type.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("here is the news")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"For more info visit: {news_url}")

        a = int(input("Press 1 to continue or press 2 to stop: "))
        if a == 1:
            pass
        elif a == 2:
            break
        speak("that's all about the news")
