import pygame
import sys



class Settings:
    
    def __init__(self):
        
        
        #ship settings
        self.ship_speed = 5
        self.ship_startx = 100
        self.ship_starty = 100
        self.ship_limit = 4
        
        
        #screen settings
        self.screen_info = pygame.display.Info()
        self.sw = self.screen_info.current_w
        self.sh = self.screen_info.current_h - 50
        
        #self.screen = pygame.display.set_mode((self.sw,self.sh), pygame.RESIZABLE)
        self.bgcolor = (255, 174, 215)
        
        #bullet settings
        self.bulletWidth = 2
        self.bulletHeight = 15
        self.bulletColor = (0,0,0)
        self.fire_rate = 300
        
        #level
        self.level = 1
        
        
        
        
        
    
    
        
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        #alien settings
        #direction 1 rep right -1 represents left
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        self.alien_speed = 2.0
        self.redA_points = 50
        self.highscore = 0
        
        #bullet settings
        self.bulletSpeed = 2
        
        #score settings
        
        self.score = 0
        
       
        
    def increase_speed(self):
        #level up
        self.ship_speed *= 1.1
        self.bulletSpeed *= 1.1
        self.alien_speed *= 1.5
        
        #score increase
        self.redA_points = int(self.redA_points * 1.5)
    
    def score_increase(self):
        self.score += self.redA_points #yes this works
        
    def bonus_firerate(self):
        self.fire_rate * 1.5
        
        
        
        
        
        
        