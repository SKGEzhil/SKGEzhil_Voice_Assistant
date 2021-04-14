import requests

from SKGEzhil_Voice_Assistant.script import config
from SKGEzhil_Voice_Assistant.script.speech_engine import talk


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
