import sys      #importing sys
import pygame   #importing pygame
from settings import Settings       #importing settings class


class GhostInvasion:
    #"""Overall class to manage game assets and behavior."""

    def __init__(self):
        #Initialize the game, and create game resources.
        pygame.init()
        self.settings = Settings()

        #1200px wide and 800px high is known as surface "display.set_mode() represents the entire game window."

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        #Caption or title which will display on the top
        pygame.display.set_caption("Ghost Invasion")

        
        


#***************************run_game()********************************

#game is controlled by the run_game() method
    def run_game(self):
        #"""Start the main loop for the game."""

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop to fill the screen with color
            self.screen.fill(self.settings.bg_color)

            # It continually updates the display to show the new positions of game
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = GhostInvasion()
    ai.run_game()