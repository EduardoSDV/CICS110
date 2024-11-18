# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477
import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")


def print_revealed_phrase(phrase, guessed_letters):
  result = ""
  for char in phrase:
    if char.isalpha() and char not in guessed_letters:
      result += "_"
    else:
      result += char
  print(result)


def get_letter(guessed_letters):
  while True:
    user_input = input("Please enter a letter: ").upper()
    if not user_input.isalpha() or len(user_input) != 1:
      print(f'"{user_input}" is not a letter!')
    elif user_input in guessed_letters:
      print(f'"{user_input}" has already been guessed!')
    else:
      return user_input

def won(phrase, guessed_letters):
  for char in phrase:
    if char.isalpha() and char not in guessed_letters:
      return False
  return True


def play_game():
  phrase = make_phrase()
  misses = 0
  guesses = []

  print("*** Welcome to Hangman ***")
  print_gallows(misses)
  print()

  while True:
    print_revealed_phrase(phrase, guesses)
    print(f"Letters guessed: {', '.join(sorted(guesses))}")
    guess = get_letter(guesses)
    guesses.append(guess)

    if guess not in phrase:
      misses += 1
      print_gallows(misses)
      if misses == 6:
        print("Game Over!")
        print(f"Solution was: {phrase}")
        break
    else:
      if won(phrase, guesses):
        print_revealed_phrase(phrase, guesses)
        print("Congratulations!")
        break

        



