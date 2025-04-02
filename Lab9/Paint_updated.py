import pygame

# Define Color Palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Drawing Functions
def drawLineBetween(window, start_pos, end_pos, thickness, draw_color):
    dx = start_pos[0] - end_pos[0]
    dy = start_pos[1] - end_pos[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = i / iterations
        inverse_progress = 1 - progress
        x = int(inverse_progress * start_pos[0] + progress * end_pos[0])
        y = int(inverse_progress * start_pos[1] + progress * end_pos[1])
        pygame.draw.circle(window, draw_color, (x, y), thickness)

def drawRectangle(window, position, width, height, color):
    x, y = position
    pygame.draw.rect(window, color, (x, y, width, height), 3)

def drawCircle(window, position, color, radius):
    x, y = position
    pygame.draw.circle(window, color, (x, y), radius, 3)

def drawSquare(window, position, color, size):
    x, y = position
    pygame.draw.rect(window, color, (x, y, size, size), 3)

def drawRightTriangle(window, position, color, size):
    x, y = position
    pygame.draw.polygon(window, color, [(x, y), (x + size, y), (x, y + size)], 3)

def drawEquilateralTriangle(window, position, color, size):
    x, y = position
    height = size * (3 ** 0.5) / 2
    pygame.draw.polygon(window, color, [(x, y), (x + size, y), (x + size / 2, y - height)], 3)

def drawRhombus(window, position, color, size):
    x, y = position
    w, h = size, size * 1.2
    points = [
        (x, y - h // 2),
        (x + w // 2, y),
        (x, y + h // 2),
        (x - w // 2, y)
    ]
    pygame.draw.polygon(window, color, points, 3)

# Main Function
def main():
    pygame.init()
    canvas = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    game_clock = pygame.time.Clock()

    # Initialize the screen with black background
    canvas.fill(BLACK)
    brush_radius = 10
    active_color = WHITE
    shape_dimension = 100
    previous_position = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            
            if event.type == pygame.KEYDOWN:
                # Change color based on key press
                if event.key == pygame.K_r:
                    active_color = RED
                elif event.key == pygame.K_g:
                    active_color = GREEN
                elif event.key == pygame.K_b:
                    active_color = BLUE
                elif event.key == pygame.K_y:
                    active_color = YELLOW
                elif event.key == pygame.K_BACKSPACE:
                    active_color = BLACK

                # Draw shapes based on key press
                elif event.key == pygame.K_l:
                    drawRectangle(canvas, pygame.mouse.get_pos(), shape_dimension * 2, shape_dimension, active_color)
                elif event.key == pygame.K_c:
                    drawCircle(canvas, pygame.mouse.get_pos(), active_color, shape_dimension)
                elif event.key == pygame.K_s:
                    drawSquare(canvas, pygame.mouse.get_pos(), active_color, shape_dimension)
                elif event.key == pygame.K_t:
                    drawRightTriangle(canvas, pygame.mouse.get_pos(), active_color, shape_dimension)
                elif event.key == pygame.K_e:
                    drawEquilateralTriangle(canvas, pygame.mouse.get_pos(), active_color, shape_dimension)
                elif event.key == pygame.K_h:
                    drawRhombus(canvas, pygame.mouse.get_pos(), active_color, shape_dimension)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                previous_position = pygame.mouse.get_pos()

            elif event.type == pygame.MOUSEMOTION and event.buttons[0] and previous_position:
                drawLineBetween(canvas, previous_position, pygame.mouse.get_pos(), brush_radius, active_color)
                previous_position = pygame.mouse.get_pos()

        pygame.display.flip()
        game_clock.tick(60)

    pygame.quit()

# Run the main function
main()
