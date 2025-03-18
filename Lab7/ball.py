import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))

pos_x = 150
pos_y = 150
radius = 25
step = 20

flag = True
while flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            flag = False
            pygame.quit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT and pos_x + radius + step <= 300:
                pos_x += step
            elif i.key == pygame.K_LEFT and pos_x - radius - step >= 0:
                pos_x -= step
            elif i.key == pygame.K_UP and pos_y - radius - step >= 0:
                pos_y -= step
            elif i.key == pygame.K_DOWN and pos_y + radius + step <= 300:
                pos_y += step

    screen.fill("white")
    pygame.draw.circle(screen, "red", (pos_x, pos_y), radius)
    pygame.display.update()
