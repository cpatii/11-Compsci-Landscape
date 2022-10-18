import pygame
from pygame import K_ESCAPE, KEYDOWN
pygame.init()


width = 1280
height = 720
screensize = (width, height)
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

#  sun and moon variables
sun_y = 100
moon_y = 600
stars_y = moon_y
#  cloud variables
cloud_x = 0
cloud_rgb = (242, 241, 230)


running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    # sky color change
    if moon_y > 350:
        screen.fill((135, 206, 235))
    else:
        screen.fill((22, 27, 54))
    
    # sun and moon movement
    sun_y += 1
    if moon_y != 100:
        moon_y -= 1
        stars_y = moon_y
    cloud_x += 1
    # sun
    pygame.draw.circle(screen, (252, 229, 112), (655, sun_y), 30)
    pygame.draw.circle(screen, (253, 184, 19), (655, sun_y), 40, 10)
    pygame.draw.circle(screen, (253, 102, 0), (655, sun_y), 50, 10)
    # moon
    pygame.draw.circle(screen, (229,229,229), (655, moon_y), 30)
    pygame.draw.circle(screen, (220,220,220), (655, moon_y), 40, 10)
    pygame.draw.circle(screen, (201,201,201), (655, moon_y), 50, 10)
    # grass
    pygame.draw.rect(screen, (86, 125, 90), (0, 300, 1280, 720))
    # road
    pygame.draw.polygon(screen, (92, 92, 92), ((615, 300), (665, 300), (820, 720), (460, 720)))
    # road lanes
    pygame.draw.rect(screen, (207, 178, 35), (637, 660, 6, 50))
    pygame.draw.rect(screen, (207, 178, 35), (637, 580, 6, 50))
    pygame.draw.rect(screen, (207, 178, 35), (637, 500, 6, 50))
    pygame.draw.rect(screen, (207, 178, 35), (637, 420, 6, 50))
    pygame.draw.rect(screen, (207, 178, 35), (637, 340, 6, 50))
    # mountains
    pygame.draw.polygon(screen, (112, 115, 114), ((-30, 300), (100, 100), (220, 300)))
    pygame.draw.polygon(screen, (112, 115, 114), ((80, 300), (280, 70), (400, 300)))
    pygame.draw.polygon(screen, (112, 115, 114), ((320, 300), (420, 100), (615, 300)))
    pygame.draw.polygon(screen, (112, 115, 114), ((540, 300), (680, 220), (780, 300)))
    pygame.draw.polygon(screen, (112, 115, 114), ((700, 300), (880, 150), (980, 300)))
    pygame.draw.polygon(screen, (112, 115, 114), ((900, 300), (1100, 100), (1400, 300)))
    # mountain snow

    # clouds
    def draw_cloud(screen, x, y):
        pygame.draw.circle(screen, (cloud_rgb), (50 + cloud_x + x, 100 + y), 30)
        pygame.draw.circle(screen, (cloud_rgb), (100 + cloud_x + x, 100 + y), 30)
        pygame.draw.circle(screen, (cloud_rgb), (80 + cloud_x + x, 80 + y), 25)
        pygame.draw.circle(screen, (cloud_rgb), (70 + cloud_x + x, 120 + y), 25)
    draw_cloud(screen, 1200, 0)
    draw_cloud(screen, 900, 70)
    draw_cloud(screen, 600, 0)
    draw_cloud(screen, 300, 70)
    draw_cloud(screen, 0, 0)
    draw_cloud(screen, -300, 70)
    draw_cloud(screen, -600, 0)
    draw_cloud(screen, -900, 70)
    draw_cloud(screen, -1200, 0)

    # trees
    def draw_tree(screen, x2, y2):
        pygame.draw.rect(screen, (98,65,51), (100 + x2, 400 + y2, 15, 50))
        pygame.draw.polygon(screen, (20, 51, 6), ((50 + x2, 400 + y2), (166 + x2, 400 + y2), (108 + x2, 360 + y2)))
        pygame.draw.polygon(screen, (20, 51, 6), ((50 + x2, 380 + y2), (166 + x2, 380 + y2), (108 + x2, 340 + y2)))

    draw_tree(screen, -50, -50)
    draw_tree(screen, 50, -50)
    draw_tree(screen, 150, -50)
    draw_tree(screen, 250, -50)
    draw_tree(screen, 350, -50)
    draw_tree(screen, 450, -50)
    draw_tree(screen, -100, 15)
    draw_tree(screen, 0, 15)
    draw_tree(screen, 100, 15)
    draw_tree(screen, 200, 15)
    draw_tree(screen, 300, 15)
    draw_tree(screen, 400, 15)
    draw_tree(screen, -50, 80)
    draw_tree(screen, 50, 80)
    draw_tree(screen, 150, 80)
    draw_tree(screen, 250, 80)
    draw_tree(screen, 350, 80)
    draw_tree(screen, -100, 145)
    draw_tree(screen, 0, 145)
    draw_tree(screen, 100, 145)
    draw_tree(screen, 200, 145)
    draw_tree(screen, 300, 145)
    draw_tree(screen, -50, 210)
    draw_tree(screen, 50, 210)
    draw_tree(screen, 150, 210)
    draw_tree(screen, 250, 210)

    # water
    pygame.draw.circle(screen, (116,204,244), (1100, 500), 100)
    pygame.draw.circle(screen, (116,204,244), (1000, 450), 80)
    pygame.draw.circle(screen, (116,204,244), (1000, 550), 70)
    draw_tree(screen, 800, 210)
    draw_tree(screen, 1100, 210)
    draw_tree(screen, 700, 10)
    draw_tree(screen, 1100, 15)
    draw_tree(screen, 900, -100)
    
        

    
    pygame.display.flip()
    clock.tick(30)
pygame.quit()