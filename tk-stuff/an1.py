from tkinter import *
import time
an_w = 800
an_h = 600
xan_start = 50
yan_start = 50
b_radius = 30
m_factor = 5
refresh = 0.01
def window():
    root = Tk()
    root.title = ("Bouncing ball")
    root.geometry = (f"{an_w}x{an_h}")
    root.resizable = (False, False)
    return root

def canvas(root):
    C = Canvas(root, background='black', width=an_w, height=an_h)
    C.pack(fill="both", expand=True)
    return C

def animate(root, canvas, xincr, yincr):
    ball = canvas.create_oval(
        xan_start - b_radius, yan_start - b_radius,
        xan_start + b_radius, yan_start + b_radius,
        fill='blue', outline='white', width=30
    )
    while True:
        canvas.move(ball, xincr, yincr)
        root.update()
        time.sleep(refresh)
        ball_pos = canvas.coords(ball)
        x1, y1, x2, y2, =  ball_pos
        if x1 < abs(xincr) or x2 > an_w - abs(xincr):
            xincr =  -xincr
        if y1 < abs(yincr) or y2 > an_h - abs(yincr):
            yincr = -yincr

root = window()
a_canvas = canvas(root)
animate(root, a_canvas, m_factor, m_factor)
