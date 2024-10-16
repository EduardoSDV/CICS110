# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

def is_edge_sorted(a, b , c):
    if (a <= b) and (b <= c):
        return True
    else:
        return False


def classify_by_edges(a, b ,c):
    _lengths = {a, b ,c}
    if (a+b) <= c:
        return 'invalid'
    elif len(_lengths) == 1:
        return 'equilateral'
    elif len(_lengths) == 2:
        return 'isosceles'
    else:
        return 'scalene'


def classify_by_angles(a, b, c):
    if (a+b) <= c:
        return 'invalid'
    elif c**2 == a**2 + b**2:
        return 'right'
    elif  c**2 >= a**2 + b**2:
        return 'obtuse'
    else:
        return 'acute'