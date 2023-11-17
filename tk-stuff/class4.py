from tkinter import *
from tkinter import ttk

# Press a buton in keyboard
def PressAnyKey(label):
   value = label.char
   l.config(text= f"Pressed {value}")
base = Tk()
base.geometry('300x150')
base.bind('<Key>', lambda i : PressAnyKey(i))
l = ttk.Label(base, text="Pressed Nothing")
l.pack()
mainloop()
