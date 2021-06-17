import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import wolframalpha
import subprocess
import cv2
import sys
import numpy as np

face_cascade= cv2.CascadeClassifier('C:/Users/dell/Desktop/haarcascade_frontalface_default.xml')
cap= cv2.VideoCapture(0)


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 160)

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
        talk("so, tell me")

    elif hour>=12 and hour<18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
        talk("so, tell me")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")
        talk("so, tell me")

wishMe()


def take_command():
    try:
        with sr.Microphone() as source:
            print('J.A.R.V.I.S is listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)

    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        print('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what' in command:
        smth = command.replace('what', '')
        result = wikipedia.summary(smth)
        print(result)
        talk(result)

    elif 'recognise faces now' in command:
        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()


    elif "hibernate" in command or "sleep" in command:
        talk("Hibernating now")
        subprocess.call("shutdown /h /f -c J.A.R.V.I.S is hibernating this PC ")

    elif 'joke' in command:
        jk = command.replace('joke', '')
        jks = pyjokes.get_joke()
        print(jks)
        talk(jks)
    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")

    elif 'do you have a girlfriend' in command:
        talk('yeah, i have more than you have ever had haa haa haa haa haa')

    elif 'thank you' in command:
        talk('your welcome yuss')
        print('your welcome yuss')
    elif 'search' in command:
        ggle = command.replace('search', '')
        vxl= pywhatkit.search(ggle)
        talk(vxl)
        print(vxl)

    elif "calculate" in command:

        app_id = "GU85HE-JTY457A27P"
        client = wolframalpha.Client(app_id)
        indx = command.lower().split().index('calculate')
        query = command.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        talk("The answer is " + answer)

    elif "who made you" in command or "who created you" in command or "who discovered you" in command:
        talk("I was built by Yuss")
        print("I was built by Yuss")

    elif 'who is yuss' in command or 'who the heck is yuss' in command or '.....is yuss':
        talk(
            'yuss is a billionaire philantrophist who created the jarvis project and is currently living in..... ohh, I cant tell you that sorry')
        print(
            'yuss is a billionaire philantrophist who created the jarvis project and is currently living in..... ohh, I cant tell you that sorry')

    elif 'show me the computer processes' in command or 'show me the tasks running' in command:
        talk('highlighting now yuss')
        tskl=subprocess.call("tasklist")
        talk(tskl)
        print(tskl)
while True:
    run_jarvis()
