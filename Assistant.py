import datetime
import sys
import time
import pyautogui
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib

engine = pyttsx3.init ('sapi5')
voices = engine.getProperty ('voices')
# print(voice
# s[0].id)
engine.setProperty ('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say (audio)
    print (audio)
    engine.runAndWait ( )


# convert voice to text
def takecommand():
    r = sr.Recognizer ( )
    with sr.Microphone ( ) as source:
        print ("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print ("Recognizing....")
        query = r.recognize_google (audio, language='en-in')
        print (f"Mamona Said, {query}")

    except Exception as e:
        speak ("Say that again please ma'am...")
        return "none"
    return query


# to wish
def wish():
    hour = int (datetime.datetime.now( ).hour)
    tt = time.strftime("%H: %M: %S")

    if hour >= 0 and hour <= 12:
        speak (f"Good Morning, its {tt} AM")
    elif hour > 12 and hour < 18:
        speak (f"Good afternoon, its {tt} PM")
    elif hour > 18 and hour < 22:
        speak (f"Good evening, its {tt} PM")
    else:
        speak (f"Good night, its{tt} PM")
    speak ("Ma'am. please tell me How can I help you")


#to send email
def sendEEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Your email adress','your password')
    server.sendmail('type email ', to, content)
    server.close()


# FOR NEWS UPDATEs
def news():
    main_url = 'https://newsapi.org/v2/everything?q=Apple&from=2022-12-11&sortBy=popularity&apiKey=3b13129071e348c2b1963db14f579cb2'

    main_page = requests.get(main_url).json()
    #print(main page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


if __name__ == "__main__":
    wish()
    while True:
    # if 1:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open code" in query:
            npath = "F:\\Microsoft VS Code\\code.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("Start cmd")

        elif "open courses" in query:
            npath = "D:\\EE courses.exe"
            os.startfile(npath)

        elif "open Pakistan study" in query:
            npath = "D:\\EE courses\\Pak Studies.exe"
            os.system(npath)

        elif "Open algebra" in query:
            npath = "D:\\EE courses\\Algebra and ODE'S.exe"
            os.system(npath)

        elif "open mechanics" in query:
            npath = "D:\\EE courses\\Engineering mechanics.exe"
            os.system(npath)

        elif "open workshop" in query:
            npath = "D:\\EE courses\\Workshop.exe"
            os.system(npath)
        
        elif "open com skills" in query:
            npath = "D:\\EE courses\\Com Skills.exe"
            os.system(npath)
        
        elif "open Electrical network analysis" in query:
            npath = "D:\\EE courses\\Electrical Network Analysis.exe"
            os.system(npath)


        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =5)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif 'open WhatsApp' in query:
           webbrowser.open("www.WhatsApp.com")

        elif 'open instagram' in query:
           webbrowser.open("www.instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"Ma'am , the time is {strTime}")

        elif 'introduce yourself' in query:
            speak("Hello! I am Desktop assistant.")

        
        elif 'open google' in query:
            speak("what should I search on google Ma'am? ")
            cm = takecommand().islower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("friend's number with country code", "Assalam o Aalaikum", 11,50)
            pyautogui.press ("enter")

        elif 'play song on youtube' in query:
            kit.playonyt("on my way")

        elif 'email to friend' in query:
            try:
                speak("what should I say ma'am? ")
                content = takecommand().lower()
                to = "reciever's email adress"
                sendEEmail(to, content)
                speak("Email has been sent to your friend ma,am")

            except Exception as e:
                print(e)
                speak("Sorry ma'am, I'm unable to send this email to your friend")

        elif 'you can sleep' in query:
            speak("Thanks for using me Ma'am, Have a good day")
            sys.exit()

      
    # to close any app
        elif "close notepad" in query:
            speak("Okay Ma'am I'm closing notepad. ")
            os.system("taskkill /f /im notepad.exe")
        elif "close command prompt" in query:
            speak("Okay ma'am I am closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif"set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'E:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[1]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown/s")
        elif "restart the system" in query:
            os.system("shutdown/r")
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendtate 0,1,0")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait ma'am,I am fetching the news for you....")
            news()

        # speak("Anything else ma'am...")

        # to hide files and folders

        elif "hide all files" in query or "hide this folder" in query or "make it visible for everyone" in query:
            speak("Ma'am, please tell me do you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("Ma'am, all the files in this folder are now hidden. I hope you won't regret at this decision")

            elif "visible" in query:
                os.system("attrib -h /s /d")
                speak("Ma'amm, all the files in this folder are now visible to everyone. ")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok, ma'am")
