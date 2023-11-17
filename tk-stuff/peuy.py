from tkinter import *
import time
root = Tk()

C = Canvas(root, width=1000, height=600, background='white')
C.pack()
root.geometry('1000x600')
root.title("Walking animation")
walk_images = [
    PhotoImage(file=f'images/character_malePerson_walk{i}.png')
    for i in range(8)
]
w_sequence = [
    C.create_image(50, 500, anchor='s', image=x, state='hidden')
    for x in walk_images
]
def swap(index):
    for i in range(8):
        x = w_sequence[i]
        if i == index:
            C.itemconfig(x, state='normal')
        else:
            C.itemconfig(x, state='hidden')
        C.move(x, 5, 0)
def walk():
    for i in range(7):
        swap(i)
        root.update()
        time.sleep(0.08)
    swap(7)
    root.update()
    # time.sleep(0.08)
    root.after(80, walk)
walk()
root.mainloop()
