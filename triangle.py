import sys
import turtle as t
def draw_triangle(x0, y0, x1, y1, x2, y2):
    t.hideturtle()
    t.pu()
    t.goto(x0,y0)
    t.pd()
    t.goto(x1,y1)
    t.goto(x2,y2)
    t.goto(x0,y0)
    t.done()
x0 = float(input())
y0 = float(input())
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
draw_triangle(x0,y0,x1,y1,x2,y2)