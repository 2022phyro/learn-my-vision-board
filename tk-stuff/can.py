from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from PIL import Image, ImageTk

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
menu = C.create_rectangle(0, 0, 1000, 70, fill='grey')

def savePos(event):
    global lastx, lasty
    lastx, lasty = C.canvasx(event.x), C.canvasy(event.y)

color='black'    
def addLine(event):
    global menu
    x, y = C.canvasx(event.x), C.canvasy(event.y)
    if x > 100 and y > 70:
        C.create_line(lastx, lasty, x, y, fill=color)
        savePos(event)
def changeC(col = None):
    global color, lastcolor
    lastcolor = color
    if col:
        color = col
        return
    colors = askcolor(title='Pick a color')
    if colors:
        color = colors[1]
        lastcolor = color
    else:
        color = lastcolor



id = C.create_rectangle(20, 20, 40, 40, fill='red', activeoutline='grey', activewidth=3)
C.tag_bind(id, '<Button-1>', lambda x: changeC('red'))
btn = Button(text="More colors", command = changeC)
C.create_window(20, 50, anchor="nw", window=btn)
C.bind("<Button-1>", savePos)
C.bind("<B1-Motion>", addLine)



root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
