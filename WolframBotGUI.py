from Tkinter import *
import wolframalpha
import ttk

app_id='PA237Q-XA42375UEE'
client = wolframalpha.Client(app_id)


def Call(*args):
    #query = feet.get()
    #res = client.query(str(query))
    
    try:
        query = feet.get()
        res = client.query(str(query))
        meter = next(res.results).text
    except:
        meter ='I don\'t understand, please try again'
    
    
    res = Label(root, text = meter).grid(column=2, row=2, sticky=W)
    #res.pack()
    
    
root = Tk()
root.title("Math Solver")
root.geometry('300x100+650+300')

feet = StringVar()
meters = StringVar()
ttk.Label(text="Enter your question here:   ").grid(row=0, sticky=W)
feet_entry = ttk.Entry(textvariable=feet)
feet_entry.grid(column=2, row=0, sticky= W)


ttk.Button(text="Calculate", command=Call).grid(column=2, row=8, sticky=W)

ttk.Label(text="Your Answer Is:   ").grid(row=2, sticky=E)



feet_entry.focus()
root.bind('<Return>', Call)


root.mainloop() 

