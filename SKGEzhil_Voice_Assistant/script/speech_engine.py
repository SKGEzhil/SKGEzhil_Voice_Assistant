import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        audio = r.listen(source)
        try:
            print("Recognizing Now .... ")
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")
            return r.recognize_google(audio)
        except Exception as e:
            print("Error :  " + str(e))
            print('error: command not received')
            return 'command not received'
