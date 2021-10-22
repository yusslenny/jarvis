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
import os
from random import randint
import requests

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
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

def goto(linenum):
    global line
    line = linenum

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
        subprocess.call("shutdown /h /f -t 66 -c J.A.R.V.I.S is hibernating this PC ")

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
        talk('here are the results from google')
        print("here are the results from google")

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

    elif 'who is yuss' in command or 'who the heck is yuss' in command:
        talk(
            'yuss is a billionaire philantrophist who created the jarvis project and is currently living in..... ohh, I cant tell you that sorry')
        print(
            'yuss is a billionaire philantrophist who created the jarvis project and is currently living in..... ohh, I cant tell you that sorry')

    elif 'show me the computer processes' in command or 'show me the tasks running' in command:
        talk('highlighting now yuss')
        tskl=subprocess.call("tasklist")
        talk(tskl)
        print(tskl)

    elif 'repeat the statement' in command or 'repeat what i say' in command:
        talk("ok what do you want me to say")
        import time
        time.sleep(1)
        sya = take_command()
        talk(sya)

    elif 'do something fun' in command:

        talk("ok yuss, choose between the following categories.....we have movies...songs...music artists .......jokes .......comics")

        req = take_command()

        if 'movies' in req:
            talk('ok yuss....here are a list of upcoming movies from rotten tomatoes')
            print(req)
            webbrowser.open_new_tab('https://editorial.rottentomatoes.com/article/most-anticipated-movies-of-2021/')



        elif'songs' in req:
            talk('what type of music do you listen to?')
            talk('we have gospel.......hiphop......RnB......Pop')
            print(req)
            sng = take_command()

            if 'hiphop' in sng:
                talk('you can look thorough the following tracks i pulled up on genius.com')
                print('you can look thorough the following tracks i pulled up on genius.com')
                webbrowser.open_new_tab('https://genius.com/artists/Rap-genius')

            elif 'gospel' in sng:
                talk('look at the following gospel tracks from you')
                print('look at the following gospel tracks from')
                webbrowser.open_new_tab('https://www.udiscovermusic.com/stories/praise-best-gospel-songs-time/')

                talk('or if you want i can open gospel tracks from youtube')
                print('or if you want i can open gospel tracks from youtube')

                gsp = take_command()
                if "yes" in gsp:
                    talk('alright,.....here are some popular and uplifting songs you can select from youtube')
                    print('alright,.....here are some popular and uplifting songs you can select from youtube')
                    webbrowser.open_new_tab('https://www.youtube.com/results?search_query=great+gospel+songs+of+all+time')

                else:
                    talk('ok then.......you can browse the ones on youdiscover music then')
                    run_jarvis()


            elif 'pop' in sng:
                talk('here are the latest pop tracks you might like')
                print('here are the latest pop tracks you might like')

            elif 'RnB' in sng:
                talk('i pulled up latest RnB tracks....check them out')
                print('i pulled up latest RnB tracks....check them out')
            else:
                talk('sorry but i dont know of that genre yet........ but if you need to do anything fun,..... just tell me')
                run_jarvis()

    elif 'give me a random word' in command:
        url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text%2Fplain'
        r = requests.get(url)
        text = r.text

        word = text.split()
        rndwrd = randint(0, len(word))

        print(word[rndwrd])
        
    elif " list sub processes" in command:
        subprocess.call("help")
        talk("here are a list of available windows batch commands")
        print("here are a list of available windows batch commands")
        llp=take_command()
        
            if "disk part" in llp:
                talk
                subprocess.call("diskpart")
                
            else:
            talk("i currently do not have the sub process requested")
            print("i currently do not have the sub process requested")
            run_jarvis
    elif "show me all the live matches" in command:
        talk("showing current matches from hesgoal.com")
        print("showing current matches from hesgoal.com")
        webbrowser.open_new_tab('hesgoal.com')
            take_command()
            #to be continued
    
    elif "scan for wifi networks" in command:
        os.system('cmd /c "netsh wlan show networks"')
        
while True:
    run_jarvis()
