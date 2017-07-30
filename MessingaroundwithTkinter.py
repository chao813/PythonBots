from Tkinter import *
import ttk
import wolframalpha



"""app_id='PA237Q-XA42375UEE'
query = raw_input('Enter your math question: ')

client = wolframalpha.Client(app_id)


def calculate(*args):
    value = feet.get()
    res = client.query(str(query))
    try:
        next(res.results).text
    except:
        pass
    
root = Tk()
root.title("Enter your math question: ")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()"""

def Pressed():                          #function
    print 'buttons are cool'

root = Tk()                              #main window
button = Button(root, text = 'Press', command = Pressed)
button.pack(pady=20, padx = 20)
Pressed()
root.mainloop()