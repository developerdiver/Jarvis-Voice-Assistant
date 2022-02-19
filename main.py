import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
 

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening!")        
    speak("Hii everyone, this project work have been made by me.")
    speak("it is a prject which is used to automate different daily activities")
    speak("the activities can be asked to do as a form of audio input.")
    speak("I'm jarvis sir. please tell me how may I help you")

def takeCommand():
    '''
    it is taking command from 
    the user with the help of microphone.
    and returns string as the output.
    '''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)    
    

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language= 'en-US') 
        print(f"User said:{query}\n")   
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo
    server.starttls()
    server.login('19bcs2505@cuchd.in','xyz')
    server.sendmail('abparasar99@gmail.com',to,content)
    server.close()


if _name_ == "_main_":
    wishMe()
    while True: 

        query= takeCommand().lower()
        if 'wikipedia' in query:
             speak("Searching wikipedia...")
             query = query.replace("wikipedia","")
             results= wikipedia.summary(query,sentences= 2)
             speak("According to wikipedia")
             print(results)
             speak (results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = ""
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime}")

        elif 'open code' in query:
            codePath= "C:\\Users\\abpar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codePath)
        
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content= takeCommand()
                to = "abparasar99@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print("sorry email not sent..pls try again")
