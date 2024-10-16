# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

def nand(a, b):
    if a == True and b == True:
        return False
    else:
        return True

print(nand(True, False))

def implies(a , b):
    if a == True and b == True:
        return True
    elif a == False and b == True:
        return True
    elif a == False and b == False:
        return True
    else:
        return False


def iff(a, b):
    if  a == b:
        return True
    else:
        return False

def xor(a, b):
    if a == b :
        return False
    else:
        return True

