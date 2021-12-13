import random

from .constants import RED, WHITE, ROWS, COLS

class Ian:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.

  # this function will get the score!
  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

#total_score checks if you have pieces in a row and give you a positive score if you do. If you have 3 in a row and can win
  # by placing a fourth it gives you a high score. If the opponent has three in a row it gives you a high score and prioritizes
  # blocking them, unless you can win.
  def total_score(self, color, board):
    count = 0
    score = 0
    counter = 0
    if board.winner(color):
      return 10000000
    for row in range(ROWS):
      for col in range(COLS):
        if board.board[row][col] != 0 and board.board[row][col].color == color:
          count += 1

        else:
          count = 0

        if count == 2:
          score += 10
        if count == 3:
          score += 15
        if count == 4:
          score += 12000
    count = 0

    for row in range(ROWS):
      for col in range(COLS):
        if board.board[row][col] != 0 and board.board[row][col].color != color:
          count += 1
        else: count = 0

        if count == 3:
          score += 10000
    count = 0

    for col in range(COLS):
      for row in range(ROWS):
        if board.board[row][col] != 0 and board.board[row][col].color != color:
          count += 1
        else: count = 0

        if count == 3:
          score += 100
    count = 0

    for col in range(COLS):
      for row in range(ROWS):
        if board.board[row][col] != 0 and board.board[row][col].color == color:
          count += 1

        else:
          count = 0

        if count == 2:
          score += 10
        if count == 3:
          score += 15
        if count == 4:
          score += 20
    count = 0

    for row in range(3):
      for column in range(4):
        while counter < 4 and board.board[row + counter][column + counter] != 0 and board.board[row + counter][column + counter].color == color:
          counter += 1
          if counter == 2:
            score += 10
          if counter == 3:
            score += 15
          if counter == 4:
            score += 12000
    count = 0

    #diagonal up
    for row in range(3):
      for column in range(4):
        while counter < 4 and board.board[row + counter][6 - column - counter] != 0 and board.board[row + counter][6 - column - counter].color == color:
          counter += 1
          if counter == 2:
            score += 10
          if counter == 3:
            score += 15
          if counter == 4:
            score += 12000


    count = 0
    counter = 0
    return score
