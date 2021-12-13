import random

from .constants import RED, WHITE, ROWS, COLS

class Jake:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!

  #For my minimax algorithm I start by checking to see if there is going to be a winner.
  # If there are three in a row, the score is set to infinity, telling the AI that the opponent’s score will win if it is not blocked.
  # This results in the AI blocking.
  # Then, it loops through the board, checking for how many there are in a row horizontally, vertically, and diagonally, giving a score of 10 for every 2 in a row, adding to the score if three in a row is reached.
  # The AI looks to minimize the score, getting as many in a row as it can, blocks the player when it has three in a row, and makes sure it will not make a move that allows the player to place off of it and win (unless unavoidable).

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

  def total_score(self, color, board):
    score = 0
    counter = 0
    current = board.winner(color)

    if current:
      score = float("inf")

    # Check Horizontal
    for row in range(ROWS):
      for col in range(COLS):
        if board.board[row][col] != 0 and board.board[row][col].color == color:
          counter += 1

        else:
          counter = 0

        if counter == 2:
          score += 10
        elif counter == 3:
          score += 5
        elif counter == 4:
          score += 5

    for column in range(COLS):
      for row in range(ROWS):
        if board.board[row][column] != 0 and board.board[row][column].color == color:
          counter += 1
        else:
          counter = 0

        if counter == 2:
          score += 10
        elif counter == 3:
          score += 5
        elif counter == 4:
          score += 5


    #diagonal down
    for row in range(3):
      for column in range(4):
        while counter < 4 and board.board[row + counter][column + counter] != 0 and board.board[row + counter][column + counter].color == color:
          counter += 1

        else:
          counter = 0

        if counter == 2:
          score += 10
        elif counter == 3:
          score += 5
        elif counter == 4:
          score += 5

    #diagonal up
    for row in range(3):
      for column in range(4):
        while counter < 4 and board.board[row + counter][6 - column - counter] != 0 and board.board[row + counter][6 - column - counter].color == color:
          counter += 1

        else:
          counter = 0

        if counter == 2:
          score += 10
        elif counter == 3:
          score += 5
        elif counter == 4:
          score += 5

      counter = 0



    return score


