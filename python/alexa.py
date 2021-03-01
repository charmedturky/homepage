import speech_recognition as sr
import pyttsx3
import webbrowser 
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess

listener = sr.Recognizer() 
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[26].id)
engine.say("What can I du for you")
engine.runAndWait()

try:
    with sr.Microphone() as source: 
        print("listening...")   
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)

    if "play music" in command:
       webbrowser.open_new("https://www.youtube.com/watch?v=nqggm9o2Z9k&list=PLudsWki_g-JUCAr_X6cRtdY4WycZ88tvn")
         
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        engine.setProperty("voice", voices[22].id)
        engine.say(time)
        engine.runAndWait()

    elif "search" in command:
        person = command.replace("search","") 
        info = wikipedia.summary(person, 10)
        engine.setProperty("voice", voices[26].id)
        engine.say(info)
        engine.runAndWait()
        print(info)
    if "open gmail" in command:
        webbrowser.open_new("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    if "joke" in command:
        joke = pyjokes.get_joke() 
        engine.setProperty("voice", voices[26].id)
        engine.say(joke)
        print(joke)
        engine.runAndWait()  
    if "open youtube" in command:
        webbrowser.open_new("https://www.youtube.com/")
       
    if "messages" in command:
        webbrowser.open_new("https://web.whatsapp.com/")
        engine.setProperty("voice", voices[26].id)
        engine.say("We will see")
        engine.runAndWait()
    if "food" in command:
        webbrowser.open_new("https://dsporto.unicard.pt/UnicardSIGE_Portal")
    if "teams" in command:
       subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Microsoft Teams.app"]
    ) 
    if "app store" in command:
       subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/App Store.app"]
    ) 
    if "teams" in command:
       subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/QuickTime Player.app"]
    ) 
    if "zoom" in command:
       subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Zoom.app"]
    ) 
    if "system preferences" in command:
       subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/System Preferences.app"]
    ) 
    if "finder" in command:
       subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Finder.app"]
    ) 
    if "text edit" in command:
        subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app"]
    )
    if "open my portuguese lesson of monday" in command:
         webbrowser.open_new("https://us04web.zoom.us/j/77064948232?pwd=VVFtME1Ld1VvaW8xQnhoRDIxTUpKdz09")
    if "open my portuguese lesson of tuesday" in command:
         webbrowser.open_new("https://us04web.zoom.us/j/79606340052?pwd=MWJRQlFVYWJ4bG1vVXY5dmNpa1oxdz09")
    if "open my portuguese lesson of thursday" in command:
         webbrowser.open_new("https://us04web.zoom.us/j/71128583022?pwd=ZGFMMlJ0ZTNMMXcrOTh1dC8wQ1htZz09")

except:

    pass