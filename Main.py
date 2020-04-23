import pygame, sys


# init program
pygame.init()
clock = pygame.time.Clock()
screen_x = 1200
screen_mid_x = screen_x/2
screen_y = 800
screen_mid_y = screen_y/2
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Python Pong")
running = True


# init objects
bg_color = pygame.Color('grey12')
obj_color = (200,200,200)
ball_size = (30,30)
ball_pos = (screen_mid_x - ball_size[0]/2, screen_mid_y - ball_size[0]/2)
ball = pygame.Rect(ball_pos, ball_size)
paddle_size = (10,140)
player_pos = (screen_x - (paddle_size[0] + 20), screen_mid_y - paddle_size[1]/2)
player = pygame.Rect(player_pos, paddle_size)
opponent_pos = (20, screen_mid_y - paddle_size[1]/2)
opponent = pygame.Rect(opponent_pos, paddle_size)


# classes
ball_speed_x = 7
ball_speed_y = 7


# functions
def ball_physics():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_y:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_x:
        ball_speed_x *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def screen_update():
    # draw order matters. First is in background last is on top.
    screen.fill(bg_color)
    pygame.draw.aaline(screen, obj_color, (screen_mid_x,0), (screen_mid_x,screen_y))
    # pygame.draw.Rect(surface, color, rect)
    pygame.draw.rect(screen, obj_color, player)
    pygame.draw.rect(screen, obj_color, opponent)
    pygame.draw.ellipse(screen, obj_color, ball)
    pygame.display.flip()


# Main Loop
while running:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # object updates
    ball_physics()


    # screen update
    screen_update()


    # frames per second
    clock.tick(60)
