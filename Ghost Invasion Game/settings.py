class Settings:

    #A class to store all settings for Ghost Invasion.

    def __init__(self):
        #"""Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (225, 225, 225)  #white

        # Ship settings
        self.ship_limit = 3

        # Bullets Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # 60, 60, 60
        self.bullets_allowed = 20         #20 bullets allowed at a position


        #fleet dropping speed
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):

        #"""Initialize settings that change throughout the game.""
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.ghost_speed = 2.0
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50


    def increase_speed(self):

        # """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ghost_speed *= self.speedup_scale
