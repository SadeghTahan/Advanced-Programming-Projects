import random
a = [random.randint(0,20) for i in range(0,5)]
for v in a:
    print('array a = ',v)
maximum = max(a)
print('maximum = ',maximum)
average = float(sum(a)) / len(a)
print('average = ',average)
b = a[:]
print('array b = ',b)
a = a[::-1]
print('reversed array a = ',a)