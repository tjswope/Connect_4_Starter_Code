import pygame
from .constants import SQUARE_SIZE

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color


    def calc_x(self):
        return SQUARE_SIZE * self.col + SQUARE_SIZE // 2


    def calc_y(self):
        return SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - 6
        pygame.draw.circle(win, self.color, (self.calc_x(), self.calc_y()), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.calc_x(), self.calc_y()), radius)

    def move(self, row):
        self.row = row
        self.calc_pos()

    def __repr__(self):
        return str(self.color)