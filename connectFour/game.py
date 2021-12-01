import pygame
from .constants import RED, WHITE
from .board import Board

class Game:

  
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
      self.board = Board()
      self.turn = RED

    def winner(self, col):
        return self.board.winner(self.turn)

    def reset(self):
        self._init()

    def add_piece(self, column):  
      if self.board.add_piece(self.turn, column):
        self.board.print()
        if self.board.winner(self.turn):
          winner = "red" if self.turn == RED else "white"
          print(winner + " is the winner")
        self.change_turn()


    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
      return self.board

    # return the new board after a move.
    # will pass a new board object to the game 
    def ai_move(self,board):
      self.board = board
      if self.board.winner(self.turn):
          print("white is the winner")
      self.change_turn()
