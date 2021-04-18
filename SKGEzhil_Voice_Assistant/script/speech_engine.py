import pyttsx3
import speech_recognition as sr
# PyAudio~=0.2.11

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


engine = pyttsx3.init()
engine.setProperty('rate', 145)
engine.setProperty('volume', 2)
engine.setProperty('voice', 'english')


def talk(text):
    engine.say(text)
    engine.runAndWait()
