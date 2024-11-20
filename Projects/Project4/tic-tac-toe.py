# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477
def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)

def make_empty_board(n):
  board = []
  for _ in range(n):
    row = []
    for _ in range(n):
      row.append(' ')
    board.append(row)
  return board

def get_location(n, board):
  while True:
    row_input = input(f"Please enter a row index between 0 and {n - 1}: ")
    col_input = input(f"Please enter a column index between 0 and {n - 1}: ")

    if not (row_input.isdigit() and col_input.isdigit()):
      print(f"({row_input}, {col_input}) is not a legal input!")
      continue

    row, col = int(row_input), int(col_input)

    if not (0 <= row < n and 0 <= col < n):
      print(f"({row}, {col}) is not a legal space!")
    elif board[row][col] != ' ':
      print(f"({row}, {col}) is not an available space!")
    else:
      return row, col

def row_win(n, board, player):
  for row in board:
    all_match = True
    for cell in row:
      if cell != player:
        all_match = False
        break
    if all_match:
      return True
  return False


def col_win(n, board, player):
  for col in range(n):
    all_match = True
    for row in board:
      if row[col] != player:
        all_match = False
        break
    if all_match:
      return True
  return False


def diag_win(n, board, player):
  for i in range(n):
    if board[i][i] != player:
      return False
  return True


def anti_diag_win(n, board, player):
  for i in range(n):
    if board[i][n - 1 - i] != player:
      return False
  return True

def has_won(n, board, player):
  return row_win(n, board, player) or col_win(n, board, player) or diag_win(n, board, player) or anti_diag_win(n,
                                                                                                               board,
                                                                                                               player)
def print_board(n, board):
  for row in board:
    print("+---" * n + "+")
    print("| " + " | ".join(row) + " |")
  print("+---" * n + "+")

def play_game(n):
  board = make_empty_board(n)
  print(f"*** Welcome to {n} by {n} Tic-Tac-Toe ***")
  print_board(n, board)

  player = "X"
  total_moves = 0
  max_moves = n * n

  while total_moves < max_moves:
    print(f"\n* {player}'s turn *")
    row, col = get_location(n, board)
    board[row][col] = player
    print_board(n, board)

    if has_won(n, board, player):
      print(f"{player} wins!")
      return

    player = "O" if player == "X" else "X"
    total_moves += 1

  print("Tie!")





