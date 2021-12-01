# makes an actual copy of the object not just a reference to the object. BOXES!
from copy import deepcopy
from .constants import RED, WHITE


# this function will be called recursively
# current_board will be a board object - based on this board
# depth - how far am i making this tree - every time we call this function the depth will decrease by one.
# max_player - boolean value - are we trying minimize or maximize?
# game - the actual game object. 
def minimax(current_board, depth, max_player, color):
  # evaluate position when we reach the depth of the tree, evaluations bubble up. 
  if depth == 0:# or current_board.winner(RED) != False or current_board.winner(WHITE) != False:
    return current_board.evaluate(), current_board

  if max_player:
    maxEval = float('-inf')
    best_move = None
    for move in get_all_moves(current_board, WHITE):
      evaluation = minimax(move, depth-1, False, RED)[0]
      maxEval = max(maxEval, evaluation)
      if maxEval == evaluation:
        best_move = move

    return maxEval, best_move

  else:
    minEval = float('inf')
    best_move = None
    for move in get_all_moves(current_board, RED):
      evaluation = minimax(move, depth-1, True, WHITE)[0]
      minEval = min(minEval, evaluation)
      if minEval == evaluation:
        best_move = move

    return minEval, best_move


# This function crates a deep copy of the current board, determines all possible moves that color can make, and returns a list that contains the boards that would result from the possible moves.
def get_all_moves(board, color):
    moves = []                                # this array will contain Boards
    possible_moves = board.get_valid_moves()  # gets an array that contains the lowest open row in each column. It's main purpose is to see if a column is full so that we can skip over that row. 
    for column in range(len(possible_moves)):      # loop through each column
      if possible_moves[column] != -1:             # column is full if it has a lowest open row of -1 so we can skip it.
        temp_board = deepcopy(board)               # creates a deep copy of the board as opposed to a shallow copy.
        temp_board.add_piece(color, column)        # add a piece to the new copy of board in column
        temp_board.print()                       # uncomment if you want to debug your algorothim to see what moves are being considered.
        moves.append(temp_board)                  # add the new board to the list

    return moves
