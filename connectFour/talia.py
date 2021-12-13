import random

from .constants import RED, WHITE, ROWS, COLS

class Talia:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

# My code starts by creating a variable score, to keep track of the value of each player.
# Then I test if there is a winner, and loop through all the squares on the board.
# If there’s a winner, I add to my value. Then, after the loops, I return score.
  def total_score(self, color, board):
    score = 0
    if board.winner(color):
      for row in range(ROWS):
        for col in range(COLS):
          score = float("inf")
    return score

