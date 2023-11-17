from tkinter import *
from tkinter import ttk


root = Tk()
root.title("An intro into Canvas")
H = ttk.Scrollbar(root, orient='horizontal')
V = ttk.Scrollbar(root, orient='vertical')
C = Canvas(root, background='white', scrollregion=(0, 0, 200, 2000),
           yscrollcommand=V.set, xscrollcommand=H.set)
H['command'] = C.xview
V['command'] = C.yview
C.grid(row=0, column=0, sticky='NSWE')
H.grid(column=0, row=1, sticky='we')
V.grid(column=1, row=0, sticky='ns')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

r = C.create_rectangle(0, 0, 100, 70, fil='blue')
def move(event):
    if event.keysym == 'm':
        C.move(r, 10, 0)
    elif event.keysym == 'j':
        C.move(r, 0, 10)
C.bind('<KeyPress>', move)
C.focus_set()
root.mainloop()
