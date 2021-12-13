import random

from .constants import RED, WHITE


class Nathan:

    # "optimal" weights: (1, 5, 1.25, 2)
    #   didn't really test these too much
    # (Empty Weight, Filled Weight, Risk, Safety)
    # empty weight is how much they value empty spaces
    # filled weight is how much they value spaces filled by their piece
    # risk affects how much they value a great move for them (even if it's possibly bad for them)
    #   setting this to a high/larger value than Fear will make an aggressive AI
    #   they are fun to watch :)
    # safety affects how much they value what a move will do for the enemy
    #   setting this to a high/larger value than Greed will make a lame AI (which is usually the best plan)

    # AI Explanation:
    # the AI loops through 8 directions: up, down, left, right, and the four diagonals.
    # it sums up the consecutive number of empty and filled spaces multiplied by their respective weights.
    # when looping, it ignores base nodes (nodes to start checks FROM) that it has already checked.
    # it also makes sure not to lose when possible.
    # at the end, the AI raises the two scores to the power of their respective weights (risk and safety).

    def evaluate(self, board):
        return pow(self.total_score(WHITE, board), 1.25) - pow(self.total_score(RED, board), 2)

    def total_score(self, color, board):

        ROWS, COLS = 6, 7
        constants = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]  # stores all the consecutive-check vector directions

        EMPTY_WEIGHT = 1

        FILLED_WEIGHT = 5

        consecutive = 0
        closed_nodes = []  # stores the nodes we have already checked so we don't check them again

        if board.winner(color): # try to win (and not lose)
            return 999999

        for row in range(ROWS):
            for col in range(COLS):

                _row = ROWS - row - 1  # iterates from bottom up

                if board.board[_row][col] == 0:  # little optimization (i think)
                    continue

                if board.board[_row][col].color == color and (col, _row) not in closed_nodes:

                    closed_nodes.append((col, _row))

                    n = 0

                    for iteration in range(8):
                        x_mult = constants[iteration][0]
                        y_mult = constants[iteration][1]
                        while True:
                            n += 1
                            x_row = _row + n * x_mult
                            y_col = col + n * y_mult
                            if COLS > y_col >= 0 and ROWS > x_row >= 0:
                                if board.board[x_row][y_col] == 0:
                                    consecutive += EMPTY_WEIGHT
                                elif board.board[x_row][y_col].color == color:
                                    consecutive += FILLED_WEIGHT
                                    closed_nodes.append((y_col, x_row))
                                else:
                                    break
                            else:
                                break
                        n = 0

                else:
                    pass

        return consecutive

#########################################
