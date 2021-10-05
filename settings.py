class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1
        self.ship_left = 3

        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 3

        self.alien_speed = 1
        self.alien_drop_speed = 10
        self.alien_direction = 1