import wolframalpha
app_id = 'TVGYHV-AA7WU2YXW9'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)
import wikipediaapi
import speech_recognition as sr
# answer = next(res.results).text
# print(answer)
import PySimpleGUI as sg
import pyttsx3
engine = pyttsx3.init()
engine.say("Welcome, I am Jarvis. Type your command")
engine.runAndWait()
sg.theme('Darkpurple')
# Define the window's contents
layout = [[sg.Text("Enter a command")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1),key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Jarvis', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    else:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        p_wiki = wiki_wiki.page(values['-INPUT-'])
        wiki_exist=p_wiki.exists()

        # Output a message to the window

        if wiki_exist==True:
            engine.say(p_wiki.summary[0:300])
            sg.PopupNonBlocking(p_wiki.title,p_wiki.summary[0:300])
            engine.runAndWait()
            engine.stop()
        else:
            res = client.query(values['-INPUT-'])
            wolfram_res = next(client.query(values['-INPUT-']).results).text
            engine.say(wolfram_res)
            window['-OUTPUT-'].update(wolfram_res)
            sg.PopupNonBlocking(values['-INPUT-'],wolfram_res)
            engine.runAndWait()
            engine.stop()
# Finish up by removing from the screen
window.close()
