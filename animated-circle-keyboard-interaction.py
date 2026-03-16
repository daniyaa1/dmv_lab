import pygame

# initialize pygame
pygame.init()

# window size
width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")

# circle properties
x = width // 2
y = height // 2
radius = 30
speed = 5

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard interaction
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # background
    screen.fill((255, 255, 255))

    # draw circle
    pygame.draw.circle(screen, (173, 216, 230), (x, y), radius)

    pygame.display.update()

    clock.tick(60)

pygame.quit()