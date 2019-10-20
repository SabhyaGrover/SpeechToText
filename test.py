import pyaudio
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Tell me something:")
    engine.say('Say something')
    engine.runAndWait()
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        translate = r.recognize_google(audio)
        print("You said:- " + translate)
    except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')
            engine.runAndWait()