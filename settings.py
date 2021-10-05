class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 3

        self.alien_drop_speed = 5

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed = 1
        self.bullet_speed = 0.5
        self.alien_speed = 0.5
        self.alien_direction = 1
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
