from Tkinter import *
import wolframalpha
import ttk
from PIL import ImageTk
import base64, zlib

app_id='PA237Q-XA42375UEE'
client = wolframalpha.Client(app_id)


def Call(*args):
    #query = feet.get()
    #res = client.query(str(query))
    
    
    try:
        query = feet.get()
        res = client.query(str(query))
        meters.set(next(res.results).text)
    except:
        meters.set('I don\'t understand, please try again')
    
    
    #res = Label(root, text = meters).grid(column=2, row=2, sticky=W)
    
    button['fg'] = 'black'
    button['bg'] = 'light blue'
    #button.after(2000, lambda: button.configure(background ="grey"))
    return meters
    
#clear button to empty all values
def clear_text(*args):
    meters_entry.delete(0,'end')
    feet_entry.delete(0, 'end')
    
    
root = Tk()
root.title("Math Solver")
root.geometry('350x100+650+300')

#Top right icon to transparent
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
image=ImageTk.PhotoImage(data=ICON)
root.tk.call('wm', 'iconphoto', root._w, image)  


feet = StringVar()
meters = StringVar()
ttk.Label(text="Enter your question here:   ", font = "Helvetica 10 bold").grid(row=0, sticky=W)
feet_entry = ttk.Entry(textvariable=feet)
feet_entry.grid(column=2, row=0, sticky= W)
ttk.Label(text="Your answer is:   ",font = "Helvetica 10 bold").grid(row=2, sticky=E)
meters_entry = ttk.Entry(textvariable=meters)
meters_entry.grid(column=2, row=2, sticky= W)

#calculate button
button = Button(text="Calculate", command=Call)
button['bg'] ='light blue'
button.grid(column=2, row=8, sticky=W)

#clear button
clear_button = Button(text = "Clear", command = clear_text)
clear_button.grid(column = 0, row=8, sticky = E)
clear_button['fg'] = 'black'
clear_button['bg'] = 'light blue'



feet_entry.focus()
root.bind('<Return>', Call)

for child in root.winfo_children():
    child.grid_configure(padx=3, pady=3)


root.mainloop() 

