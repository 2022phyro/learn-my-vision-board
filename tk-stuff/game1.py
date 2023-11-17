from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import sys
import random
root = Tk()
root.title("Our first tkinter game")
game_width = 1500
game_height = 700
s_movement_factor = 7
root_delay = 10
animation_delay = 0.01
bullet_tag = 'bullet'
alien_tag = 'alien'
bullet_count = 0
alien_count = 0
alien_movement_factor = 1
life = 3
lives = []
root.geometry(f'{game_width}x{game_height}')
C = Canvas(root, width=game_width, height=game_height, bg='black')
C.pack()
v = 30
for i in range(1, life + 1):
    x2 = v + 10
    lives.append(C.create_rectangle(v, 25, x2, 50, fill='green', tags='life'))
    v = x2 + 15
print(lives)
svar = StringVar()
svar.initialize('0')
score = ttk.Label(C, textvariable=svar, font=("Algerian", 30), foreground='red', background='black')
C.create_window(1000, 25, anchor='nw', window=score)
def load(image):
    img = Image.open(image)
    result = ImageTk.PhotoImage(img)
    return result
star = load('starship.png')
s_id = C.create_image(game_width / 2, game_height, anchor='s', image=star)
alien = load('alien.png') 

def move_left(event):
    x1, y1 = C.coords(s_id)
    if  x1 -s_movement_factor < 0:
        return
    else:
        C.move(s_id,  0 - s_movement_factor, 0)

def rando():
    x = random.uniform(0, game_width)
    y = random.uniform(75, 250)
    return x, y

def move_right(event):
    x1, y1 = C.coords(s_id)
    if  x1 + s_movement_factor > game_width:
        return
    else:
        C.move(s_id,  0 + s_movement_factor, 0)
print(lives)
def move_up(event):
    x1, y1 = C.coords(s_id)
    if y1 - s_movement_factor < 0:
        return
    else:
        C.move(s_id, 0 , 0 - s_movement_factor)

def move_down(event):
    x1, y1 = C.coords(s_id)
    if y1 + s_movement_factor > game_height:
        return
    else:
        C.move(s_id, 0 , 0 + s_movement_factor)

def new_bullet(event):
    global bullet_count
    if bullet_count >= 10:
        return
    x, y = C.coords(s_id)
    C.create_rectangle(x - 2, y - 90, x + 1, y - 75, fill='red', tags=bullet_tag)
    bullet_count += 1

def move_bullet():
    C.move(bullet_tag, 0, -1)
    root.after(root_delay, move_bullet)

def collision():
    global bullet_count, alien_count, life
        # Check for collisions with aliens
    for a in C.find_withtag(alien_tag):
        x, y = C.coords(a)
        for bullet in C.find_withtag(bullet_tag):
            x1, y1, x2, y2 = C.coords(bullet)
            if y1 <= 0:
                C.delete(bullet)
                bullet_count -= 1
            if x > x1 and x <= x2 and y >= y1:
                C.delete(a)
                C.delete(bullet)
                bullet_count -= 1
                alien_count -= 1
                scy = int(svar.get())
                svar.set(f'{scy + 7}')
        if y >= game_height:
            life -= 1
            C.delete(lives.pop())
            if life <= 0:
                C.create_text(game_width / 2, game_height / 2, text='Game Over', font=("Parchment", 70), fill='red', anchor='center')
                    
                
    root.after(root_delay, collision)

def aliens():
    global alien_count
    if alien_count <= 10:
        C.create_image(*rando(), anchor='s', image=alien, tags=alien_tag)
        alien_count += 1
    root.after(root_delay, aliens)

def move_aliens():
    global alien_movement_factor
    C.move(alien_tag, alien_movement_factor, 0)
    for a in C.find_withtag(alien_tag):
        x, y = C.coords(a)
        if x >= game_width or x <= 0:
            alien_movement_factor = 0 - alien_movement_factor
            C.move(alien_tag, 0, 20)
            break
    root.after(root_delay, move_aliens)

def all_bindings():
    C.focus_set()
    C.bind('<Left>', move_left)
    C.bind('<Right>', move_right)
    C.bind('<space>', new_bullet)
    C.bind('<Up>', move_up)
    C.bind('<Down>', move_down)

all_bindings()
root.after(root_delay, move_bullet)
root.after(root_delay, aliens)
root.after(root_delay, move_aliens)
root.after(root_delay, collision)
root.mainloop()
