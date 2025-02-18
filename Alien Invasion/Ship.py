import pygame
from PIL import Image

class Ship:
    
    def __init__(self,ai_game):
        
        
        
        gif_path = "your_animated.gif"
        gif = Image.open("Spaceship (ani).gif")
        
        frame_count = gif.n_frames
        frames = []
        
        for frame in range(frame_count):
            gif.seek(frame)  # Move to the specific frame
            frame_image = gif.convert("RGBA")  # Ensure it has an alpha channel
            frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, "RGBA")
            frames.append(frame_surface)
            
        clock = pygame.time.Clock()
        running = True
        frame_index = 0
        
        
        self.blit(frames[frame_index], (0, 0))  # Draw the frame
        pygame.display.flip()
        
        frame_index = (frame_index + 1) % frame_count
        
        clock.tick(10)  # Adjust the speed of the animation