import turtle as t
from random import random
t.speed(0)
t.tracer(0)
colors = ['red','green','blue','yellow','orange','purple','black']
for i in range(100):
    t.color(colors[i %len(colors)])
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
t.update()
t.done()