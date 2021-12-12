import pygame
from connectFour.constants import WIDTH, HEIGHT, RED, WHITE, SQUARE_SIZE
from connectFour.game import Game
from connectFour.algorithm import minimax
from connectFour.evaluate import Evaluate
from connectFour.evaluate2 import Evaluate2
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect 4')

def main():
    game = Game(WIN)
    player1 = Evaluate()
    player2 = Evaluate2()

    while not game.winner(WHITE) and not game.winner(RED):

        if game.turn == WHITE:
          value, new_board = minimax(game.get_board(), 4, True, WHITE, player1)
          game.ai_move(new_board)
        else:
          value, new_board = minimax(game.get_board(), 4, False, RED, player2)
          game.ai_move(new_board)

        game.update()

        for event in pygame.event.get():
            pass

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



main()
