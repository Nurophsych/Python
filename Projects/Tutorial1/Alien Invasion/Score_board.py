import pygame.font
from pygame.sprite import Group
from Ship import Ship
class Scoreboard:
    
    def __init__(self, ai_game):
        self.stats = ai_game.stats
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_ships()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        
        
    def prep_score(self):
        #turn or score into an image onscreen
        rounded = int(self.settings.score)
        score_str = f'{rounded}'
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bgcolor)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.hs_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        
    def prep_high_score(self):
        
        high_score = int(self.settings.highscore)
        highscore_str = f"{high_score}"   
        self.high_score_image = self.font.render(highscore_str, True, self.text_color, self.settings.bgcolor)
        
        self.hs_rect = self.high_score_image.get_rect()
        self.hs_rect.centerx = self.screen_rect.centerx
        self.hs_rect.top = self.score_rect.top
        
    def check_high_score(self):
        if self.settings.score > self.settings.highscore:
            self.settings.highscore = self.settings.score
            self.prep_high_score()
            
    def prep_level(self):
        level_str = str(self.settings.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bgcolor)
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(ship.frames[0], (ship.width -100, ship.height -100))
            ship.rect.x = 10 + ship_number * ship.rect.width 
            ship.rect.y = 10
            self.ships.add(ship)
