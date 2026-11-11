import pygame
import time
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
CAR_WIDTH = 73

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
BLOCK_COLOR = (53, 115, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()

car_img = pygame.image.load("racecar.png")
game_icon = pygame.image.load("racecar.png")
crash_sound = pygame.mixer.Sound("crash.wav")

pygame.display.set_icon(game_icon)

# TODO: Write a function called obstacles_dodged that displays the score.

def obstacles(obstaclex, obstacley, obstaclew, obstacleh, color):
    pygame.draw.rect(window, color, [obstaclex, obstacley, obstaclew, obstacleh])


def car(x, y):
    window.blit(car_img, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def crash():
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################

    # TODO: Make a crash screen that is VERY similar to the intro screen.
    # It should display a crash message and buttons for playing or quitting.
    # Again, optionally you can implement three levels.


def button(msg, x, y, width, height, inactive_color, active_color, action=None):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x + width > mouse_x > x) and (y + height > mouse_y > y):
        pygame.draw.rect(window, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(window, inactive_color, (x, y, width, height))

    small_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    window.blit(text_surf, text_rect)


def quit_game():
    pygame.quit()
    quit()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill(WHITE)
        large_text = pygame.font.SysFont("comicsansms", 115)
        text_surf, text_rect = text_objects("A bit Racey", large_text)
        text_rect.center = ((WIDTH / 2), (HEIGHT / 2))
        window.blit(text_surf, text_rect)

        button("GO!", 150, 450, 100, 50, GREEN, BRIGHT_GREEN, game_loop)
        button("Quit", 550, 450, 100, 50, RED, BRIGHT_RED, quit_game)
        # TODO (Optional): You may implement three different difficulty levels.
        # For example, level 1 is the default start speed and incrementing by 1.
        # Levels 2 and 3 would have a higher start speed and larger increments.

        pygame.display.update()
        clock.tick(15)


def game_loop():
    pygame.mixer.music.load("jazz.mp3")
    pygame.mixer.music.play(-1)
    
    car_x = (WIDTH * 0.45)
    car_y = (HEIGHT * 0.8)

    x_change = 0

    obstacle_startx = random.randrange(0, WIDTH)
    obstacle_starty = -600
    obstacle_speed = 4
    # TODO (Optional): You may choose to have different obstacle speeds for each level.
    obstacle_width = 100
    obstacle_height = 100

    # TODO: Make a variable to track the score (i.e., how many obstacles were dodged).

    game_exit = False
    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                    x_change = 0

        car_x += x_change
        window.fill(WHITE)

        obstacles(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height, BLOCK_COLOR)

        obstacle_starty += obstacle_speed
        car(car_x, car_y)
        
        # TODO: Call the obstacles_dodged function with the correct argument.

        if (car_x > WIDTH - CAR_WIDTH) or (car_x < 0): # if the car hits the left or right wall, it crashes.
            crash()

        if obstacle_starty > HEIGHT:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(0, WIDTH)

            # TODO: Increment the score variable.

            obstacle_speed += 1

            # TODO (optional): Increment the obstacle speed at a faster rate for levels 2 and 3.
            # obstacle_width += (dodged * 1.2)

        # check if the car crashes into an obstacle
        if car_y < obstacle_starty + obstacle_height: 
            print("y crossover")

            if (car_x > obstacle_startx and car_x < obstacle_startx + obstacle_width) or (car_x + CAR_WIDTH > obstacle_startx and car_x + CAR_WIDTH < obstacle_startx + obstacle_width):
                print("x crossover")
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
