import pygame
import random

RED = (255, 0, 0)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)  # eraser

pygame.display.set_caption("Paint Program")  

def main():
    pygame.init() 
    canvas = pygame.display.set_mode((800, 500))  
    clock = pygame.time.Clock()
    
    brush_size = 15
    color_mode = BLUE
    previous_position = None 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color_mode = RED
                elif event.key == pygame.K_g:
                    color_mode = GREEN
                elif event.key == pygame.K_b:
                    color_mode = BLUE
                elif event.key == pygame.K_a:
                    color_mode = CYAN
                elif event.key == pygame.K_LSHIFT:
                    color_mode = BLACK
                elif event.key == pygame.K_l:
                    draw_rectangle(canvas, pygame.mouse.get_pos(), 200, 100, color_mode)
                elif event.key == pygame.K_c:
                    draw_circle(canvas, pygame.mouse.get_pos(), color_mode)
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                previous_position = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0] and previous_position:
                draw_line(canvas, previous_position, pygame.mouse.get_pos(), brush_size, color_mode)
                previous_position = pygame.mouse.get_pos()
                
        pygame.display.flip()
        clock.tick(60)

def draw_line(canvas, start, end, width, color):
    xaxis = start[0] - end[0]
    yaxis = start[1] - end[1]
    iterations = max(abs(xaxis), abs(yaxis))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        inverse_progress = 1 - progress
        x = int(inverse_progress * start[0] + progress * end[0])
        y = int(inverse_progress * start[1] + progress * end[1])
        pygame.draw.circle(canvas, color, (x, y), width)

def draw_rectangle(canvas, position, width, height, color):
    x, y = position
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(canvas, color, rect, 3)

def draw_circle(canvas, position, color):
    x, y = position
    pygame.draw.circle(canvas, color, (x, y), 100, 3)

main()
