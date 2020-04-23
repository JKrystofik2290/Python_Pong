import pygame, sys

# init
pygame.init()
clock = pygame.time.Clock()
screen_x = 1280
screen_y = 960
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Python Pong")
running = True
# pygame.Rect(left, top, x, y)
ball = pygame.Rect(screen_x/2 - 15, screen_y/2 - 15, 30, 30)
player = pygame.Rect(screen_x - 20, screen_y/2 - 70, 10, 140)
opponent = pygame.Rect(20, screen_y/2 - 70, 10, 140)


# Main Loop
while running:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pygame.draw.Rect(surface, color, rect)
    pygame.draw.Rect(screen,(200,200,200), player)





    # screen update
    pygame.display.flip()
    clock.tick(60)
