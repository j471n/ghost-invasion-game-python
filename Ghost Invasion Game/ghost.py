import pygame
from pygame.sprite import Sprite

class Ghost(Sprite):
    # """A class to represent a single ghost in the fleet."""

    def __init__(self, ai_game):
        # """Initialize the ghost and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the ghost image and set its rect attribute.
        self.image = pygame.image.load('images/ghost.png')
        self.rect = self.image.get_rect()
        # Start each new ghost near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the ghost's exact horizontal position.
        self.x = float(self.rect.x)
    
    def update(self):
        # """Move the ghost to the right."""
        self.x += self.settings.ghost_speed
        self.rect.x = self.x