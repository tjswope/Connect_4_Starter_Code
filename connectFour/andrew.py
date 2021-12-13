import random
from .constants import RED, WHITE, ROWS, COLS

class Andrew:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)


    #What I have done is check to see how close the AI is to winning, and whichever square presents both the most options AND is the closest to winning will be chosen. Values were determined by testing. Defense is intentionally left out due to the fact that everyone else's AIs most likely include them, and so if mine solely goes for offense all of theirs should revert to just trying to block. Beyond that, leaving out defense makes the AI both more efficient and also prevents issues resulting in weighing a victory over blocking an enemy (regardless of values, the chance is present for it to choose to block in this case if the values associated with block are anywhere near high enough to compete with advancing winning chances). Code to check if won is used to determine progress.
  def total_score(self, color, board):
    score = 0

    #vertical
    counter = 0
    for column in range(COLS):
      for row in range(ROWS):
        if self.board[row][column] != 0 and self.board[row][column].color == color:
          counter += 1
        else:
          counter = 0

        if counter >= 2:
          score+=3
        if counter >= 3:
          score+=5
        if counter >= 4:
          score+=10

      counter = 0

    #horizontal
    for row in range(ROWS):
      for column in range(COLS):
        if self.board[row][column] != 0 and self.board[row][column].color == color:
          counter += 1
        else:
          counter = 0

        if counter >= 2:
          score+=3
        if counter >= 3:
          score+=5
        if counter >= 4:
          score+=10

      counter = 0

    #diagonal
    #idagonal down
    for row in range(3):
      for column in range(4):
        while counter < 4 and self.board[row + counter][column + counter] != 0 and self.board[row + counter][column + counter].color == color:
          counter += 1

        if counter >= 2:
          score+=3
        if counter >= 3:
          score+=5
        if counter >= 4:
          score+=10
        counter = 0

      counter = 0

    #diagonal up
    for row in range(3):
      for column in range(4):
        while counter < 4 and self.board[row + counter][6 - column - counter] != 0 and self.board[row + counter][6 - column - counter].color == color:
          counter += 1

        if counter >= 2:
          score+=3
        if counter >= 3:
          score+=5
        if counter >= 4:
          score+=10
        counter = 0

      counter = 0

    return score

