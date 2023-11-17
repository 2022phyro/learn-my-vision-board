from tkinter import *
import time
import sys
import random
root = Tk()
root.title("Our second tkinter game")
game_width = 1000
game_height = 700
animation_delay = 0.1
root.geometry(f'{game_width}x{game_height}')
C = Canvas(root, width=game_width, height=game_height, bg='white')
C.pack()
run_sequence = [
    PhotoImage(file=f'images/character_zombie_run{i}.png')
    for i in range(3)
]
run_sequence.append(PhotoImage(file='images/character_zombie_jump.png'))
run_sequence.append(PhotoImage(file='images/character_zombie_slide.png'))
run_images = [
    C.create_image(100, 500, anchor='s', tags='run', image=run_sequence[i], state='hidden')
    for i in range(5)
]

def move():
    for pic in run_images:
        C.move(pic, 10, 0)

def swap(index):
    for i in range(5):
        if i == index:
            C.itemconfig([run_images[i]], state='normal')
        else:
            C.itemconfig([run_images[i]], state='hidden')

def run():
    swap(0)
    root.update()
    move()
    time.sleep(animation_delay)
    swap(1)
    root.update()
    move()
    time.sleep(animation_delay)
    swap(2)
    root.update()
    move()
    root.after(int(animation_delay * 1000), run)

def jump(event):
    if event.keysym == 'space':
        swap(3)
        C.move(run_images[3], 0, -150)
        root.update()
        time.sleep(animation_delay + 0.1)
        swap(3)
        C.move(run_images[3], 0, 150)
        root.update()
        time.sleep(animation_delay + 0.1)

C.bind('<KeyRelease>', jump)
C.focus_set()
run()
root.mainloop()
