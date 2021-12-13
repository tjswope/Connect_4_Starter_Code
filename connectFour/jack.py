import random

# My total_score function has computes a score in 4 directions: vertical, horizontal,
# diagonal from the top right, and diagonal from the bottom left.
# The algorithm scores consecutives on an exponential scale, with 1 in-a-row being worth 1 point,
# 2 in-a-row worth 3, 3 worth 9, and 4 worth 27.
# It scores (R-R-0-R) the same as (R-R-R). A previous iteration which scored (R-R-0-R) the
# same as (R-R) + (R) performed worse.
# This distinction is signifigant due to the exponential scoring scale.
from .constants import RED, WHITE, ROWS, COLS

class Evaluate:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

  def total_score(self, color, board):
    if board.winner(color):
      return 999

    totalScore = 0

    # vertical checker
    consecCounter = 0
    for column in range(COLS):
      consecCounter = 0
      for row in reversed(range(ROWS)):
        if row == 0 and board.board[row][column] == 0:
          break
        if row == 2 and consecCounter == 0:
          break
        if board.board[row][column] != 0 and board.board[row][column].color == color: # first condition is to prevent a runtime exception
          if consecCounter == 0:
            consecCounter += 1
          else:
            consecCounter *= 3
        elif board.board[row][column] != 0 and board.board[row][column].color != color:
          consecCounter = 0
        else: # if there is an empty space
          totalScore += consecCounter
          break
      totalScore += consecCounter

    # horizontal checker
    consecCounter = 0
    for row in range(ROWS):
      consecCounter = 0
      for column in range(COLS):
        if column == 4 and consecCounter == 0:
          break
        if board.board[row][column] != 0 and board.board[row][column].color == color:
          if consecCounter == 0:
            consecCounter += 1
          else:
            consecCounter *= 3
        elif board.board[row][column] != 0 and board.board[row][column].color != color:
          consecCounter = 0
      totalScore += consecCounter

    # diagonal from the left
    consecCounter = 0
    for row in range(ROWS): # loops through number of rows
      for column in range(COLS): # loops through number of columns
        consecCounter = 0
        for k in range(COLS): # loops through number of columns
          if row+k == ROWS or column+k == COLS:
            break
          else:
            if board.board[row+k][column+k] != 0 and board.board[row+k][column+k].color == color:
              if consecCounter == 0:
                consecCounter += 1
              else:
                consecCounter *= 3
            elif board.board[row+k][column+k] != 0 and board.board[row+k][column+k].color != color:
              consecCounter = 0
            # elif board.board[row+k][column+k] == 0:
            #   totalScore += consecCounter
            #   consecCounter = 0
        totalScore += consecCounter

    #diagonal from the right
    consecCounter = 0
    for row in reversed(range(ROWS)): # loops through number of rows
      for column in range(COLS): # loops through number of columns
        consecCounter = 0
        for k in range(COLS): # loops through number of columns
          if row-k < 0 or column+k == COLS:
            break
          else:
            if board.board[row-k][column+k] != 0 and board.board[row-k][column+k].color == color:
              if consecCounter == 0:
                consecCounter += 1
              else:
                consecCounter *= 3
            elif board.board[row-k][column+k] != 0 and board.board[row-k][column+k].color != color:
              consecCounter = 0
            # elif board.board[row-k][column-k] == 0:
            #   totalScore += consecCounter
            #   consecCounter = 0
        totalScore += consecCounter

    return totalScore


