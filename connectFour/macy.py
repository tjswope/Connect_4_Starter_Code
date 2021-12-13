

from .constants import RED, WHITE

class Macy:

  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!

  def evaluate(self, board):
    return self.total_score(WHITE, board) - self.total_score(RED, board)

# My total_score method keeps track of the amount of each color in a consecutive row. The in_a_row variable does this.
# The more like pieces in a row, the greater the value added to the count variable that is returned.
# There is a 2D for loop for each of the four main ways of scoring: horizontally in a row, vertically in a column, left diagonally, and right diagonally.
# If an empty space or a piece of the opposing color is found, the in_a_row is set back to zero, because that is the end of the string of like pieces in a row.
# At the end of each loop, there are a set of if/elif statements that add an amount to count based on the amount of like pieces in a row after each loop through.
# The amount add to count increases as the amount of pieces increases.

#I got the idea to count the amount of pieces from a classmate during a short conversation.

  def total_score(self, color, board):
        count = 0
        # 6 rows
        for row in range(0, 6):
            in_a_row = 0
            # 7 cols
            for col in range(0, 7):
                if board.board[row][col] != 0 and board.board[row][col].color == color:
                    in_a_row += 1
                    if col != 0 and col != 6:
                        count += 5

                elif board.board[row][col] != 0 and board.board[row][col].color != color:
                    in_a_row = 0

                else:
                    in_a_row = 0
                # adds a value to count based on the amount of like pieces in a row
                if in_a_row == 2:
                    count += 100
                elif in_a_row == 3:
                    count += 1000
                elif in_a_row == 4:
                    count += 10000000000000
        # instead of in_a_row, this for loop uses a in_a_col variable that holds the same function as the in_a_row variable
        for col in range(0, 7):
            in_a_col = 0
            for row in range(0, 6):
                if board.board[row][col] != 0 and board.board[row][col].color == color:
                    in_a_col += 1

                elif board.board[row][col] != 0 and board.board[row][col].color != color:
                    in_a_col = 0

                else:
                    in_a_col = 0

                if in_a_col == 2:
                    count += 100
                elif in_a_col == 3:
                    count += 1000
                elif in_a_col == 4:
                    count += 10000000000000

        # # got this code template from tic tac toe starter code
        for row in range(0, 6 - 3):
            for column in range(0, 7 - 3):
                inner_count = 0
                in_a_row = 0
                while row + inner_count < 6 and column + inner_count < 7:
                    if board.board[row + inner_count][column + inner_count] != 0 and board.board[row + inner_count][column + inner_count].color == color:
                        in_a_row += 1

                    elif board.board[row + inner_count][column + inner_count] != 0 and board.board[row + inner_count][column + inner_count].color != color:
                        in_a_row = 0

                    else:
                        in_a_row = 0

                    if in_a_row == 2:
                        count += 100
                    elif in_a_row == 3:
                        count += 1000
                    elif in_a_row == 4:
                        count += 10000000000000

                    inner_count += 1

        # # got this code template from tic tac toe starter code
        for row in range(3, 6):
            in_a_row = 0
            for column in range(0, 7 - 3):
                inner_count = 0
                in_a_row = 0
                while row - inner_count >= 0 and column + inner_count < 7:
                    if board.board[row - inner_count][column + inner_count] != 0 and board.board[row - inner_count][column + inner_count].color == color:
                        in_a_row += 1

                    elif board.board[row - inner_count][column + inner_count] != 0 and board.board[row - inner_count][column + inner_count].color != color:
                        in_a_row = 0

                    else:
                        in_a_row = 0

                    if in_a_row == 2:
                        count += 100
                    elif in_a_row == 3:
                        count += 1000
                    elif in_a_row == 4:
                        count += 10000000000000

                    inner_count += 1

        #Below are other ideas I tried to code to enhance my program, but they seemed to interfere with my code above


        # This attempts to keep track of two like pieces in a row, a space, and then one more like piece.
        # If this situation is identified, a value is added to count in hopes of blocking.
        #This version loops looks through the rows to see if such a pattern exists.
        # for row in range(0,6):
        #     in_a_row = 0
        #     for col in range(0, 7):
        #         if board.board[row][col] != 0 and board.board[row][col].color == color:
        #             in_a_row += 1
        #             if in_a_row == 2 and row - 2 > 0 and row + 1 < 5:
        #                 row_before = row - 2
        #                 row_after = row + 1
        #                 if board.board[row_before][col] == 0 and board.board[row_after][col] == 0:
        #                     count += 100
        #         elif board.board[row][column] != 0 and board.board[row][column].color != color:
        #             in_a_row = 0
        #
        #         else:
        #             in_a_row = 0

        # This attempts to keep track of the same thing but in a different way.
        #This version loops looks through the cols to see if such a pattern exists.
        # for row in range(0, 6):
        #     in_a_row = 0
        #     for col in range(0, 7):
        #         # if board.board[row][col] != 0 and board.board[row][col].color == color:
                #     in_a_row += 1
                #     if in_a_row == 2 and col + 2 <= 6:
                #         col_after = col + 2
                #         col_empty = col + 1
                #         row_empty = row - 1
                #         if board.board[row][col_after] != 0 and board.board[row][col_after].color == color:
                #             if board.board[row_empty][col_empty] == 0:
                #                 count += 10000000000000
                #             elif board.board[row][col_empty] == 0:
                #                 count += 10000000000000
                # elif board.board[row][column] != 0 and board.board[row][column].color != color:
                #     in_a_row = 0
                #
                # else:
                #     in_a_row = 0

        return count
