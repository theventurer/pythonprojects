import wolframalpha
app_id = 'TVGYHV-AA7WU2YXW9'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)
import wikipediaapi
import webbrowser
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" #note the double \ syntax
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
import os
import duckduckgo
import datetime
import smtplib
import speech_recognition as sr

# answer = next(res.results).text
# print(answer)
import PySimpleGUI as sg
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    print('Jarvis:'+audio)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis, how may I help you")
def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
        return query
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('theventurer1234@gmail.com', 'Cooldude1234')
    server.sendmail('theventurer1234@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            if 'search wikipedia for' in query:
                query = query.replace("search wikipedia for", "")
            elif 'search wikipedia' in query:
                query = query.replace("search wikipedia", "")
            elif 'wikipedia' in query:
                query = query.replace("wikipedia", "")            
            wiki_wiki = wikipediaapi.Wikipedia('en')
            p_wiki = wiki_wiki.page(query)
            wiki_exist=p_wiki.exists()
            if wiki_exist == True:
                speak("According to Wikipedia")
                sg.PopupNonBlocking(p_wiki.title,p_wiki.summary[0:300])
                speak(p_wiki.summary[0:300])          
        elif 'quit' in query:
            print("Okay, I am quitting")
            speak("Thank you, have a nice day")
            break
        elif 'stop' in query:
            print("Okay, I am quitting")
            speak("Thank you, have a nice day")
            break
        elif 'bye' in query:
            print("Okay, I am quitting")
            speak("Thank you, have a nice day")
            break
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'play music' in query:
            os.system('start C:\\Users\\DELL\\Desktop\\Spotify.lnk')
        elif 'who made you' in query:
            print("Mr Divyanshu Bose")
            speak("My inventor is Divyanshu, he is a cool guy.")
        elif 'sorry' in query:
            print("Okay, Repeat that")
            speak("I am listening, repeat that")
        elif 'email to divyanshu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bose.divyanshu@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email") 
        elif 'none' == query:
            print("Please speak properly..")
            speak("I think you are busy,I'll be leaving then. Have a nice day")
            break
        else:
            try:
                res = client.query(query)
                wolfram_res=next(res.results).text
                sg.popup_non_blocking(query,wolfram_res)
                speak(wolfram_res)
            except Exception as e:
                duck_res = duckduckgo.get_zci(query)
                if 'http' in duck_res:
                    speak('I am opening browser for your result')
                    webbrowser.open(duck_res)
                else:
                    sg.PopupNonBlocking(duck_res)
                    speak(duck_res)
# Finish up by removing from the screen
# window.close()
