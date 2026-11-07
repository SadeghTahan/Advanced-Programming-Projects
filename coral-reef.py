import turtle as t
import random
t.speed(0)
t.hideturtle()
t.tracer(0)
t.pu()
rules = [(40, (.31, -.53, .89), (-.46, -.29, 1.04)),
        (15, (.31, -.08, .22), (.15,  -.45, .34)),
        (45, (0,   .55,  .01), (.69,  -.20, .38)),]
n = 30000
S = 600
x,y = 0, 0
probability = [r[0] for r in rules]

for _, (a, b, c), (d, e, f) in random.choices(rules, probability, k=n):
    x, y = a*x + b*y + c, d*x + e*y + f
    t.goto((x - 0.5) * S, (y - 0.5) * S)
    t.dot(2, 'purple')
t.update()
t.done()