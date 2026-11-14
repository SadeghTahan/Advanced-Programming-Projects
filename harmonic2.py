import sys
def harmonic(n , r=1):
    total = .0
    for i in range(1 , n+1):
        total += 1.0 / (i**r)
    return total
n = int(sys.argv[1])
r = int(sys.argv[2])
print(harmonic(n , r))