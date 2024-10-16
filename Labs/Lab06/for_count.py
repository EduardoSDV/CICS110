# Author   : Eduardo Suarez del Valle, Shehroz Asim
# Email    : esuarez@umass.edu, sasim@umass.edu
# Spire ID : 34750477 , 34748987

def count_strings(string_list, n):
    count = 0
    for string in string_list:
        if len(string) >= n:
            count += 1
    return count



print(count_strings(['a'],0))



