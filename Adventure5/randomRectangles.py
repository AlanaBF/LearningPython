import random
import pygame

pygame.init()

width = 400
height = 300
windowSize = [width, height]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

sqrW = int(width / 10)  # Convert to integer
sqrH = int(height / 10)  # Convert to integer

done = False
while not done:
    red = random.randrange(0, 256)
    green = random.randrange(0, 256)
    blue = random.randrange(0, 256)

    x = random.randrange(0, width, sqrW)  # Use width - sqrW
    y = random.randrange(0, height, sqrH)  # Use height - sqrH
    pygame.draw.rect(screen, (red, green, blue), (x, y, sqrW, sqrH))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(10)

pygame.quit()
