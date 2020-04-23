import pygame, sys, random


# init program
pygame.init()
clock = pygame.time.Clock()
screen_x = 1200
screen_mid_x = round(screen_x/2)
screen_y = 800
screen_mid_y = round(screen_y/2)
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Python Pong")
bg_color = pygame.Color('grey12')
obj_color = (200,200,200)


# init objects
ball_size = (30,30)
ball_pos = (round(screen_mid_x - ball_size[0]/2), round(screen_mid_y - ball_size[0]/2))
ball = pygame.Rect(ball_pos, ball_size)
collision_on = True
paddle_size = (10,140)
player_pos = (round(screen_x - (paddle_size[0] + 20)), round(screen_mid_y - paddle_size[1]/2))
player = pygame.Rect(player_pos, paddle_size)
player_speed = 0
opponent_pos = (20, round(screen_mid_y - paddle_size[1]/2))
opponent = pygame.Rect(opponent_pos, paddle_size)
# can modify opponent_speed for difficulty level
opponent_speed = 5


# classes
class ball_speed():
    def __init__(self, x, y):
        self.x = x
        self.y = y
ball_speed = ball_speed(7 * random.choice((1,-1)), 7 * random.choice((1,-1)))


# functions
def ball_animation():
    global collision_on
    ball.x += ball_speed.x
    ball.y += ball_speed.y
    if ball.top <= 0 or ball.bottom >= screen_y:
        ball_speed.y *= -1
    if ball.left <= 0:
        print('player scored!')
        ball_reset()
    if ball.right >= screen_x:
        print('opponent scored!')
        ball_reset()
    if (ball.colliderect(player) or ball.colliderect(opponent)) and collision_on:
        ball_speed.x *= -1
        collision_on = False
    elif ball.colliderect(player) == False and ball.colliderect(opponent) == False:
        collision_on = True

def ball_reset():
    ball.center = (screen_mid_x, screen_mid_y)
    ball_speed.x *= random.choice((1,-1))
    ball_speed.y *= random.choice((1,-1))

def player_animation():
    # player_speed & screen_y do not need to be global because I am not writing to them only reading
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_y:
        player.bottom = screen_y

def opponent_animation():
    if opponent.top > ball.y:
        opponent.top -= opponent_speed
    else: opponent.top += opponent_speed
    if opponent.bottom < ball.y:
        opponent.top += opponent_speed
    else: opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_y:
        opponent.bottom = screen_y
    opponent.y += opponent_speed

def screen_update():
    # draw order matters. First is in background last is on top.
    screen.fill(bg_color)
    pygame.draw.aaline(screen, obj_color, (screen_mid_x,0), (screen_mid_x,screen_y))
    # pygame.draw.Rect(surface, color, rect)
    pygame.draw.rect(screen, obj_color, player)
    pygame.draw.rect(screen, obj_color, opponent)
    pygame.draw.ellipse(screen, obj_color, ball)
    pygame.display.flip()


def event_handler(event):
    global player_speed
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player_speed -= 7
        if event.key == pygame.K_DOWN:
            player_speed += 7
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            player_speed += 7
        if event.key == pygame.K_DOWN:
            player_speed -= 7


# Main Loop
while True:

    # event handler
    for event in pygame.event.get():
        event_handler(event)

    # update animations
    ball_animation()
    player_animation()
    opponent_animation()

    # screen update
    screen_update()

    # frames per second
    clock.tick(60)
