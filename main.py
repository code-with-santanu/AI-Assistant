from speak import *
from userInput import *
from myAssistant import *


if __name__ == "__main__":

    while (True):
        query = takeCommand().lower()
        if 'alfred' in query:
            greet()
            break
        else:
            speak("sorry! I didn't get it")

    while (True):
        query = takeCommand().lower()

        if 'time' in query:
            time()
        if 'date' in query:
            date()
        if 'offline' in query:
            offline()
