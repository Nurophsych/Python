import pygame
from PIL import Image
from settings import Settings
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Set the ship's dimensions and position
        self.width = 150
        self.height = 150
        self.x2 = (self.settings.sw / 2) - (self.width / 2)
        self.y2 = self.settings.sh - self.height  # Position at the bottom
        
        # Load the animated GIF (relative path for better portability)
        gif_path = r"Spaceship (ani).gif"  # Use relative path
        gif = Image.open(gif_path)
        
        # Initialize frames for animation
        self.frames = []
        for frame in range(gif.n_frames):
            gif.seek(frame)  # Move to the specific frame
            frame_image = gif.convert("RGBA")  # Ensure it has an alpha channel
            frame_image = frame_image.resize((self.width - 50, self.height - 50))  # Resize frames
            frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, "RGBA")
            self.frames.append(frame_surface)

        # Animation initialization
        self.frame_index = 0
        self.frame_count = len(self.frames)
        self.animation_speed = 10  # Controls animation speed
        self.counter = 0
        
        # Initialize the rect (for positioning and collision detection)
        self.rect = self.frames[0].get_rect()  # Use the first frame's rect as base
        self.rect.midbottom = (self.settings.sw / 2, self.settings.sh - 10)  # Position at the bottom
    
    def update(self):
        """Update the ship's position and animation."""
        # Update animation frame
        self.counter += 1
        if self.counter >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % self.frame_count
            self.counter = 0

        # Update the position of the ship
        self.rect.x = self.x2  # Update the rect's x position to match ship's x
        self.rect.y = self.y2  # Update the rect's y position to match ship's y
    
    def blitme(self):
        """Draw the ship at its current position."""
        current_frame = self.frames[self.frame_index]
        self.screen.blit(current_frame, self.rect)  # Draw the current frame using the rect position

    def center_ship(self):
        """Center the ship on the screen."""
        self.screen_rect = self.screen.get_rect()  # Get screen rectangle
        self.rect.midbottom = self.screen_rect.midbottom  # Position ship
        self.x2 = float(self.rect.x)  # Use float for smoother movement
        self.y2 = float(self.rect.y)
