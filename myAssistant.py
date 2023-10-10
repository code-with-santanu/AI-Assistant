from speak import *

import datetime
import wikipedia


def greet():
    speak("welcome back mr. Santanu")
    hour = datetime.datetime.now().hour
    if (hour >= 4 and hour < 12):
        speak("Good morning sir")
    elif (hour >= 12 and hour < 17):
        speak("Good afternoon sir")
    elif (hour >= 17 and hour < 20):
        speak("Good evening sir")
    else:
        speak("Good night sir")

    speak("alfred at your service. how can I help you?")


def offline():
    speak('thank you')
    speak('going offline')
    quit()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("today's date is ")
    speak(day)
    speak(month)
    speak(year)


def search(query, line):
    result = wikipedia.summary(query, sentences=line)
    print(result)
    speak(result)
