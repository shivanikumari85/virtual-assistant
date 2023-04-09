import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
# import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")

    speak("Hello Boss, I am Jarvis. Please tell me, how can I help you")


# it takes microphone input from the user and return string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kumari.shivani.1164@gmail.com', 'shivani@2021')
    server.sendmail('kumari.shivani.1164@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        # if 1:
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\My Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1.3\\bin\\pycharm64.exe"
            os.startfile(codepath)

        elif 'open file' in query:
            codepath = "C:\\Users\\shivani\\Documents"
            os.startfile(codepath)

        elif 'open code' in query:
            codepath = "C:\\Users\\shivani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'mail to boss' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "shivanikumar1929@gmail.com"
                sendmail(to, content)
                speak("Mail has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry boss. I am not able to send this mail")