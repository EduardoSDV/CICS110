# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

import math as math


def discriminant(a, b, c):
    d = b**2-(4*a*c)
    return d
print(discriminant(1, 4, 3))

def has_real_root(a , b, c):
    if b**2-(4*a*c) >= 0 :
        return True
    else:
        return False

print(has_real_root(1,2,3))

def get_real_roots(a,b,c):
    x1 = ((-b)+ math.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = ((-b)- math.sqrt(b**2-(4*a*c)))/(2*a)
    return x1, x2

print(get_real_roots(1,4,2))
