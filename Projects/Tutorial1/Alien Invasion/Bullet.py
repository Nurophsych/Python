import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bulletColor
        
        # Create a bullet at the ship's current position
        self.rect = pygame.Rect(0, 0, self.settings.bulletWidth, self.settings.bulletHeight)
        self.rect.midtop = ai_game.ship.rect.midtop  # Position at the ship's top
        
        # Store the bullet's position as a float for smoother movement
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet upwards."""
        self.y -= self.settings.bulletSpeed  # Move the bullet upward
        self.rect.y = self.y  # Update the rect's position
        
    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)  # Draw the bullet

