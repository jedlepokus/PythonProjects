import numpy as np
# ax^2 + bx + c = 0

#print(np.sqrt(9))
#print(np.pow(2, 3))
#print(5**2)
#print(9**(1/2))


def kvadraticka(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return []
    elif D == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + D**(1/2)) / (2 * a)
        x2 = (-b - D**(1/2)) / (2 * a)
        return [x1, x2]

print(kvadraticka(1,2,1))
print(kvadraticka(1,3,1))
print(kvadraticka(1,1,1))
