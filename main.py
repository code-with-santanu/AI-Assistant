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

        elif 'date' in query:
            date()

        elif ('wikipedia' in query) or ('search' in query):
            speak('searching.....')
            query = query.replace('wikipedia', "")
            query = query.replace('search', "")
            if 'in details' in query:
                query = query.replace('in details', "")
                search(query, 20)
            elif 'in short' in query:
                query = query.replace('in short', "")
                search(query, 5)
            else:
                search(query, 2)

        elif 'offline' in query:
            offline()
