print("\033c")

import pygame

pygame.init()

display_title = "Add Elements to My Screen"
display_size = (500, 500)
display_color = (0, 0, 0)
display = pygame.display.set_mode(display_size)

rect_left = 30
rect_top = 30
rect_width = 205
rect_height = 205
rect_color = (255, 0, 100)
rect = pygame.Rect(rect_left, rect_top, rect_width, rect_height)

circle1_radius = 102.5
circle1_center = (367.5, 132.5)
circle1_color = (0, 255, 100)

circle2_radius = 102.5
circle2_width = 30
circle2_center = (132.5, 367.5)
circle2_color = (0, 100, 255)

polygon_color = (255, 255, 0)
polygon_points = [(367.5, 265), (265, 470), (470, 470)]

clock_framerate = 60
clock = pygame.time.Clock()

running = True

display.fill(display_color)
pygame.display.set_caption(display_title)
pygame.draw.rect(display, rect_color, rect)
pygame.draw.circle(display, circle1_color, circle1_center, circle1_radius)
pygame.draw.circle(display, circle2_color, circle2_center, circle2_radius, circle2_width)
pygame.draw.polygon(display, polygon_color, polygon_points)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(clock_framerate)

pygame.quit()