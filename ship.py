import pygame


class Ship:
    """ A class to manage the ship """ 

    def __init__(self, ai_game):
        """ Init the ship and adding start position """ 
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        

       #Load the ship image and get its rect.
        self.image = pygame.image.load('ship-al-abs.bmp')
        self.rect = self.image.get_rect()

       #Start each new ship at the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self): 
        """ Draw the ship its current location """ 
        self.screen.blit(self.image, self.rect)
        
    def _check_events(self):
        # Respond to keypress and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.rect.x += 1