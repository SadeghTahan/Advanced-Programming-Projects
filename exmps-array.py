import random
a = []
for i in range(0,5):
    a += [random.randint(0,20)]
for v in a:
    print('array a =' , v)
maximum = a[0]
for v in a[1:]:
    if(v > maximum):
        maximum = v
print('maximum =' , maximum)
total = 0.0
for v in a:
    total += v
average = total / len(a)
print('average =' , average)
b = []
for v in a:
    b += [v]
print('array copy =' , b)
n = len(a)
for i in range(n // 2):
    temp = a[i]
    a[i] = a[n-1-i]
    a[n-1-i] = temp
print('reversed array =' , a)