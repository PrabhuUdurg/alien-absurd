import sys
import pygame
from settings import Settings


class AliensInvasion:
    def __init__(self):
        # Initialise a game and create game window
        pygame.init()
        pygame.display.set_caption("Aliens Absurd")

        self.clock = pygame.time.Clock()  # Frame rate(FPS)

        # Import Settings

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

    def run_game(self):

        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(60)  # FPS

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)


if __name__ == '__main__':
    # Making a game instant and run the game
    ai = AliensInvasion()
    ai.run_game()
