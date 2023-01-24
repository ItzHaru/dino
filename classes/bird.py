from classes.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image, SCREEN_WIDTH, game_speed, obstacles):
        self.type = 0
        super().__init__(image, self.type, SCREEN_WIDTH, game_speed, obstacles)
        self.rect.y = 250
        self.index = 0

    # Funkce na vykreslení
    def draw(self, SCREEN):
        # Animace ptáka
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1