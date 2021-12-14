import random
from .constants import RED, WHITE
from .constants import ROWS, COLS
class Alex:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)



  def total_score(self, color, board):
    potentialwinspots=[]
    absolutewinspots=[]
    compoundwinspots=0
    score=0
    if board.winner(color):
      return 100000

    for spot in self.winspots(color, board):
      if board.board[spot[0]-1][spot[1]] !=0 or spot[0]==5:
        absolutewinspots.append(spot)
      else:
        potentialwinspots.append(spot)
      for s in self.winspots(color, board):
        if spot[0]-1 == s[0] and spot[1] == s[1]:
          compoundwinspots += 1
    if len(absolutewinspots) > 1:
      score += 3000
    elif len(absolutewinspots) == 1:
      score += 300
    score+=len(potentialwinspots)*100
    score+=compoundwinspots*3000

    for row in range(ROWS):
      for col in range(COLS):
        if board.board[row][col] != 0 and board.board[row][col].color == color and board.board[row][col].col<5 and board.board[row][col].row>1:
          score+=1
        if board.board[row][col] != 0 and board.board[row][col].color == color and board.board[row][col].col==3:
          score+=1

    return score

  def horizontal_winspots(self, color, board):
    counter = 0
    Ocounter = 0
    winspots = []
    tempwinspot = None
    for row in range(ROWS):
      for column in range(COLS):
        for i in range(4):
          if column+3<=COLS-1:
            if board.board[row][column+i] == 0 and Ocounter ==0:
              Ocounter = 1
              tempwinspot=(row, column+i)
            elif board.board[row][column+i] != 0 and board.board[row][column+i].color == color:
              counter +=1
            else:
              Ocounter = 0
              counter = 0
              tempwinspot=None
            if counter==3 and Ocounter == 1:
              winspots.append(tempwinspot)
        Ocounter = 0
        counter = 0
        tempwinspot=None

      counter = 0
      Ocounter = 0
    return winspots

  def vertical_winspots(self, color,board):
    counter = 0
    Ocounter = 0
    winspots=[]
    tempwinspot=None
    for column in range(COLS):
      for row in range(ROWS):
        for i in range(4):
          if row+3<=ROWS-1:
            if board.board[row+i][column] == 0 and Ocounter ==0:
              Ocounter = 1
              tempwinspot=(row+i, column)
            elif board.board[row+i][column] != 0 and board.board[row+i][column].color == color:
              counter += 1
            else:
              tempwinspot=None
              Ocounter = 0
              counter = 0
            if counter==3 and Ocounter == 1:
              winspots.append(tempwinspot)

        Ocounter = 0
        counter = 0

      counter = 0
      Ocounter = 0

    return winspots

  def diagonal_winspots(self, color, board):
    Ocounter = 0
    counter = 0
    i=0
    tempwinspot=None
    winspots=[]

    #diagonal down
    for row in range(3):
      for column in range(4):
        while i < 4:
          if board.board[row + i][column + i] == 0 and Ocounter==0:
            Ocounter += 1
            tempwinspot=(row+i, column+i)
          elif board.board[row + i][column + i] != 0 and board.board[row + i][column + i].color == color:
            counter +=1
          else:
            Ocounter=0
            counter=0
            tempwinspot=None
          i+=1
        if counter==3 and Ocounter == 1:
          winspots.append(tempwinspot)

        counter = 0
        Ocounter = 0
        i=0

      counter = 0
      Ocounter = 0

    #diagonal up
    for row in range(3):
      for column in range(4):
        while i < 4:
          if board.board[row + i][6 - column - i] == 0 and Ocounter==0:
            Ocounter += 1
            tempwinspot=(row+i, column+i)
          elif board.board[row + i][6 - column - i] != 0 and board.board[row + i][6 - column - i].color == color:
            counter += 1
          else:
            Ocounter=0
            counter=0
            tempwinspot=None
          i+=1
        if counter==3 and Ocounter == 1:
          winspots.append(tempwinspot)
        counter = 0
        Ocounter = 0
        i=0

      counter = 0
      Ocounter = 0

    return winspots

  def winspots(self, color, board):
    horizontal= self.horizontal_winspots(color, board)
    vertical= self.vertical_winspots(color, board)
    diagonal= self.diagonal_winspots(color, board)
    for i in horizontal:
      for j in vertical:
        if i==j:
          horizontal.remove(i)
    total=horizontal+vertical

    for i in total:
      for j in diagonal:
        if i==j:
          diagonal.remove(i)
    total=total+diagonal
    return total


