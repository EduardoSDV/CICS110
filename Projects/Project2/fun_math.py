# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

import math as math

def cullen(n):
    cullen_number =  (n*2**n) + 1
    return cullen_number

print(cullen(1))

def woodall(n):
    woodall_number = (n*2**n) -1
    return woodall_number

print(woodall(5))

def fermat(n):
    fermat_number = (2**2**n) + 1
    return fermat_number

print(fermat(5))

def divides_evenly(dividend, divisor):
    if (dividend % divisor) == 0:
        return True
    else:
        return False

print(divides_evenly(4,2))


def cone_volume(r, h):
    return  math.pi * (r**2) * (h/3)

print(cone_volume(2,3))
