from Tkinter import *
import winshell


def empty():
    recycle_bin = winshell.recycle_bin()
    recycle_bin.empty(confirm=False, show_progress=False, sound=True)

def desktop():
    winshell.desktop()
    winshell.my_documents()
    
    
root = Tk()
root.title("Basic Winshell Operations")
root.geometry('350x100+650+300')
#calculate button
button = Button(text="Empty Recycle Bin", command=empty)
button['bg'] ='light blue'
button.grid(column=2, row=8, sticky=W)

#clear button
desktop_button = Button(text = "Open Desktop Folder", command =desktop)
desktop_button.grid(column = 0, row=8, sticky = E)
desktop_button['fg'] = 'black'
desktop_button['bg'] = 'light blue'






for child in root.winfo_children():
    child.grid_configure(padx=3, pady=3)


root.mainloop() 

