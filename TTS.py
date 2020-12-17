import pyttsx3


while True:
    engine = pyttsx3.init()
    print("Yes: ")
    txt = input()
    if(txt == 'q'):
        quit()
    engine.say(txt)
    engine.runAndWait()
