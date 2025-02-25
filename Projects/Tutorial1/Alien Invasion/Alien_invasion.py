import sys
import pygame
from settings import Settings  
from Game_stats import GameStats 
from Button import Button
from Ship import Ship
from Bullet import Bullet
from Alien import Alien
from Score_board import Scoreboard
from time import sleep


class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #call settings 
        self.settings.initialize_dynamic_settings()
        self.screen = pygame.display.set_mode(
            (self.settings.sw, self.settings.sh))
        #caption
        pygame.display.set_caption("Alien Invasion")
        #init sprites
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.ship = Ship(self)
        #init stats
        self.stats = GameStats(self)
        #set a timer for game
        self.clock = pygame.time.Clock()
        #fire rate
        self.last_shot_time = 0
        self.fire_rate = self.settings.fire_rate
        #game state
        self.game_active = False
        #playbutton
        self.play_button = Button(self, "Play")
        #score
        self.sb = Scoreboard(self)
        
        
        #calls
        
        
        
    def _update_bullets(self):
        self.bullets.update()
        self._check_bullet_alien_collisions()
        
    def _ship_hit(self):
        
        if self.stats.ships_left > 1:
            
        #Reduce by increment of 1
            
            self.stats.ships_left -= 1
            print(self.stats.ships_left)
            self.sb.prep_ships()
            

        
        #trash all bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
        
        #reset
            self._create_fleet()
            self.ship.center_ship()
        
            sleep(0.5)
        
             
        elif self.stats.ships_left <= 1:
            self.ship.kill()
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.game_active = False #this
            pygame.mouse.set_visible(True)
        
        
    def _check_bullet_alien_collisions(self):
           
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.settings.score += self.settings.redA_points * len(aliens)
            self.settings.score_increase()
            self.sb.prep_score()
            self.sb.prep_high_score()
        
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                bullet.kill()
        if not self.aliens:
            self.bullets.empty()
            self.settings.increase_speed()
            self._create_fleet()
            
            self.settings.level += 1
            self.sb.prep_level()
            if self.settings.level % 2 == 0:
                self.settings.bonus_firerate()
                
    def _update_aliens(self):
        #update all pos of aliens
        self._check_fleet_edges()
        self.aliens.update()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
        
        
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.sh:
                self._ship_hit()
                break
            
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
        
    def main_loop(self):
        running = True
        while running:
            
            
            
            if self.game_active:
                self.bullets.update()
                self._update_aliens()
                self._update_bullets()
                
            
            self._update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos) #this!!!!!!!!!!!!!
            if self.game_active:       
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and self.ship.x2 > 0:
                    self.ship.x2 -= self.settings.ship_speed  # Move left
                if keys[pygame.K_RIGHT] and self.ship.x2 < self.settings.sw - self.ship.width:
                    self.ship.x2 += self.settings.ship_speed  # Move right
                if keys[pygame.K_SPACE]:
                    self.fire_bullet()
                elif keys[pygame.K_q]:
                    sys.exit()
            
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.stats.ships_left = self.settings.ship_limit
            self.stats.score = 0
            self.stats.level = 1
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.sb.check_high_score()

            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()

            self.game_active = True
            pygame.mouse.set_visible(False)
        
    
    def fire_bullet(self):
        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.fire_rate:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.last_shot_time = current_time  # Update the time of the last shot
            
    def _create_fleet(self):
        #make die alien
        alien = Alien(self)
        alien_width = alien.rect.width - 40
        alien_height = alien.rect.height - 20
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.sh - 3 * alien_height):
            while current_x < (self.settings.sw - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
        
        
            #reset x and y after a row
            current_x = alien_width
            current_y += 2 * alien_height
        
            
            
            
    def _create_alien(self, x_position, y_position):        
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
           
    def _update_screen(self):
        self.screen.fill(self.settings.bgcolor) 
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
                
        self.ship.update()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        
        
        if not self.game_active:
            self.play_button.draw_button()

        
        pygame.display.flip()  # Update display
            
        self.clock.tick(60) 
             
                    
    pygame.quit()  # Ensure proper cleanup when exiting
        
     
        
            
if __name__ == '__main__':
    # Make instance and start
    ai = AlienInvasion()
    ai.main_loop()



