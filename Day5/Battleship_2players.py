from random import randint

board = []
players = []
for x in range(0, 10):
  board.append(["O"] * 10)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row1 = random_row(board)
ship_col1 = random_col(board)
ship_row2 = random_row(board)
ship_col2 = random_col(board)
players.append(input("Enter first player name"))
players.append(input("Enter second player name, if u don't have any, press enter"))

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print ("Turn", turn + 1)
  print_board(board)
  if players[1] != "":
    print (players[0] + "- Your turn now")
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row - 1 == ship_row1 and guess_col - 1 == ship_col1 \
          or guess_row - 1 == ship_row2 and guess_col - 1 == ship_col2:
    print ("Congratulations! " + players[0] + " You sank my battleship!")
    break
  else:
    if guess_row not in range(1,11) or \
      guess_col not in range(1,11):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row-1][guess_col-1] == "X":
      print( "You guessed that one already." )
    else:
      print ("You missed my battleship!")
      board[guess_row-1][guess_col-1] = "X"
    if players[1] != "":
      print_board(board)
      print(players[1] + "- Your turn now")
      guess_row = int(input("Guess Row: "))
      guess_col = int(input("Guess Col: "))
      if guess_row - 1 == ship_row1 and guess_col - 1 == ship_col1 \
              or guess_row - 1 == ship_row2 and guess_col - 1 == ship_col2:
        print("Congratulations! " + players[1] + " You sank my battleship!")
        break
      else:
        if guess_row not in range(1, 11) or \
                guess_col not in range(1, 11):
          print("Oops, that's not even in the ocean.")
        elif board[guess_row - 1][guess_col - 1] == "X":
          print("You guessed that one already.")
        else:
          print("You missed my battleship!")
          board[guess_row - 1][guess_col - 1] = "X"
    if turn == 3:
      print ("Game Over")