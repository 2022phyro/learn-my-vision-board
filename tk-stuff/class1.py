from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Foor order Delivery")
# root.resizable(False, False)
root.geometry('600x600')
content = ttk.Frame(root, padding=20)
content.pack(anchor='w')
title = ttk.Label(content, font=('Gothic', 24), justify='center',
                  text='Food order delivery')
title.pack(anchor='center', ipady=10)
frame1 = ttk.Frame(content)
frame1.pack(anchor='w', ipady=7)
frame2 = ttk.Frame(content)
frame2.pack(anchor='w', ipady=7)
ttk.Label(frame1, text="What would you like for takeout?", font=('Georgia', 18)).pack(anchor='w')
ttk.Label(frame2, text="How would you like to pay?", font=('Georgia', 18)).pack(anchor='w')
check_boxes = [BooleanVar() for _ in range(4)]
options = ['Fufu and Egusi', 'Jollof Rice and Chicken', 'Abacha', 'Nkwobi']
for var, text in zip(check_boxes, options):
    ttk.Checkbutton(frame1, text=text, variable=var).pack(anchor='w')
radiovar = StringVar()
choices = ['Card', 'Cheque', 'Bank Order', 'Postal Order', 'Barter']
for text in choices:
    ttk.Radiobutton(frame2, text=text, variable=radiovar, value=text,).pack(anchor='w')
def take_order():
    for var, text in zip(check_boxes, options):
        if var.get() is True:
            print(text)
    print(radiovar.get())
            
btn = ttk.Button(content, command=take_order, text='submit')
btn.pack()
    

root.mainloop()
