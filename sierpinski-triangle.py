import turtle as t
import random
import math as m
t.pu()
t.goto(-150,-100)
t.pd()
t.hideturtle()
t.speed(0)
t.tracer(0)
colors=['red','green','blue']
for i in range(3):
    t.color(colors[i])
    t.fd(300)
    t.lt(120)
r = [-150,-100]
g = [150,-100]
b = [0,-100 + 300 * m.sqrt(3)/2]
vertex = [r,g,b]
x = random.choice(vertex)
for n in range(25000):
    c = random.randrange(3)
    v = vertex[c]
    t.pu()
    x = [(x[0]+v[0])/2,(x[1]+v[1])/2]
    t.goto(x[0],x[1])
    t.color(colors[c])
    t.pd()
    t.dot(2)
t.done()