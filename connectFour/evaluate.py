import random

from .constants import RED, WHITE

class Evaluate:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

  def total_score(self, color, board):
    return random.randint(1,10)

