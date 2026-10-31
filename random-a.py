import random
import math
a=[]
for i in range(1,11):
    x= random.randrange(1,11)
    y= random.randrange(1,11)
    a.append([x,y])
distance=[]
for i in range(0,9):
    distance.append(math.sqrt((a[i+1][0]-a[i][0])**2 + (a[i+1][1]-a[i][1])**2))
print(distance)