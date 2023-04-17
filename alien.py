import sys
import pygame


class AliensInvasion:
    def __init__(self):
        # Initialise a game and create game window
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Aliens Absurd")

    def run_game(self):

        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    # Making a game instant and run the game
    ai = AliensInvasion()
    ai.run_game()
