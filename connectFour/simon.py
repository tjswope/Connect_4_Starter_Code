import random

from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, YELLOW, GREY



class Simon:

    # The Best Board Evaluation Function To Ever Exist: By Simon Roling
    # TO START, THE FUNCTION EVALUATES TO SEE IF A WIN IS PLAUSIBLE WITHIN THE NEXT FEW MOVES, AND IF IT IS IT TAKES ACTION TO BLOCK IT BY SETTING THE SCORE TO INFINTY.
    # AFTER FULLFILLING ANY NECESSARY BLOCKS, IT WILL CHECK THE HORIZONTAL USING THE SAME LOOP THAT THE CHECK WINNER USED, BUT THIS TIME IT ALSO EVALUATES EMPTY SPACES AND ASSIGNS A SCORE ACCORDINGLY.
    # AFTER CHECKING THE HORIZONTAL SCORE, IT CHECKS THE VERTICAL AND USES A SIMILAR SCORING SYSTEM TO THE HORIZONTAL (NUMBER IN A ROW*5000 + 3000 WHENEVER THERE IS AN EMPTY SPACE AFTER A SAME COLORED PIECE, AND MINUS 5000 WHEN THE PIECE ADJACENT IS OF THE OPPOSITE COLOR.
    # IT THEN CHECKS DIAGONALS AND RETURNS A TOTAL BOARD SCORE.

    # Functions for evaluating the board. These functions will be used by the minimax algorithm.
    # this function will get the score!

    def evaluate(self, board):
        return self.total_score(WHITE, board) - self.total_score(RED, board)

    def total_score(self, color, board):
        currentResult = board.winner(color)
        score = 0
        in_a_row = 0
        in_a_row_vert = 0

        if currentResult:
            return float("inf")

        # Horizontal

        for row in range(ROWS):
            for column in range(COLS):
                if board.board[row][column] != 0 and board.board[row][column].color == color:
                    in_a_row += 1


                elif board.board[row][column] == 0 and in_a_row > 0:
                    score += 3000
                    in_a_row = 0

                elif board.board[row][column] == 0 and in_a_row == 0:
                    in_a_row = 0

                else:
                    score = score - 5000

                score = score + 5000 * in_a_row

        for column in range(COLS):
            for row in range(ROWS):
                if board.board[row][column] != 0 and board.board[row][column].color == color:
                    in_a_row_vert += 1


                elif board.board[row][column] == 0 and in_a_row > 0:
                    score += 3000
                    in_a_row_vert = 0

                elif board.board[row][column] == 0 and in_a_row == 0:
                    in_a_row_vert = 0

                else:
                    score = score - 5000
                    in_a_row_vert = 0

                score = score + 5000 * in_a_row_vert

        # diagonal up
        in_a_row_up = 0
        for row in range(3):
            for column in range(4):
                while in_a_row_up < 4 and board.board[row + in_a_row_up][6 - column - in_a_row_up] != 0 and \
                        board.board[row + in_a_row_up][6 - column - in_a_row_up].color == color:
                    in_a_row_up += 1

        score += 5000 * in_a_row_up

        return (score)
