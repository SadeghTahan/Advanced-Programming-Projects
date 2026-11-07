import turtle as t
import random
import math as m
colors = ['red','green','blue','orange','purple','cyan']

t.pu()
t.goto(-200,-150)
t.pd()

for i in range(3):
    t.color(colors[i])
    t.fd(400)
    t.lt(120)
def circle():
    t.fd(100)
    t.lt(90)
    t.pd()
    t.circle(100)
    t.pu()
    t.rt(90)
    t.bk(100)
for r in range(3):
    t.pu()
    t.color(colors[r+3])
    t.fd(400)
    t.lt(120)
    circle()
t.done()