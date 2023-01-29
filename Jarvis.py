import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

#To set the JARVIS voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

#to say anything by JARVIS
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#To wish 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("Good Morning Sir")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("i am jarvis .how can i help you?")

#To take command from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognition.....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: "+query)

    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query

wishMe()
while(True):
    query = takeCommand().lower()

    #To search anything on google
    if ('wikipedia' in query):
        speak("Searching wikipedia! please wait")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=3)
        print(result)
        speak("do you want to listen the data ?")
        choice = takeCommand().lower()
        if ("yes" in choice):
            speak("according to wikipedia "+result)
        else:
            continue       

    #To ask question
    elif ('who are you' in query):
        speak('I AM JARVIS.')

    elif ('full form of jarvis' in query):
        speak('the full form of JARVIS is Just A Rather Very Intellgent System')

    #To open whatsapp web
    elif ('open whatsapp' in query):
        speak("opening whatsapp")
        webbrowser.open('web.whatsapp.com')

    #Search for youtube
    elif ('open youtube' in query):
        speak("opening youtube")
        webbrowser.open('youtube.com')

    #To open online c compiler
    elif ('open online compiler' in query):
        speak('openning compiler')
        webbrowser.open('onlineGDB.com')

    #To open google
    elif ('open google' in query):
        speak("opening google")
        webbrowser.open("google.com")

    #To show time
    elif('time' in query):
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        print(str(Time))
        speak("It's"+str(Time))

    #To open Visual Studio Code
    elif('open vs code' in query):
        speak('opening visual stdio code')
        vs_code_path = "C:\\Users\\naruto\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vs_code_path)


    #To stop the program
    elif('stop' in query):
        speak('Thank You Sir')
        exit()