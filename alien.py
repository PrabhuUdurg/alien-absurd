import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from ufos import Alien
from time import sleep
from game_stats import GameStats


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
        
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        


    def run_game(self):

        while True:
            # Watch for keyboard and mouse events
            
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen() 
            self.clock.tick(60)  # Frame rate(FPS)
            

    
    def _update_screen(self):
        # Update images on the screen, and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)
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
        self._check_bullet_alien_collision()
            
    def _ship_hit(self):
        self.stats.ships_left -= 1
        self.bullets.empty()
        self.aliens.empty()
        
        self._create_fleet()
        self.ship.center_ship()
        
        # Sleep
        sleep(0.5)
        
        
    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet
        
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        
        
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break 
            
    def _change_fleet_direction(self): 
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 
        
    
    def _create_alien(self, x_postion, y_position):
        new_alien = Alien(self)
        new_alien.x = x_postion
        new_alien.rect.x = x_postion
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
        
    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        
        
        current_x, current_y = alien_width, alien_height
        while current_y < self.settings.screen_height - 4 * alien_height:
            while current_x < self.settings.screen_width - alien_width:
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2
            current_y += alien_height * 2
            current_x = alien_width
        
if __name__ == '__main__':
    # Making a game instant and run the game
    ai = AliensInvasion()
    ai.run_game()

