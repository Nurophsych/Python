import pygame
from pygame.sprite import Sprite
from PIL import Image

class Alien(pygame.sprite.Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load(r"C:\Users\nurop\OneDrive\Desktop\pYTHON COURSE\Projects\Tutorial1\Alien Invasion\Alien.bmp").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.mask = pygame.mask.from_surface(self.image)
        
        self.x = float(self.rect.x)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.settings.fleet_direction > 0:  # Moving right
            return self.rect.right >= screen_rect.right
        else:  # Moving left
            return self.rect.left <= 0

        
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = round(self.x)  # Convert float to integer for smooth movement
        
    
    
    
    
    