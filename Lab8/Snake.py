import pygame, random, sys, time
pygame.init()

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 25  
VELOCITY = 12 

BG_COLOR = (40, 40, 40)
SNAKE_COLOR = (0, 180, 180)
FOOD_COLOR = (180, 0, 0)
TEXT_COLOR = (255, 255, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.Font(None, 36)

def render_text(content, x, y, color=TEXT_COLOR):
    text_surface = font.render(content, True, color)
    screen.blit(text_surface, (x, y))

def create_food(snake_body):
    while True:
        x = random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE
        y = random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE
        if (x, y) not in snake_body:
            return x, y

def render_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], TILE_SIZE, TILE_SIZE))

def render_food(food_pos):
    pygame.draw.rect(screen, FOOD_COLOR, (food_pos[0], food_pos[1], TILE_SIZE, TILE_SIZE))

def start_game():
    snake = [(150, 150), (125, 150), (100, 150)]
    direction = "RIGHT"
    food = create_food(snake)
    points = 0
    level = 1
    speed = VELOCITY

    clock = pygame.time.Clock()
    active = True

    while active:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        head_x, head_y = snake[0]
        if direction == "UP":
            head_y -= TILE_SIZE
        elif direction == "DOWN":
            head_y += TILE_SIZE
        elif direction == "LEFT":
            head_x -= TILE_SIZE
        elif direction == "RIGHT":
            head_x += TILE_SIZE

        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            active = False
        if (head_x, head_y) in snake:
            active = False

        snake.insert(0, (head_x, head_y))

        if (head_x, head_y) == food:
            points += 1
            food = create_food(snake)
            if points % 3 == 0:
                level += 1
                speed += 2
        else:
            snake.pop()

        render_snake(snake)
        render_food(food)
        render_text(f"Score: {points}", 20, 20)
        render_text(f"Level: {level}", 650, 20)

        pygame.display.update()
        clock.tick(speed)

    screen.fill(BG_COLOR)
    render_text("Game Over!", WIDTH // 2 - 80, HEIGHT // 2 - 20, FOOD_COLOR)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

start_game()
