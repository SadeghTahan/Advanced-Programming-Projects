coefficients = []
coefficients.append([1])
for n in range(1,9):
    row = []
    for k in range(n+1):
        if k==0 or k==n:
            row.append(1)
        else:
            row.append(coefficients[n-1][k-1] + coefficients[n-1][k])
    coefficients.append(row)
for j in coefficients:
    print(j)
unities = []
unities.append(['1'])
for power in range(1,9):
    unity = []
    for coefficient in range(power+1):
        if coefficient == 0:
            unity.append('x^' + str(power))
        elif coefficient == power:
            unity.append('y^' + str(power))
        else:
            unity.append(str(coefficients[power][coefficient]) + 'x^' + str(power-coefficient) + 'y^' + str(coefficient))
    unities.append(unity)
for r in unities:
    print(' + '.join(r))