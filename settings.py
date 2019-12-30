class Settings:

  def __init__(self):
    """Initialize the game's static settings"""
    self.screen_width = 2560
    self.screen_height = 1080
    self.bg_color = (0, 0, 0)

    #ship settings
    self.ship_speed = 1.5
    self.ship_limit = 3

    # bullet settings
    self.bullet_speed = 3
    self.bullet_width = 10
    self.bullet_height = 25
    self.bullet_color = (241, 7, 7)

    # alien settings
    self.alien_speed = 1.5
    self.fleet_drop_speed = 10.0
    # fleet_direction of 1 represents right; -1 represents left
    self.fleet_direction = 1

    #how quickly the game speeds up
    self.speedup_scale = 1.1

    self.initialize_dynamic_settings()

  def initialize_dynamic_settings(self):
    """Initialize settings that change through the game"""
    self.ship_speed = 2.0
    self.bullet_speed = 3.0
    self.alien_speed = 2.2
    #scoring
    self.alien_points = 50

    self.fleet_direction = 1

  def increase_speed(self):
    """Increase speed settins"""
    self.ship_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale