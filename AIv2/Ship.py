import pygame
from PIL import Image
from settings import Settings

class Ship:
    
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        
        
        
        gif_path = (r"C:\Users\nurop\OneDrive\Desktop\pYTHON COURSE\Projects\Tutorial1\Alien Invasion\Spaceship (ani).gif")
        gif = Image.open(gif_path)
        
        
        frame_count = gif.n_frames
        self.frames = []
        
        for frame in range(gif.n_frames):
            gif.seek(frame)  # Move to the specific frame
            frame_image = gif.convert("RGBA")  # Ensure it has an alpha channel
            frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, "RGBA")
            self.frames.append(frame_surface)
            
        self.frame_index = 0
        self.frame_count = len(self.frames)
        self.animation_speed = 10
        self.counter = 0
        
        self.x = 100
        self.y = 100
        
        def update(self):
            self.counter += 1
            if self.counter >= self.animation_speed:
                self.frame_index = (self.frame_index + 1) % self.frame_count
                self.counter = 0
                
        def blitme(self):
            current_frame = self.frames[self.frames_index]
            self.screen.blit(current_frame, (self.x, self.y))
                
            
        #clock = pygame.time.Clock()
        #running = True
        #frame_index = 0
        
        
        #self.blit(frames[frame_index], (0, 0))  # Draw the frame
        #pygame.display.flip()
        
        #frame_index = (frame_index + 1) % frame_count
        
        #clock.tick(10)  # Adjust the speed of the animation