import pygame
import random
import os
pygame.mixer.init()
pygame.init()
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
# Creating window
screen_width = 1000
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
#Background Image
bgimg = pygame.image.load("back2.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
bgimg1 = pygame.image.load("1.jpg")
bgimg1= pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()
bgimg2 = pygame.image.load("go.jpg")
bgimg2= pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()
# Game Title
pygame.display.set_caption("Snake it up!")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgimg1, (0, 0))
        text_screen("Press Space Bar To Play", white, 352, 570)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(120)
# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 90
    snake_y = 90
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    food_x = random.randint(70, int(screen_width / 2))
    food_y = random.randint(70, int(screen_height / 2))
    score = 0
    init_velocity = 3
    snake_size = 30
    fps =120
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.blit(bgimg2, (0, 0))
            text_screen("Press Enter To Continue", white, 352, 570)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x)<25 and abs(snake_y - food_y)<25:
                score +=10
                food_x = random.randint(80, int(screen_width / 2))
                food_y = random.randint(80, int(screen_height / 2))
                snk_length +=6
                if score>int(hiscore):
                    hiscore = score
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
            if snake_x<70 or snake_x>screen_width-105 or snake_y<50 or snake_y>screen_height-90:
                game_over = True
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
