import sys
binary=str(sys.argv[1])
power=0
decimal=0
for digit in reversed(binary):
    decimal= int(digit)*(2**power) + decimal
    power += 1 
print(decimal)