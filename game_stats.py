

class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        self.reset_stats()
    
    def reset_stats(self):
        self.ship_left = self.settings.ship_left