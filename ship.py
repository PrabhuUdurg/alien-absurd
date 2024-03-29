import pygame


class Ship:
    """ A class to manage the ship """ 

    def __init__(self, ai_game):
        """ Init the ship and adding start position """ 
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

       #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

       
       #Start each new ship at the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom
       
       #Store a decimal value for the ship's horizontal position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
       
        self.moving_right = False
        self.moving_left = False 
        self.moving_down = False 
        self.moving_up = False 
        
        
    def blitme(self): 
        """ Draw the ship its current location """ 
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """ Update the ships position based on the movement flag """
        if self.moving_right and self .rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.rect.x += 1
        if self.moving_left and self .rect.left > 0:
            self.x -= self.settings.ship_speed
            self.rect.x -= 1
            
        if self.moving_down and self .rect.bottom < self.screen_rect.bottom:
            self.y -= self.settings.ship_speed
            self.rect.y -= 1
            
        if self.moving_up and self .rect.top < self.screen_rect.top:
            self.y += self.settings.ship_speed
            self.rect.y += 1
            
        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
            
            
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom 
        self.x = float(self.rect.x)