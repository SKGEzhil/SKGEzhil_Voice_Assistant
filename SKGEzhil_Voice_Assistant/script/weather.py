import requests
import pyttsx3
import time
from SKGEzhil_Voice_Assistant.script import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from SKGEzhil_Voice_Assistant.script.speech_engine import talk,take_command

def location():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path='SKGEzhil_Voice_Assistant/chromedriver.exe', chrome_options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    return latitude, longitude

def weather_report(city_name):
    try:
        api_key = config.weather_api
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        city_name = city_name
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        print(complete_url)
        response = requests.get(complete_url)
        x = response.json()
        print(x["cod"])
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            celcius = current_temperature - 273
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talk(" Temperature is " +
                 str(round(celcius)) + 'degree celcius' +
                 "\n humidity is " +
                 str(current_humidiy) + 'percentage' +
                 "\n description  " +
                 str(weather_description))
            print(" Temperature is = " +
                  str(round(celcius)) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
        if x["cod"] == "404":
            url = f'http://api.openweathermap.org/data/2.5/weather?lat={location()[0]}&lon={location()[1]}&appid={config.weather_api}'
            print(url)
            response = requests.get(url)
            x = response.json()
            y = x["main"]
            current_temperature = y["temp"]
            celcius = current_temperature - 273
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talk(" Temperature is " +
                 str(round(celcius)) + 'degree celcius' +
                 "\n humidity is " +
                 str(current_humidiy) + 'percentage' +
                 "\n description  " +
                 str(weather_description))
            print(" Temperature is = " +
                  str(round(celcius)) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
    except Exception as e:
        print(e)
        url = f'api.openweathermap.org/data/2.5/weather?lat={location()[0]}&lon={location()[1]}&appid={config.weather_api}'
