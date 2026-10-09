import sys
import math
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
delta=b*b-4.0*a*c
root=math.sqrt(delta)
print((-b+root)/(2*a))
print((-b-root)/(2*a))