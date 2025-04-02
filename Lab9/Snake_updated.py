import pygame, random, sys, time
pygame.init()

# Screen & Game Settings
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
START_SPEED = 10

# Colors
BG_COLOR = (20, 20, 20)   # Dark Gray
SNAKE_COLOR = (143, 0, 255)  # Violet
FOOD_COLOR_1 = (255, 0, 0)  # Red (1 point)
FOOD_COLOR_2 = (0, 255, 0)  # Green (2 points)
FOOD_COLOR_3 = (0, 0, 255) # Blue (3 points)
TEXT_COLOR = (255, 255, 255)  # White

# Initialize Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font('font/Pixeltype.ttf', 40)
clock = pygame.time.Clock()

def display_text(text, x, y, color=TEXT_COLOR):
    screen.blit(font.render(text, True, color), (x, y))

def create_food(snake_body):   #Ensures the food does not spawn on the snake's body.
    while True:
        food_x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        food_y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        if (food_x, food_y) not in snake_body:
            return {'position': (food_x, food_y), 'points': random.randint(1, 3), 'timestamp': time.time()}

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    color = FOOD_COLOR_1 if food['points'] == 1 else FOOD_COLOR_2 if food['points'] == 2 else FOOD_COLOR_3
    pygame.draw.rect(screen, color, (*food['position'], GRID_SIZE, GRID_SIZE))

def run_game():
    snake = [(100, 100), (80, 100), (60, 100)]  #snake size
    direction = "RIGHT"
    food = create_food(snake)
    score, level, speed = 0, 1, START_SPEED
    running = True

    while running:
        screen.fill(BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        # Move Snake
        head_x, head_y = snake[0]
        if direction == "UP": head_y -= GRID_SIZE
        elif direction == "DOWN": head_y += GRID_SIZE
        elif direction == "LEFT": head_x -= GRID_SIZE
        elif direction == "RIGHT": head_x += GRID_SIZE

        # Collision Detection
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or (head_x, head_y) in snake):
            break  # Game Over
        
        snake.insert(0, (head_x, head_y))

        # Check if food is eaten
        if (head_x, head_y) == food['position']:
            score += food['points']
            food = create_food(snake)
            if score % 5 == 0:
                level += 1
                speed += 2
        else:
            snake.pop()  # Remove tail if no food eaten

        # Remove food if too old (5 sec lifespan)
        if time.time() - food['timestamp'] > 5:
            food = create_food(snake)

        # Draw Everything
        draw_snake(snake)
        draw_food(food)
        display_text(f"Score: {score}", 10, 10)
        display_text(f"Level: {level}", WIDTH - 120, 10)

        pygame.display.update()
        clock.tick(speed)

    # Game Over Screen
    screen.fill(BG_COLOR)
    display_text("Game Over!", WIDTH // 2 - 50, HEIGHT // 2, FOOD_COLOR_1)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

run_game()
