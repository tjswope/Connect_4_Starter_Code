import random

from .constants import RED, WHITE, ROWS, COLS

class hillis:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

  def total_score(self, color, board):

    #create a value matrix of which squares in the board are the most valuable to occupy.
    # These values were loosely estimated based on my playstyle originally, but they were tweaked with testing.
    # squares that were more commonly members of 4-in-a-rows during my testing were given higher values, making the AI
    #much more likely to choose those squares in draw-ish positions (the win is more than 5 moves away)

    value = [
      [0, 0, 0, 1, 0, 0, 0],
      [0, 0.5, 1, 1.5, 1, 0.5, 0],
      [0.5, 1, 1.5, 2, 1.5, 1, 0],
      [1, 1.5, 2, 2.5, 2, 1.5, 1],
      [1.5, 2, 2.5, 3, 2.5, 2, 1.5],
      [2, 3, 4, 5, 4, 3, 2]
    ]


    if board.winner(color):
      return 1000000000
      #if either player has a win, that boardstate is given the highest possible value.
      # The AI will therefore play for this position (or defend against it) at all costs
    else:
      sum = 0

      #if there is no win for either player, the AI will check the total "square value" of each player's board
      #it will then play the move with the highest square value, playing towards the position with the most occupied "good" squares

      for r in range(ROWS): #in each row
        for c in range(COLS): #in each column
          if (board.get_piece(r, c) != 0):
            #if there is a piece
            if (board.get_piece(r, c).color == color):
              sum += value[r][c]
                      #add that square's value to the total sum if it is occupied by a piece of our color

      return sum
        #return total square value



