import sys
import pygame
from settings import Settings
from ship import Ship


class AliensInvasion:
    def __init__(self):
        # Initialise a game and create game window
        pygame.init()
        self.clock = pygame.time.Clock()  # Frame rate(FPS)
        # Import Settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Aliens Absurd")
        self.ship = Ship(self)


    def run_game(self):

        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

            self._update_screen() 

            # FPS
    
    def _update_screen(self):
        # Update images on the screen, and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)
    
    def _check_events(self):
        # Respond to keypress and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right
                    self.ship.rect.x += 1

if __name__ == '__main__':
    # Making a game instant and run the game
    ai = AliensInvasion()
    ai.run_game()

