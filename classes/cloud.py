import random

class Cloud:
    def __init__(self, SCREEN_WIDTH, CLOUD, game_speed):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.CLOUD = CLOUD
        self.game_speed = game_speed

    # Funkce na updatování mraků každý loop
    def update(self):
        self.x -= self.game_speed
        # Když mrak dojede doleva, resetuje se
        if self.x < -self.width:
            self.x = self.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    # Funkce na vykreslení
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
