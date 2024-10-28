# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477
import random

def get_guess():
    x = str(input('Input your guess: '))
    return x.upper()

def print_word(_string):
    print( ' '.join(_string))

def exact_match_compare(x , y):
    t_arr = []
    for el, el2 in zip(str(y), str(x)):
        if el != el2:
            t_arr.append( '🔴')
        else:
            t_arr.append( '🟢' )

    return ''.join(t_arr)

def one_turn(x):
    guess = get_guess()
    match_compare = exact_match_compare(x,guess)
    print(' '.join(guess))
    print(match_compare)
    if x == guess:
        print('Congratulations!')
        exit()


def make_solution():
    _list = ["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]
    return random.choice(_list)

print(get_guess())
print(print_word(get_guess()))
print(exact_match_compare('HELO','HELP'))
print(one_turn('HELLO'))


