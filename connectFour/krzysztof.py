import random

from .constants import RED, WHITE, ROWS, COLS

class Krzysztof:

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

  #this winner function relies on the value of consecutives,
  # for every consecutive piece the score gets increased and higher consecutives have higher values
  #also if you have two or three in a row but a win is not possible the score does not increase
  #also reduces run time by not checking empty columns
  #if all scores at the start are equal the algorithm will prioritize the inner columns to ensure best moves
  #also checks if a win is possible and if so it will make that move no matter what
  def total_score(self, color, board):
    score = 0

    if board.winner(color):
      score += 999

    vert = 0
    #checking for vertical consecutives and if there are consecutives then add to the scoring
    for column in range(COLS):
          vert = 0
          for row in reversed(range(ROWS)):
            if row == 0 and board.board[row][column] == 0:
              break
            if row == 2 and vert == 0:#if we get to the third top square and you have no pieces biult up then break
              break
            if board.board[row][column] != 0 and board.board[row][column].color == color:#if consecutives happen as a result of the move then add 1 to the scoring
              if vert == 0:
                vert += 1
              else:
                vert *= 3
            elif board.board[row][column] != 0 and board.board[row][column].color != color:#if there is a blockade then consecutives don't matter and set the score to zero
              vert = 0
            else:
              score += vert
              vert = 0
              break
          score += vert

    #checking for horizontal consecutives
    horizon = 0
    for row in range(ROWS):
      horizon = 0
      for column in range(COLS):
        if column == 4 and horizon == 0:
          break
        if board.board[row][column] != 0 and board.board[row][column].color == color:
          if horizon == 0:
            horizon += 1
          else:
            horizon *= 3
        elif board.board[row][column] != 0 and board.board[row][column].color != color:#if there is a blockade then consecutives don't matter and set the score to zero
          horizon = 0
      score += horizon

    #diagonal going down
    down = 0
    for row in range(ROWS):
      for column in range(COLS):
        for k in range(COLS):
          if row + k > ROWS-1 or column+k > COLS-1:
            break
          if board.board[row + k][column + k] != 0 and board.board[row + k][column + k].color == color:
            if down == 0:
              down += 1
            else:
              down *= 3
          elif board.board[row+k][column+k] != 0 and board.board[row+k][column+k].color != color:
            down = 0
        score += down
        down = 0

  #diagonal going up
    up = 0
    for row in reversed(range(ROWS)):
      for column in range(COLS):
        up = 0
        for k in range(COLS):
          if row - k < 0 or column+k > COLS-1:
            break
          if board.board[row - k][column + k] != 0 and board.board[row - k][column + k].color == color:
            if up == 0:
              up += 1
            else:
              up *= 3
          elif board.board[row-k][column+k] != 0 and board.board[row-k][column+k].color != color:
            up = 0
        score += up
        up = 0

      if board.board[5][3] != 0 and board.board[5][3].color == color:
        score *= 1.25
      if (board.board[5][4] != 0 and board.board[5][2] != 0) and (board.board[5][4].color == color or board.board[5][2].color == color):
        score *= 1.2
      if (board.board[5][5] != 0 and board.board[5][1] != 0) and (board.board[5][5].color == color or board.board[5][1].color == color):
        score *= 1.1
    return score

