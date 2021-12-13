import random

from .constants import RED, WHITE, ROWS, COLS

class Phillip:

  # Algorithm explanation
  # The algorithm wants to minimize the score of red and maximize the score of white. Both red and white are
  # given a score that corresponds to the number of ways they can win. The minimax function prioritizes blocking
  # red, because after white makes its turn, it becomes red’s turn. For example, if red has 3-in-a-row and white
  # has 2-in-a-row, white moves to block red instead of placing the piece to get 3-in-a-row, or else red would
  # win on the next move. Both 4-in-a-row and 3-in-a-row conditions add to the score. The counter, which tracks
  # the number of pieces in a row, is also added to the score so that 2-in-a-row win conditions can be considered.
  # The function evaluate returns the value of white’s score minus red’s score. If the value is negative it will
  # have to block red from winning. If the value is positive it will make a move that makes white win.

    # this function will get the score!
  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

  def total_score(self, color, board):
    score = 0
    counter = 0
    # horizontal
    for row in reversed(range(ROWS)):
      for column in reversed(range(COLS)):
        if board.board[row][column] != 0 and board.board[row][column].color == color:
          counter+=1
        # elif board.board[row][column] == 0:
        #   counter +=1
        elif board.board[row][column] != 0 and board.board[row][column].color != color:
          counter = 0
        if counter == 4 and color == RED:
          score+=10
        if counter == 4 and color == WHITE:
          score+=8
        if counter == 3 and color == RED:
          score+=4
        if counter == 3 and color == WHITE:
          score +=2
        score+=counter
        counter = 0
    # vertical
    for column in reversed(range(COLS)):
      for row in range(ROWS):
        if board.board[row][column] != 0 and board.board[row][column].color == color:
          counter += 1
        # elif board.board[row][column] == 0:
        #   counter += 1
        elif board.board[row][column] != 0 and board.board[row][column].color != color:
          counter = 0
        if counter == 4 and color == RED:
          score+=10
        if counter == 4 and color == WHITE:
          score+=8
        if counter == 3 and color == RED:
          score+=4
        if counter == 3 and color == WHITE:
          score +=2
        score+=counter
        counter = 0
    #diagonal down
    for row in range(3):
      for column in range(4):
        while counter < 4 and board.board[row + counter][column + counter] != 0 and board.board[row + counter][column + counter].color == color:
          counter += 1
        # while counter < 4 and board.board[row + counter][column + counter] == 0:
        #   counter += 1
        if counter == 4 and color == RED:
          score+=10
        if counter == 4 and color == WHITE:
          score+=8
        if counter == 3 and color == RED:
          score+=4
        if counter == 3 and color == WHITE:
          score +=2
        score+=counter
        counter = 0
    #diagonal up
    for row in range(3):
      for column in range(4):
        while counter < 4 and board.board[row + counter][6 - column - counter] != 0 and board.board[row + counter][6 - column - counter].color == color:
          counter += 1
        # while counter < 4 and board.board[row + counter][6 - column - counter] == 0:
        #   counter += 1
        if counter == 4 and color == RED:
          score+=10
        if counter == 4 and color == WHITE:
          score+=8
        if counter == 3 and color == RED:
          score+=4
        if counter == 3 and color == WHITE:
          score +=2
        score+=counter
        counter = 0

    # for row in reversed(range(ROWS)):
    #   if board.board[row][column] == 0:
    #     board.board[row][column] = Piece(row, column, color)
    #     return True
    #
    # return False

    return score
