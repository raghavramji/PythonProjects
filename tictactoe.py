# main.py
import random
import time

def printBoard(board):
  for i in range(3):
    for j in range(3):
      if j == 2:
        print(" " + board[i][j], end="")
      else:
        print(" " + board[i][j] + " |", end="")
    if i != 2:
      print("\n-––+–––+–––")
  print("\n")


# Set up the board
board = []
for i in range(3):
  line = []
  for j in range(3):
    line.append(' ')
  board.append(line)


# Check if a player has won the game
def checkwin(board, player):
  # Horizontal wins
  if board[0][0] == player and board[0][1] == player and board[0][2] == player:
    return True
  if board[1][0] == player and board[1][1] == player and board[1][2] == player:
    return True
  if board[2][0] == player and board[2][1] == player and board[2][2] == player:
    return True
  
  #Vertical wins
  if board[0][0] == player and board[1][0] == player and board[2][0] == player:
    return True
  if board[0][1] == player and board[1][1] == player and board[2][1] == player:
    return True
  if board[0][2] == player and board[1][2] == player and board[2][2] == player:
    return True
  #Diagonal wins
  if board[0][0] == player and board[1][1] == player and board[2][2]== player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
    

printBoard(board)

tie = False
player = 'X'
flip = random.randint(1, 2)
if flip == 1:
  print("The coin flip shows that the computer (O) goes first!")
  player = 'O'
else:
  print("The coin flip shows that you (X) will go first!")

input("Press Enter to begin!")


  
# Smart Computer algorithm 

def AIcomputer(board): 
  # Check if AI has any moves that result in a win
  for i in range(3):
    for j in range(3):
      if Win(board, i, j, "O"):
        return[i, j]
  
  # Checks if opponent has any moves that result in a win
  for i in range(3):
    for j in range(3):
      if Win(board, i, j, "X"):
        return[i, j]
  
 # Checks for a move that is a fork
  for i in range(3):
   for j in range(3):
     if Fork(board,i,j,"O"):
       return[i,j]
  
  # Checks if there is a move that user can play for a Fork
  # If there are two forks, choose offense
  loseForks = 0
  Set = [0,0]
  for i in range(3):
    for j in range(3):
      if Fork(board,i,j,"X"):
        loseForks += 1
        Set = [i,j]
  
  if loseForks == 1:
    return Set
  elif loseForks == 2:
    if board[0][1] == " ":
      return[0,1]
    if board[1][0] == " ":
      return[1,0]
    if board[1][2] == " ":
      return[1,2]
    if board[2][1] == " ":
      return[2,1]
  
  
  # If the center is open, play it
  if board[1][1] == " ":
    return[1, 1]
  
  # If there's an open corner, use it
  corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
  for x in corners:
    if board[x[0]][x[1]] == " ":
      # corners.remove(c)
      return x
  
  #find open spot and return
  loc = getOpen(board)
  if loc != " ":
    return loc
 
#See is win is possible if user picks input position   
def testWin(board,i,j,player):
  newBoard = copyBoard(board)
  if newBoard[i][j] != " ":
    return False
  newBoard[i][j] = player
  return win(newBoard,player)
  
#Deep copy of board
def copyBoard(board):
  copy = []
  for a in range(3):
    line = []
    for b in range(3):
      line.append(board[a][b])
    copy.append(line)
  return copy
  
def Fork(board,i,j,player):
  newBoard = copyBoard(board)
  if newBoard[i][j] != " ":
    return False
    
  newBoard[i][j] = player
  winningMove = 0
  for k in range(3):
    for m in range(3):
      if newBoard[k][m] == " ":
        newBoard[k][m] = player
        if Win(newBoard,k,m,player):
          winningMove += 1
        newBoard[k][m] == " "
  if winningMove >= 2:
    return True 
  return False
  
  
def Win(board,i,j,player):
  copy = []
  for k in range(3):
    line = []
    for b in range(3):
      line.append(board[k][b])
    copy.append(line)
  
  if copy[i][j] != " ":
    return False
  
  copy[i][j] = player
  return checkwin(copy,player)      
  
  
  
def getOpen(board):
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        return[i, j]
  return " "
  
  
def full(board):
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        return False
  return True



while True:
  printBoard(board)      
      
  if player == 'X':
    while True:
      row = int(input("Pick a row to play: "))
      col = int(input("Pick a column to play: "))
      if (-1 < row and row < 3) and (-1 < col and col < 3) and board[row][col] == " ":
        board[row][col] = player
        break
      print("Not a valid move, try again")
  
  # Computer goes
  if player == 'O':
    time.sleep(1)
    play = AIcomputer(board)
    board[play[0]][play[1]] = player
  

  # Check if someone has won
  if checkwin(board, player):
    break
  # Check if all game spots are taken
  if full(board):
    tie = True
    break
  
  # Changes turns
  if player == 'X':
    player = 'O'
  else:
    player = 'X'

printBoard(board)
if tie:
  print("There was a tie!")
else:
  if player == 'X':
    print("You won!")
  else:
    print("The Computer won.")
