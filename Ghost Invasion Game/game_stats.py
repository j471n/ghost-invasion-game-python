class GameStats:
    # """Track statistics for Ghost Invasion."""

    def __init__(self, ai_game):
        # """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start ghost Invasion in an active state.
        self.game_active = True


#----------------------------reset_stats()-------------------------------

    def reset_stats(self):
        # """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit