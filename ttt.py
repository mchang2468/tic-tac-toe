# Tic-Tac-Toe

# Variables and Lists
# ===================
board = [
  ["   ", "   ", "   "], 
  ["   ", "   ", "   "], 
  ["   ", "   ", "   "]
]
playing = True

# Functions
# =========
# Name: print_gameboard
# Purpose: This function nicely prints the gameboard as a 3x3 square.
# Input: gameboard (a list of lists)
# Output: returns nothing, prints out the gameboard
def print_gameboard(gameboard):
  for r in range(0,len(gameboard)):
    for c in range(0,len(gameboard[0])):
      if c != 2:
        print(gameboard[r][c], end = "|")
      else:
        print(gameboard[r][c])
        if r != 2:
          print("-----------")

# Name: check_winner
# Purpose: uses the gameboard to check whether or not a player has won. 
# Input: gameboard (a list of lists)
# Output: returns 'X' or 'O' if either player has won and returns ' ' if neither player has won.
def check_winner(gameboard):
  for r in range(0,len(gameboard)):
    if gameboard[r][0] == ' X ' and gameboard[r][1] == ' X ' and gameboard[r][2] == ' X ':
      return 'X'
    elif gameboard[r][0] == ' O ' and gameboard[r][1] == ' O ' and gameboard[r][2] == ' O ':
      return 'O'
  for c in range(0,len(gameboard)):
    if gameboard[0][c] == ' X ' and gameboard[1][c] == ' X ' and gameboard[2][c] == ' X ':
      return 'X'
    elif gameboard[0][c] == ' O ' and gameboard[1][c] == ' O ' and gameboard[2][c] == ' O ':
      return 'O'
  if gameboard[0][0] == ' X ' and gameboard[1][1] == ' X ' and gameboard[2][2] == ' X ':
    return 'X'
  elif gameboard[0][0] == ' O ' and gameboard[1][1] == ' O ' and gameboard[2][2] == ' O ':
    return 'O'
  elif gameboard[0][2] == ' X ' and gameboard[1][1] == ' X ' and gameboard[2][0] == ' X ':
    return 'X'
  elif gameboard[0][2] == ' O ' and gameboard[1][1] == ' O ' and gameboard[2][0] == ' O ':
    return 'O'
  else:
    return ' '



  
  # for r in range(0,len(gameboard)):
  #   if gameboard[r][0] == gameboard[r][1] and gameboard[r][1] == gameboard[r][2]:
  #     return gameboard [r][0]
  #   for c in range (0, len(gameboard[r])):
  #     if gameboard[0][c] == gameboard[1][c] and gameboard[1][c] == gameboard[2][c]:
  #       return gameboard [0][c]
        

# Name: check_tied
# Purpose: used to determine whether the game is tied (all 9 spaces are filled but no one has won)
# Input: gameboard (a list of lists)
# Output: returns True if there is a tie and False if there is not a tie. 
def check_tied(gameboard):
  empty_spaces = 0
  for r in range(0,len(gameboard)):
    for c in range(0,len(gameboard)):
      if gameboard[r][c] == '   ':
        empty_spaces += 1
  if empty_spaces >= 1:
    return False
  else:
    return True

# Name: make_move
# Purpose: To fill the gameboard with the current player's move. Prompts the user by their name for a row and then for a column. Then, it places their symbol in the indicated spot on the gameboard. If an illegal spot is selected, the user will be prompted to make a new selection.
# Input: gameboard (a list of lists), name (a string representing the current player's name), symbol (a string representing their game symbol ('X' or 'O'))
# Output: returns nothing, updates the gameboard
def make_move(gameboard, name, symbol):
  in_turn = True
  while in_turn:
    print()
    valid_move = False
    while not(valid_move):
      try:
        row = int(input(name + ", what row is your move? (Enter a number from 0 to 2): "))
      except ValueError:
        print("Please enter an integer between 0 and 2.")
        continue
      try:
        column = int(input(name + ", what column is your move? (Enter a number from 0 to 2): "))
      except ValueError:
        print("please enter an integer between 0 and 2")
        continue
      valid_move = True
    if row < 0 or row > 2 or column < 0 or column > 2:
      print("Invalid move, try again.\n")
    elif gameboard[row][column] != '   ':
      print("Someone's already there, try again.\n")
    else: 
      gameboard[row][column] = " " + symbol + " "
      in_turn = False

# The Game
# ========
print("Welcome to tic-tac-toe, X's will go first.\n")
player_X = input("What is the name of player X: ")
player_O = input("What is the name of player O: ")
number_of_turns = 0
while playing:
  if number_of_turns % 2 == 0:
    make_move(board, player_X, "X")
    print()
  else:
    make_move(board, player_O, "O")
    print()
  print_gameboard(board)
  print()
  if check_winner(board) == 'X':
    print(player_X + " wins!")
    playing = False
  elif check_winner(board) == 'O':
    print(player_O + " wins!")
    playing = False
  elif check_tied(board):
    print("Tie Game!")
    playing = False
  number_of_turns += 1

