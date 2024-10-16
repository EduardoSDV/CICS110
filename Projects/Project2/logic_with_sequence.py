# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

from logic import xor ,nand, iff ,implies

def nand_of_tuple(a):
    _nand = nand(a[0], a[1])
    return _nand




print(nand_of_tuple((False, True)))


def implies_in_both_directions(a):
    a[0] , a[1] = implies(a[0],a[1]) ,implies(a[1], a[0])

    return a
print('implies',implies_in_both_directions([True, False]))

def iff_with_result(a):
    new_index = a.append(iff(a[0],a[1]))
    return a

print(iff_with_result([False, True]))


def xor_with_result_in_between(a):
    new_index = (xor(a[0], a[1]))
    a.insert(1 , new_index)
    return a

print(xor_with_result_in_between([True,False]))