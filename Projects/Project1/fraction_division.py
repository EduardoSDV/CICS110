# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

dividend = int(input('What is the dividend: '))
divisor = int(input('What is the divisor: '))

quotient = dividend // divisor
remainder = dividend % divisor

print(f'{dividend}/{divisor} equals:')
print(f'\t{quotient} and {remainder}/{divisor}')
