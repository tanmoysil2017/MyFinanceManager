import speech_recognition as sr
import pyttsx3

# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

try:

    engine = pyttsx3.init()
    engine.say('You said')
    engine.say(str(r.recognize_google(audio)))
    engine.runAndWait()

    # print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
