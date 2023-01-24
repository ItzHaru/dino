class Obstacle:
    def __init__(self, image, type, SCREEN_WIDTH, game_speed, obstacles):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.game_speed = game_speed
        self.obstacles = obstacles

    # Funkce na updatování pěkážek
    def update(self):
        self.rect.x -= self.game_speed
        # Když překážka dojde doleva, zmizí
        if self.rect.x < -self.rect.width:
            self.obstacles.pop()

    # Funkce na vykreslení překážek
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)
