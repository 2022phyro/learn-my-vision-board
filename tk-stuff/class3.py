from tkinter import *
from tkinter import ttk
  
# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )
  
# Change the label text
def show():
    label.config( text = clicked.get() )

options = [
    'Lundi',
    'Mardi',
    'Mecredi',
    'Jeudi',
    'Vendredi',
    'Samedi',
    'Dimanche'
]

clicked = StringVar()
clicked.set('Lundi')
drop = ttk.OptionMenu(root, clicked, *options)
drop.pack()

btn = ttk.Button(root, text='Click Me', command=show)
btn.pack()

label = ttk.Label(root, textvariable=clicked)
label.pack()
root.mainloop()
