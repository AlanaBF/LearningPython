import pygame
import colorsys

pygame.init()

width = 400
height = 300
windowSize = [width, height]
screen = pygame.display.set_mode(windowSize)

num_colors = 100
colors = []

for i in range(num_colors):
    hue = i / num_colors
    rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
    scaled_color = [int(c * 255) for c in rgb_color]
    colors.append(scaled_color)

row = 0
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    color_index = 0

    while row <= height:
        color = colors[color_index % num_colors]
        pygame.draw.rect(screen, tuple(color), (0, row, width, row + 3))
        row += 3
        color_index += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

