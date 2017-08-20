import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
import wolframalpha
import winshell
import win32com.client as wincl
import wikipedia
import ctypes
from Tkinter import *
import ttk
import time
from PIL import Image, ImageTk


speak = wincl.Dispatch("SAPI.SpVoice")

#Wolframalpha API I.D. 
app_id='PA237Q-XA42375UEE'   
client = wolframalpha.Client(app_id) 

chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' 
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path)) #Ensures Chrome opens instead of IE

root = Tk()

im = Image.open("C:/Python27/nature.jpg")
tkimage = ImageTk.PhotoImage(im)
myvar= Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)

time1 = ''
root.title('Jarvis')
#root.geometry()
root.state('zoomed')
clock = Label(root, font=('Comic Sans MS', 50), bg = "light blue")
clock.place(relx=0.5, rely=0.9, anchor=CENTER)
#welcome = Label(text = 'Welcome User', font=('Comic Sans MS', 40, 'bold'), bg = "light blue")
#welcome.place(relx=0.5, rely=0.1, anchor=CENTER)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()

#Converts speech to text
def initialize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak.Speak("Ask me to search anything, play any video on youtube, open mail, solve any math question, empty recycle bin, open desktop, look up something on wikipedia, and lock computer")
        print "Ask me to search anything, play any video on youtube, open mail, solve any math question, empty recycle bin, open desktop, look up something on wikipedia, and lock computer"
        print "Keywords: Search, Video, Mail, Math, recycle bin, desktop, wikipedia, lock computer"
        time.sleep(3)
        speak.Speak("I'm ready to listen")
        audio = r.listen(source)
    text = ''
    try:
        text = r.recognize_google(audio)
        print "Device thinks you said, " + text
    except sr.UnknownValueError:
        print "Device could not understand what you said"
    except sr.RequestError as e:
        print "Device could not receive request from user {0}".format(e)

    return text

#Takes command and does certain operation
def perform(text):
    if "search" in text:
        text = text.split()
        text = ' '.join(text[1:])
        speak.Speak("searching")
        webbrowser.get('chrome').open_new_tab('google.com/search?q=' + text)
    elif "video" in text:
        text = text.split()
        text = '+'.join(text[1:])
        speak.Speak("pulling up video")
        webbrowser.get('chrome').open_new_tab("youtube.com/results?search_query=" + text)
    elif "mail" in text:
        speak.Speak("opening mail")
        webbrowser.get('chrome').open_new_tab('portal.office.com')
    elif "math" in text:
        r2 = sr.Recognizer()
        with sr.Microphone() as source:
            speak.Speak("Ask your math question")
            audio2 = r2.listen(source)
        question = ''
        try:
            question = r2.recognize_google(audio2)
            print "Device thinks you said, " + question
            try: 
                res = client.query(question)
                ans = (next(res.results).text)
                speak.Speak(ans)
                print ans
            except:
                speak.Speak('I don\'t understand your question')
            #print ans
        except sr.UnknownValueError:
            print "Device could not understand what you said"
        except sr.RequestError as e:
            print "Device could not receive request from user {0}".format(e)
        
    elif "recycle bin" in text:
        recycle_bin = winshell.recycle_bin()
        speak.Speak("emptying recycle bin")
        recycle_bin.empty(confirm=False, show_progress=False, sound=True)
    elif "desktop" in text:
        speak.Speak("opening desktop")
        winshell.desktop(common=True)
    elif "wikipedia" in text:
        r2 = sr.Recognizer()
        with sr.Microphone() as source:
            speak.Speak("What do you want to look up on wikipedia")
            audio2 = r2.listen(source)
        question = ''
        try:
            question = r2.recognize_google(audio2)
            print "Device thinks you said, " + question
            ans = wikipedia.summary(question)
            speak.Speak(ans)
            print ans
        except sr.UnknownValueError:
            print "Device could not understand what you said"
        except sr.RequestError as e:
            print "Device could not receive request from user {0}".format(e)
    elif "lock computer" in text:
        ctypes.windll.user32.LockWorkStation()




data = initialize()
perform(data)
root.mainloop() 


