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
game_font = pygame.font.Font("freesansbold.ttf", 24)


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
opponent_speed = 7
volly_count = 0
# 0 - AI doesnt move
# 3 - easy
# 10 - Impossible
difficulty = 3


# classes
class ball_speed():
    def __init__(self, x, y):
        self.x = x
        self.y = y
ball_speed = ball_speed(7 * random.choice((1,-1)), 7 * random.choice((1,-1)))

class score():
    def __init__(self, opponent, player):
        self.opponent = opponent
        self.player = player
score = score(0, 0)


# functions
def ball_animation():
    global collision_on, volly_count, opponent_speed
    ball.x += ball_speed.x
    ball.y += ball_speed.y
    if ball.top <= 0 or ball.bottom >= screen_y:
        ball_speed.y *= -1
    if ball.left <= 0:
        score.player += 1
        ball_reset()
    if ball.right >= screen_x:
        score.opponent += 1
        ball_reset()
    if (ball.colliderect(player) or ball.colliderect(opponent)) and collision_on:
        ball_speed.x *= -1
        if (player_speed > 0 and ball_speed.y < 0) or (player_speed < 0 and ball_speed.y > 0):
            ball_speed.y *= -1
        collision_on = False
        volly_count += 1
        if volly_count >= 2:
            volly_count = 0
            opponent_speed += 1
            if ball_speed.x >= 0:
                ball_speed.x += 1
            else: ball_speed.x -= 1
            if ball_speed.y >= 0:
                ball_speed.y += 1
            else: ball_speed.y -= 1
    elif ball.colliderect(player) == False and ball.colliderect(opponent) == False:
        collision_on = True

def ball_reset():
    global volly_count, ball_speed, opponent_speed
    volly_count = 0
    opponent_speed = 7
    ball.center = (screen_mid_x, screen_mid_y)
    ball_speed.x = 7 * random.choice((1,-1))
    ball_speed.y = 7 * random.choice((1,-1))

def player_animation():
    # player_speed & screen_y do not need to be global because I am not writing to them only reading
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_y:
        player.bottom = screen_y

def opponent_AI():
    # AI difficulty?????
    AI_choice = random.randint(1,10)
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
    player_score = game_font.render(f"{score.player}", False, obj_color)
    screen.blit(player_score, (screen_mid_x + 20, screen_mid_y))
    opponent_score = game_font.render(f"{score.opponent}", False, obj_color)
    screen.blit(opponent_score, (screen_mid_x - opponent_score.get_rect().width - 20, screen_mid_y))
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
    opponent_AI()

    # screen update
    screen_update()

    # frames per second
    clock.tick(60)
