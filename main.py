import time
import random as r
import pygame
from connectFour.constants import WIDTH, HEIGHT, RED, WHITE, SQUARE_SIZE
from connectFour.game import Game
from connectFour.algorithm import minimax
from connectFour.evaluate import Evaluate

from connectFour.andrew import Andrew
from connectFour.annie import Annie
from connectFour.hillis import hillis
from connectFour.ian import Ian
from connectFour.jake import Jake
from connectFour.jack import Jack
from connectFour.krzysztof import Krzysztof
from connectFour.macy import Macy
from connectFour.nathang import Nathan
from connectFour.phillip import Phillip
from connectFour.ryan import Ryan
from connectFour.simon import Simon
from connectFour.talia import Talia
from connectFour.Alex import Alex


FPS = 60
DEPTH = 4
BEST_OF = 2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect 4')


def main():
    game = Game(WIN)
    player1 = Evaluate()      # white
    player2 = Krzysztof()         # red
    first = r.randint(0,1)
    player1_wins = 0
    player2_wins = 0

    while player1_wins < BEST_OF and player2_wins < BEST_OF:
        game.reset(first)
        first+=1

        while not game.winner(WHITE) and not game.winner(RED) and not game.board.is_full():

            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), DEPTH, True, WHITE, player1)
                game.ai_move(new_board)
            else:
                value, new_board = minimax(game.get_board(), DEPTH, False, RED, player2)
                game.ai_move(new_board)

            game.change_turn()
            game.update()

            for event in pygame.event.get():
                pass

        if game.winner(WHITE):
            print("white is the winner")
            game.board.print()
            player1_wins+=1

        elif game.winner(RED):
            print("red is the winner")
            game.board.print()
            player2_wins+=1

        time.sleep(2)

    print("White won " + str(player1_wins))
    print("Red won " + str(player2_wins))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
