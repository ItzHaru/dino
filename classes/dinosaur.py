import pygame

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self, DUCKING, RUNNING, JUMPING):
        # Nastavení obrázků
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        # Nastavení ať dinosaurus ze začátku běží
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        # Pro animaci
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        # Pro hitboxy
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    # Funkce, která updatuje dinosaura každý while loop
    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        # Resetuje každých 10 kroků
        if self.step_index >= 10:
            self.step_index = 0

        # Když zmáčkneme šipku nahoru a dinosaurus momentálně neskáče, ať začne skákat
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        # Když zmáčkneme šipku dolů a dinosaurus momentálně neskáče, ať se skrčí
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        # Když dinosaurus momentálně neskáče a nemačkáme šipku dolů, ať běží
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    # Funkce na skrčení
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    # Funkce na běh
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    # Funkce na skok
    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    # Funkce na vykreslení
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))