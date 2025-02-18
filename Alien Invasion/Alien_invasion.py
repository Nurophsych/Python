import sys
import pygame
from settings import Settings   
from Ship import Ship

class AlienInvasion:
    
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Alien Invasion")
        
        # Background color (light pink)
        self.bg_color = (255, 174, 215)
        
        self.ship = Ship(self)

        
        self.clock = pygame.time.Clock()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.sw, self.settings.sh))
        
    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  
            
            self.screen.fill(self.settings.bg_color) 
            pygame.display.flip()  # Update display
            
            self.clock.tick(60) 
            
            self.ship.blitme() 
                    
        pygame.quit()  # Ensure proper cleanup when exiting
        
     
        
            
if __name__ == '__main__':
    # Make instance and start
    ai = AlienInvasion()
    ai.main_loop()
