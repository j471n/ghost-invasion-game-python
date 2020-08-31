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

        # Bullets Settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # 60, 60, 60
        self.bullets_allowed = 20         #20 bullets allowed at a position

        # ghost settings
        self.ghost_speed = 2.0