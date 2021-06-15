import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 160)

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")

        talk('i am loading')

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
        command = command.replace("search", "")
        webbrowser.open_new_tab(command)
        talk('here are the results from google, yuss')

    elif "who made you" in command or "who created you" in command or "who discovered you" in command:
        talk("I was built by Yuss")
        print("I was built by Yuss")

    elif 'who is yuss' in command or 'who the heck is yuss' in command or 'is yuss':
        talk('yuss is a billionaire philantrophist who created the jarvis project and is currently living in..... ohh, I cant tell you that sorry')
        print('yuss is a billionaire philantrophist who created the jarvis project and is currently living in..... ohh, I cant tell you that sorry')

    else:
        talk('say that again yuss, i didnt get it')

while True:
    run_jarvis()