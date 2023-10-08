import pyttsx3 


# initialize the engine to speak
engine = pyttsx3.init()


# function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()