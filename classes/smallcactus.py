import random
from classes.obstacle import Obstacle

class SmallCactus(Obstacle):
    def __init__(self, image, SCREEN_WIDTH, game_speed, obstacles):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type, SCREEN_WIDTH, game_speed, obstacles)
        self.rect.y = 325