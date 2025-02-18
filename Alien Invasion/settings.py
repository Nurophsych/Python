import pygame


class Settings:
    
    def __init__(self):
        
        #screen settings
         self.screen_info = pygame.display.Info()
         self.sw = self.screen_info.current_w
         self.sh = self.screen_info.current_h - 50
        
         self.screen = pygame.display.set_mode((self.sw,self.sh), pygame.RESIZABLE)
         self.bgcolor = self.bg_color = (255, 174, 215)