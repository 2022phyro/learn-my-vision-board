from tkinter import *
from tkinter import ttk
import maths
import os
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
root = Tk()

#Configure root settings and favicons
# root.geometry('700x500')
current_dir = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(current_dir, "favicon/calc-32.ico")
tsk_path = os.path.join(current_dir, "favicon", "calc-96.png")
img = PhotoImage(file=tsk_path)
root.wm_iconphoto(True, img)
root.iconbitmap(icon_path)
root.title('MyCalc')
root.resizable(False, False)
#configure styles
input_style = ttk.Style()
input_style.theme_use('clam')
input_style.configure(
    'Input.TButton',
    font=('Comic Sans MS', 15),
    foreground='#2c2c29',
    background='#e9de8b',
    borderwidth=5,
    bordercolor='grey',
    # padding=15,
    width=5,
    relief='raised',
    height=16
)
fn_style = ttk.Style()
fn_style.map(
    'Function.TButton',
    background=[("active", "gray"),
                ('pressed', 'red')],
)
fn_style.configure(
    'Function.TButton',
    font=('Comic Sans MS', 15),
    foreground='whitesmoke',
    background='#af9f24',
    borderwidth=5,
    bordercolor='grey',
    # padding=15,
    width=5,
    relief='raised',
    height=16
)
at_style = ttk.Style()
at_style.configure(
    'Arithmetic.TButton',
    font=('Comic Sans MS', 15),
    foreground='red',
    background='#ebd937',
    borderwidth=5,
    bordercolor='grey',
    # padding=15,
    width=5,
    relief='raised',
    height=16
)
entry_style = ttk.Style()
entry_style.configure(
    'Custom.TEntry',
    fieldbackground='#9beaf8ef',  # Change the background color here
    bordercolor='#9beaf8ef',         # Change the border color here
    borderwidth=0,
    font=('Constantia', 18)
)
s_style = ttk.Style()
s_style.configure(
    'Success.TEntry',
    foreground="green",
    fieldbackground='#9beaf8ef',  # Change the background color here
    bordercolor='#9beaf8ef',         # Change the border color here
    borderwidth=0,
)
f_style = ttk.Style()
f_style.configure(
    'Error.TEntry',
    foreground="red",
    fieldbackground='#9beaf8ef',  # Change the background color here
    bordercolor='#9beaf8ef',         # Change the border color here
    borderwidth=0,
    font=('Constantia', 18)
)



def display(text, entry: ttk.Entry):
    entry.insert('end', text)
def Ce(entry: ttk.Entry, x=False):
    if not x:
        entry.delete(len(entry.get()) - 1, 'end')
        return
    entry.delete(0, 'end')

def pressEqualto(root, resvar: StringVar, convar: StringVar, entry:ttk.Entry):
    global ans
    stat = False
    curr = resvar.get()
    result = maths.parse(curr, ans)
    if result != "" and result is None:
        entry.config(style='Error.TEntry')
    elif result != "":
        resvar.set(f'{result}')
        entry.config(style='Success.TEntry')
        stat = True
        val = curr.replace('Ans', f'{ans}')
        ans = result
        convar.set(f"{val}")
    def reset_style(event=None, stat = stat, con = convar):
        entry.config(style='Custom.TEntry')
        if stat:
            con.set(f"{val} = {result}")

    # Bind the reset_style function to handle keypress and left-click events
    root.bind("<KeyPress>", reset_style)
    root.bind("<Button-1>", reset_style)
    
def i_button(parent, view, text, row, col, style, entry):
    btn = ttk.Button(parent, style=style, text=view, command=lambda: display(text, entry))
    btn.grid(row=row, column=col, sticky='nsew')
    return btn
def l_button(parent, view, row, col, style, cmd, *args):
    btn = ttk.Button(parent, style=style, text=view, command=lambda: cmd(*args))
    btn.grid(row=row, column=col, sticky='nsew')
    return btn

def input_buttons(parent, style, entry):
    no9 = i_button(parent, '9', '9', 1, 1, style, entry)
    no8 = i_button(parent, '8', '8', 1, 2, style, entry)
    no7 = i_button(parent, '7', '7', 1, 3, style, entry)
    no6 = i_button(parent, '6', '6', 2, 1, style, entry)
    no5 = i_button(parent, '5', '5', 2, 2, style, entry)
    no4 = i_button(parent, '4', '4', 2, 3, style, entry)
    no3 = i_button(parent, '3', '3', 3, 1, style, entry)
    no2 = i_button(parent, '2', '2', 3, 2, style, entry)
    no1 = i_button(parent, '1', '1', 3, 3, style, entry)
    zero = i_button(parent, '0', '0', 4, 2, style, entry)
    dot = i_button(parent, '.', '.', 4, 1, style, entry)
    bright = i_button(parent, '(', '(', 4, 3, style, entry)
    bleft = i_button(parent, ')', ')', 4, 4, style, entry)
    _pi = i_button(parent, 'π', 'π', 3, 4, style, entry)


def fn_buttons(parent, style, entry):
    sin1 = i_button(parent, 'sin-1', 'sin-1(', 0, 0, style, entry)
    cos1 = i_button(parent, 'cos-1', 'cos-1(', 1, 0, style, entry)
    tan1 = i_button(parent, 'tan-1', 'tan-1(', 2, 0, style, entry)
    log1 = i_button(parent, 'log-1', 'log-1(', 3, 0, style, entry)
    log = i_button(parent, 'log', 'log(', 4, 0, style, entry)
    _sin = i_button(parent, 'sin', 'sin(', 0, 1, style, entry)
    _cos = i_button(parent, 'cos', 'cos(', 0, 2, style, entry)
    _tan = i_button(parent, 'tan', 'tan(', 0, 3, style, entry)
    _mod = i_button(parent, 'mod', ' mod ', 0, 4, style, entry)
    rt = i_button(parent, '√', '√(', 1, 4, style, entry)
    pow = i_button(parent, '^', '^(', 2, 4, style, entry)
def at_buttons(parent, style, entry):
    row6 = ["+", "-", 'x', "÷"]
    add = i_button(parent, '+',  ' + ', 1, 5, style, entry)
    sub = i_button(parent, '-',  ' - ', 2, 5, style, entry)
    mul = i_button(parent, 'x',  ' x ', 3, 5, style, entry)
    div = i_button(parent, '÷',  ' ÷ ', 4, 5, style, entry)
    _ans = i_button(parent, 'Ans',  ' Ans ', 4, 6, style, entry)

def res_buttons(parent, style):
    res = ['CE', 'C', '=']
    ce = l_button(parent, 'CE',  0, 5, style, Ce, entry, False)
    clear = l_button(parent, 'C',  0, 6, style, Ce, entry, True)
    equal_to = l_button(parent, '=',  1, 5, style, pressEqualto, root, resvar, convar, entry)
    equal_to.grid(row=1, column=6, sticky='nsew', rowspan=3)
    
    
#create Main frame

ans = 0
content = ttk.Frame()
title = ttk.Label(content)
convar = StringVar()
resvar= StringVar()
result = ttk.Label(content, padding=10, textvariable=convar)
entry = ttk.Entry(content, font=('Constantia', 24),
                  style='Custom.TEntry', justify='right', textvariable=resvar)
CFrame = ttk.Frame(content)
input_buttons(CFrame, 'Input.TButton', entry)
fn_buttons(CFrame, 'Function.TButton', entry)
at_buttons(CFrame, 'Arithmetic.TButton', entry)
res_buttons(CFrame, 'Arithmetic.TButton')

# config options
content.configure(width=700, height=600, relief='raised', borderwidth=5, padding=50)
title.configure(text="MyCalc", font=('Monotype Corsiva', 28))
result.configure(font=('Constantia', 14), anchor='e', padding=(0, 0, 0, 10), foreground='#888')
CFrame.configure(padding=(0, 20, 0, 0))
#grid Settings and positioning for the widgets
title.grid(column=0, row=0, sticky='nw')
content.grid(column=0, row=0, sticky='nsew')
result.grid(column=0, row=1, sticky='nsew')
entry.grid(column=0, row=2, sticky='nsew')
CFrame.grid(column=0, row=3, sticky='nsew')

root.columnconfigure(0)
root.rowconfigure(0)
content.columnconfigure(0)
content.rowconfigure(7)
root.mainloop()

"""To do: update the function so that when buttons are clicked,
the entry widgets are updated at once"""
