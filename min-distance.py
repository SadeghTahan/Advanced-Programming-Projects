import random
import math
points=[]
for point in range(1,11):
    x=random.randint(1,10)
    y=random.randint(1,10)
    points.append([x,y])
print(points)
distance=[]
for i in range(0,9):
    distance.append(math.sqrt((points[i+1][0]-points[i][0])**2 + (points[i+1][1]-points[i][1])**2))
print(distance)
minimum = min(distance)
print("The minimum distance is: ", minimum)