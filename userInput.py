from speak import *

import speech_recognition as sr


def takeCommand():
    rec = sr.Recognizer()  # initializing the recognizer
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)

    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry! can't recognize it. Please try again")

        return "None"

    return query
