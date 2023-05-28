import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


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
        self.bullets = pygame.sprite.Group()


    def run_game(self):

        while True:
            # Watch for keyboard and mouse events
            
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen() 
            self.clock.tick(60)  # Frame rate(FPS)
            

    
    def _update_screen(self):
        # Update images on the screen, and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            pygame.display.flip()
            
    
    def _check_events(self):
        # Respond to keypress and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keyup_events(self, event):
        # Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _check_keydown_events(self, event):
        # Respond to key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _fire_bullet(self):
        # Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullet_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
                
    def _update_bullets(self):
        # Update position of bullets and get rid of old bullets
        # Update bullet positions
        self.bullets.update()
        
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
                        
if __name__ == '__main__':
    # Making a game instant and run the game
    ai = AliensInvasion()
    ai.run_game()

