import random

from .constants import RED, WHITE


class Ryan:

    # my AI loops through in the 4 basic directions
    # it makes sure not to lose when possible
    # the the score very high if they win. check for horizontal, vertical, and diagnal to add to the score
    # you add for consecutive pieces and the score is determined based on the person playing

    def evaluate(self, board):
        return self.total_score(WHITE, board) - self.total_score(RED, board)

    # the the score very high if they win. check for horizontal, vertical, and diagnal to add to the score
    def total_score(self, color, board):

        consecutive = 0
        ROWS, COLS = 6,7

        if board.winner(color):
            return 9988888888998

        for row in range(ROWS):
            for col in range(COLS):
                if board.board[row][col] == color:
                    n = 0

                    # horizontal going to right
                    while True:
                        n += 1
                        ycol = col + n
                        if ycol < COLS:
                            if board.board[row][ycol].color == color:
                                consecutive += 2
                            else:
                                break
                        else:
                            break

                    n = 0

                    # horizontal to the left
                    while True:
                        n -= 1
                        ycol = col + n
                        if ycol >= 0:
                            if board.board[row][ycol].color == color:
                                consecutive += 2
                            else:
                                break
                        else:
                            break

                    n = 0

                    # vertial up
                    while True:
                        n += 1
                        xrow = row + n
                        if xrow < row:
                            if board.board[xrow][col].color == color:
                                consecutive += 2
                            else:
                                break
                        else:
                            break

                    n = 0

                    # vertical down
                    while True:
                        n -= 1
                        xrow = row + n
                        if xrow >= 0:
                            if board.board[xrow][col].color == color:
                                consecutive += 2
                            else:
                                break
                        else:
                            break

                    n = 0

                    # diagonal down left
                    while True:
                        n -= 1
                        xrow = row + n
                        ycol = row + n
                        if xrow >= 0 and ycol >= 0:
                            if board.board[xrow][ycol].color == color:
                                consecutive += 2
                            else:
                                break
                        else:
                            break

                    n = 0

                    # diagonal down right
                    while True:
                        n += 1
                        xrow = row + n
                        ycol = row + n
                        if xrow >= 0 and ycol >= 0:
                            if board.board[xrow][ycol].color == color:
                                consecutive += 2
                            else:
                                break
                        else:
                            break

                    n = 0

        return consecutive
