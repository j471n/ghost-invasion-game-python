class Settings:

    #A class to store all settings for Ghost Invasion.

    def __init__(self):
        #"""Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (225, 225, 225)  #white

        # Ship settings
        self.ship_speed = 2.0