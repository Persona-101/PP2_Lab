import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()


clock_face = pygame.image.load("clock.png")
clock_face = pygame.transform.scale(clock_face, (400, 400))
clock_face_rect = clock_face.get_rect(center=(250, 250))


minutes_hand = pygame.image.load("minutes.png")
seconds_hand = pygame.image.load("seconds.png")
minutes_hand = pygame.transform.scale(minutes_hand, (200, 20))
seconds_hand = pygame.transform.scale(seconds_hand, (220, 15))

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = -6 * minutes + 90  
    sec_angle = -6 * seconds + 90  

    rotated_minutes_hand = pygame.transform.rotate(minutes_hand, min_angle)
    rotated_seconds_hand = pygame.transform.rotate(seconds_hand, sec_angle)

    minutes_hand_rect = rotated_minutes_hand.get_rect(center=(250, 250))
    seconds_hand_rect = rotated_seconds_hand.get_rect(center=(250, 250))

    screen.fill("white")
    screen.blit(clock_face, clock_face_rect)
    screen.blit(rotated_minutes_hand, minutes_hand_rect)
    screen.blit(rotated_seconds_hand, seconds_hand_rect)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
