# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

import random as random
from math import floor
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


def password_generator(n):
    base_count = n // 4
    list_count = [base_count] * 4
    for i in range(n%4):
        list_count[i] += 1

    random_selection = random.sample(list(ascii_uppercase), list_count[0])
    random_selection.extend(random.sample(list(ascii_lowercase), list_count[1]))
    random_selection.extend(random.sample(list(digits), list_count[2]))
    random_selection.extend(random.sample(list(punctuation), list_count[3]))
    password = ''.join(map(str, random_selection))
    return password


print(password_generator(1))









