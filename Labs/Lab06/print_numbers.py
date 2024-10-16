# Author   : Eduardo Suarez del Valle, Shehroz Asim
# Email    : esuarez@umass.edu, sasim@umass.edu
# Spire ID : 34750477 , 34748987


n = int(input())
_list = list(range(1, n + 1))

while len(_list) > 0:

    print(" ".join(str(el) for el in _list))
    _list.pop()


