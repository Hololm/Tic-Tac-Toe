#Imports os and sys for clearing console and exiting the program
from os import system
import sys


#Asks player if they want to play again
def kek():
      play_again = input("Play again? (y/n): ")
      if play_again == "y":
        system('clear')
        playagain()

      elif play_again == "n":
        system('clear')
        sys.exit()


#If user does not input y or n, it will prompt to retry, not needing a try except statement
      elif play_again != "y" or play_again != "n":
        print("Please put in y or n")
        kek()


#Function makes the essential parts of the game
def playagain():
  board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
  count = 0


  letters = ["X", "O"]
  isWon = False
  system('clear')
  playercount = 0
  turncount = 0


  #Creates the board essentially
  def thing():
    print("  0,   1,   2")
    for count, L in enumerate(board):
      print(L, count)


  thing()


  #Function redos if player makes a mistake
  def redo():
    try:
      row = input(f"{letters[playercount]}, input a row: ")
      col = input(f"{letters[playercount]}, input a column: ")
      system('clear')

      if board[int(row)][int(col)] != "-":
        print("Space is already occupied. Try again.")
        thing()
        redo()


#Checks if out of boundaries
    except:
      print("Out of boundaries. Try again.")
      thing()
      redo()
    else:
      board[int(row)][int(col)] = letters[playercount]


  #Loops the game
  while True:
    try:
      row = input(f"{letters[playercount]}, input a row: ")
      col = input(f"{letters[playercount]}, input a column: ")
      system('clear')


  #Checks if space is occupied
      if board[int(row)][int(col)] != "-":
        print("Space is already occupied. Try again.")
        thing()
        redo()
      turncount += 1


  #Checks Out of Boundary Inputs
    except:
      print("Out of boundaries. Try again.")
      thing()
      redo()
    else:
      board[int(row)][int(col)] = letters[playercount]


    thing()


  #Check Row Wins
    temparray = [[],[],[]]
    for eachrow in board:
      counter = 0
      if eachrow == [letters[playercount], letters[playercount], letters[playercount]]:
        isWon = True
        break


  #Checks Column in Row
      for eachcol in eachrow:
        if counter == 0:
          temparray[0].append(eachcol)
        if counter == 1:
          temparray[1].append(eachcol)
        if counter == 2:
          temparray[2].append(eachcol)
        counter += 1


  #Column Wins
    for eachcol in temparray:
      if eachcol == [letters[playercount], letters[playercount], letters[playercount]]:
        isWon = True
        break


  #First Possible Diagonal Win
    if board[0][0] == letters[playercount]:
      if board[0][0] == board[1][1] == board[2][2]:
        isWon = True
        break


  #Second Possible Diagonal Win
    if board[0][2] == letters[playercount]:
      if board[0][2] == board[1][1] == board[2][0]:
        isWon = True
        break


    if isWon == True:
      print("You win!")
      break


#If turncount is 9, game is a draw because max turns in tictactoe is 9
    if turncount == 9:
      print("The game is a draw!")
      kek()


#Turns between players
    playercount += 1
    playercount %= 2


  kek()
playagain()