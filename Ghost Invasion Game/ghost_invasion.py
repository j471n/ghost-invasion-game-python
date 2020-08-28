import sys      #importing sys
import pygame   #importing pygame
from settings import Settings       #importing settings class
from ship import Ship               #importing Ship class
from bullet import Bullet           #importing Bullet class


class GhostInvasion:
    #"""Overall class to manage game assets and behavior."""

    def __init__(self):
        #Initialize the game, and create game resources.
        pygame.init()
        self.settings = Settings()

        #1200px wide and 800px high is known as surface "display.set_mode() represents the entire game window."
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # # for run game in fullscreen>>>>>>>>>>>>
        """if you want to use fullscreen mode then remove below 3 comments and make upper exp. as comment"""
        # self.screen  = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        #Caption or title which will display on the top
        pygame.display.set_caption("Ghost Invasion")

        #Ship Class
        self.ship = Ship(self)
        # Storing Bullets in a Group
        self.bullets = pygame.sprite.Group()





#***************************run_game()********************************

#game is controlled by the run_game() method
    def run_game(self):
        #"""Start the main loop for the game."""

        while True:

            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                print(len(self.bullets))
                
            self._update_screen()

            # Redraw the screen during each pass through the loop to fill the screen with color
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()      #Drawing ship on the game screen

            # It continually updates the display to show the new positions of game
            pygame.display.flip()

#*************************** _check_events()********************************

    def _check_events(self):
        # """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                #when release the key
                self._check_keyup_events(event)



#*************************** _check_keydown_events()********************************

    def _check_keydown_events(self, event):

        # """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right. while press the key
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()      #if user press Q then exit from the screen
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()         #spacebar for firing bullets


#*************************** _fire_bullet()********************************

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        #checking if user input of bullet is allowed the draw bullets
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


#*************************** _check_keyup_events()********************************

    def _check_keyup_events(self, event):

        # """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

#*************************** _update_screen()********************************

    def _update_screen(self):
        # Redraw the screen during each pass through the loop to fill the screen with color
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  #Drawing ship on the game screen

        # Drawing the bullets on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # It continually updates the display to show the new positions of game
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = GhostInvasion()
    ai.run_game()