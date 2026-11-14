from math import sqrt as s
print('please enter districs: ')
def hypot(a , b):
    return s(a*a +b*b)
a = float(input())
b = float(input())
print(hypot(a , b))