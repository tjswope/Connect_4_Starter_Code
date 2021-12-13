import pygame
from connectFour.constants import WIDTH, HEIGHT, RED, WHITE, SQUARE_SIZE
from connectFour.game import Game
from connectFour.algorithm import minimax
from connectFour.evaluate import Evaluate

from connectFour.andrew import Andrew
from connectFour.annie import Annie
from connectFour.ryan import Ryan
from connectFour.simon import Simon
from connectFour.jake import Jake
from connectFour.nathang import Nathan
from connectFour.talia import Talia


from connectFour.evaluate2 import Evaluate2
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect 4')

def main():
    game = Game(WIN)
    player1 = Simon()
    player2 = Ryan()

    while not game.winner(WHITE) and not game.winner(RED):

        if game.turn == WHITE:
          value, new_board = minimax(game.get_board(), 5, True, WHITE, player1)
          game.ai_move(new_board)
        else:
          value, new_board = minimax(game.get_board(), 5, False, RED, player2)
          game.ai_move(new_board)

        game.update()

        for event in pygame.event.get():
            pass

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



main()
