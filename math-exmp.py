import sys
x = float(sys.argv[1])
y = float(sys.argv[2])
total=0
for n in range(0,101):
    total += 1 / (x+y)**n
print(total)