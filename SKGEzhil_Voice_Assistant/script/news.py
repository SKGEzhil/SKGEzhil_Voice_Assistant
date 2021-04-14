import requests
import pyttsx3
from SKGEzhil_Voice_Assistant.script import config

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def news_report():
    try:
        results = []
        url = f'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={config.news_api}'
        response = requests.get(url)
        x = response.json()
        articles = x["articles"]
        for titles in articles:
            results.append(titles["title"])
        talk("Here are some top head lines I have found for you ")
        for i in range(len(results)):
            if i >= 3:
                continue
            print(i + 1, results[i])
            news = i + 1, results[i]
            talk(news)
    except Exception as e:
        print(e)