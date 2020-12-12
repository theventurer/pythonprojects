import wolframalpha
app_id = 'TVGYHV-AA7WU2YXW9'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)
import wikipediaapi
import duckduckgo
import datetime
import speech_recognition as sr

# answer = next(res.results).text
# print(answer)
import PySimpleGUI as sg
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
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

wishMe()
recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
        print("Listening...")
        recognizer.pause_thresold = 1
        audio = recognizer.listen(source)

output = recognizer.recognize_google(audio)
print(output)
# sg.theme('Darkpurple')
# Define the window's contents
# layout = [[sg.Text("Enter a command")],
#           [sg.Input(key='-INPUT-')],
#           [sg.Text(size=(40,1),key='-OUTPUT-')],
#           [sg.Button('Ok'), sg.Button('Quit')]]
#
# # Create the window
# window = sg.Window('Jarvis', layout)

# Display and interact with the Window using an Event Loop
# while True:
#     event, values = window.read()
#     # See if user wants to quit or window was closed
#     if event == sg.WINDOW_CLOSED or event == 'Quit':
#         break
#     else:
wiki_wiki = wikipediaapi.Wikipedia('en')
p_wiki = wiki_wiki.page(output)
wiki_exist=p_wiki.exists()

        # Output a message to the window
try:
    if wiki_exist==True:
            engine.say(p_wiki.summary[0:300])
            sg.PopupNonBlocking(p_wiki.title,p_wiki.summary[0:300])
            engine.runAndWait()
    else:
            res = client.query(output)
            wolfram_res=next(res.results).text
            engine.say(wolfram_res)
            # window['-OUTPUT-'].update(wolfram_res)
            sg.PopupNonBlocking(output,wolfram_res)
            engine.runAndWait()
except Exception as e:
    duck_res = duckduckgo.get_zci(output)
    sg.PopupNonBlocking(duck_res)
    engine.say(duck_res)
    engine.runAndWait()
# Finish up by removing from the screen
# window.close()
