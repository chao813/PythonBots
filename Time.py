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

root.mainloop()