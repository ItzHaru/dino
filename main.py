import pygame
import os
import random
from classes.bird import Bird
from classes.cloud import Cloud
from classes.dinosaur import Dinosaur
from classes.largecactus import LargeCactus
from classes.obstacle import Obstacle
from classes.smallcactus import SmallCactus
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur(DUCKING, RUNNING, JUMPING)
    game_speed = 20
    cloud = Cloud(SCREEN_WIDTH, CLOUD, game_speed)
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    # Funkce na skóre
    def score():
        global points, game_speed
        points += 1
        # Každých 100 bodů se hra zrychlí
        if points % 100 == 0:
            game_speed += 1

        # Vypsání skóre
        if points % 900 >= 700:
            text = font.render("Points: " + str(points), True, (255, 255, 255))
        else:
            text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    # Funkce na pozadí - trať
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        # Když dojde na konec trati, vykreslí se hned další
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Vypnutí hry
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Nastevení pozadí
        if points % 900 >= 700:
            SCREEN.fill((0, 0, 0))
        else:
            SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        # Vykreslení dinosaura
        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS, SCREEN_WIDTH, game_speed, obstacles))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS, SCREEN_WIDTH, game_speed, obstacles))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD, SCREEN_WIDTH, game_speed, obstacles))

        # Vykreslení překážek
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            # Kolize dinosaura s překážky
            if player.dino_rect.colliderect(obstacle.rect):
                # Zastaví hru
                pygame.time.delay(2000)
                # Vypíše skóre
                death_count += 1
                menu(death_count)

        # Vykreslení pozadí
        background()

        # Vykreslení mraků
        cloud.draw(SCREEN)
        cloud.update()

        # Vyvolání funkce skóre
        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        # Začátek hry
        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            # Napozicování skóre, kde se vypíše
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            # Vypsání skóre
            SCREEN.blit(score, scoreRect)
        # Napozicování textu
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # Vypsání textu
        SCREEN.blit(text, textRect)
        # Vykreslení dinosaura pro efekt : )
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        # Updatování displeje
        pygame.display.update()
        # Vypnutí hry
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Pro restart je potřeba zmáčknout kteroukoliv klávesnici
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)
