from tkinter import *
import time
root = Tk()

C = Canvas(root, width=1305, height=722, background='white')
C.pack()
root.geometry('1305x722')
root.title("Walking animation")
bg = PhotoImage(file='images/bbound.png')
C.create_image(0, 0, anchor='nw', image=bg)
a_seq = [ PhotoImage(file=f'images/character_femalePerson_attack{i}.png') for i in range(3) ]
r_seq = [ PhotoImage(file=f'images/character_femalePerson_run{i}.png') for i in range(3)]
c_seq = [ PhotoImage(file=f'images/character_femalePerson_climb{i}.png') for i in range(2) ]

r_images = [ C.create_image(50, 665, anchor='s', image=img, state='hidden') for img in r_seq]
c_images = [ C.create_image(50, 665, anchor='s', image=img, state='hidden') for img in c_seq]

def swap(idx, ls, x, y):
    for i in range(len(ls)):
        if i == idx:
            C.itemconfig(ls[i], state='normal')
        else:
            C.itemconfig(ls[i], state='hidden')
        C.move(ls[i], x, y)

def run(event):
    while event:
        for i in range(2):
            swap(i, r_images, 10, 0)
            root.update()
            time.sleep(0.1)
        swap(2, r_images, 10, 0)
        root.update()
        time.sleep(0.2)
    # root.after(100, run)

def climb(event):
    while event:
        swap(0, c_images, 0, -5)
        root.update()
        time.sleep(0.2)
        swap(1, c_images, 0, -5)
        root.update()
        time.sleep(0.2)

    # root.after(200, climb)


root.bind('<Up>', climb)
root.bind('<Right>', run)
# run()
root.mainloop()
