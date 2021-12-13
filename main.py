import time
import random as r
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
DEPTH = 4
BEST_OF = 2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect 4')


def main():
    game = Game(WIN)
    player1 = Simon()
    player2 = Ryan()
    first = r.randint(0,1)
    player1_wins = 0
    player2_wins = 0

    while player1_wins < BEST_OF and player2_wins < BEST_OF:
        game.reset(first)
        if first % 2 == 0:
            game.turn = WHITE
        first+=1

        while not game.winner(WHITE) and not game.winner(RED) and not game.board.is_full():

            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), DEPTH, True, WHITE, player1)
                game.ai_move(new_board)
            else:
                value, new_board = minimax(game.get_board(), DEPTH, False, RED, player2)
                game.ai_move(new_board)

            if game.winner(WHITE):
                player1_wins+=1
            elif game.winner(RED):
                player2_wins+=1
            game.update()

            for event in pygame.event.get():
                pass
        time.sleep(2)

    print("White won " + str(player1_wins))
    print("Red won " + str(player2_wins))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
