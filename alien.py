import sys
import pygame
from settings import Settings
from ship import Ship

class AliensInvasion:
    def __init__(self):
        # Initialise a game and create game window
        pygame.init()

        self.clock = pygame.time.Clock()  # Frame rate(FPS)

        self.ship = Ship(self)

        # Import Settings

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Aliens Absurd")


    def run_game(self):

        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self._update_screen()


            
            self.clock.tick(60)  # FPS
    
    def _update_screen(self):
        # Update images on the screen, and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    # Making a game instant and run the game
    ai = AliensInvasion()
    ai.run_game()
