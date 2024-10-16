# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477
import math
n = int(input())

i = 1
sum1 = 0
while i <= n:

    sum1 += 1 / i**2
    i += 1

print(sum1)
print(math.sqrt(6*sum1))