import pygame, random, sys, time
import psycopg2
from config import load_config
from connect import connect

pygame.init()

# Screen & Game Settings
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
START_SPEED = 10

# Colors
BG_COLOR = (20, 20, 20)
SNAKE_COLOR = (143, 0, 255)
FOOD_COLOR_1 = (255, 0, 0)
FOOD_COLOR_2 = (0, 255, 0)
FOOD_COLOR_3 = (0, 0, 255)
TEXT_COLOR = (255, 255, 255)

# Initialize Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font('font/Pixeltype.ttf', 40)
clock = pygame.time.Clock()

# Connect to DB
config = load_config()
conn = connect(config)
cursor = conn.cursor()

def display_text(text, x, y, color=TEXT_COLOR):
    screen.blit(font.render(text, True, color), (x, y))

def create_food(snake_body):
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

def get_or_create_user(username):
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
        cursor.execute("SELECT level, score FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
        state = cursor.fetchone()
        return user_id, (state if state else (1, 0))
    else:
        cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cursor.fetchone()[0]
        conn.commit()
        return user_id, (1, 0)

def save_game_state(user_id, score, level):
    cursor.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()

def run_game():
    username = input("Enter your username: ")
    user_id, (saved_level, saved_score) = get_or_create_user(username)

    # Working game state starts from saved state
    level = saved_level
    score = saved_score
    speed = START_SPEED + (level - 1) * 2

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    food = create_food(snake)
    running = True
    saved = False

    while running:
        screen.fill(BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_p:
                    save_game_state(user_id, score, level)
                    display_text("Game Paused. Saved.", WIDTH // 3, HEIGHT // 2)
                    pygame.display.update()
                    time.sleep(1)
                    saved = True

        head_x, head_y = snake[0]
        if direction == "UP": head_y -= GRID_SIZE
        elif direction == "DOWN": head_y += GRID_SIZE
        elif direction == "LEFT": head_x -= GRID_SIZE
        elif direction == "RIGHT": head_x += GRID_SIZE

        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or (head_x, head_y) in snake):
            running = False
            break

        snake.insert(0, (head_x, head_y))

        if (head_x, head_y) == food['position']:
            score += food['points']
            food = create_food(snake)
            if score % 5 == 0:
                level += 1
                speed += 2
        else:
            snake.pop()

        if time.time() - food['timestamp'] > 5:
            food = create_food(snake)

        draw_snake(snake)
        draw_food(food)
        display_text(f"Score: {score}", 10, 10)
        display_text(f"Level: {level}", WIDTH - 120, 10)

        pygame.display.update()
        clock.tick(speed)

    screen.fill(BG_COLOR)
    display_text("Game Over!", WIDTH // 2 - 50, HEIGHT // 2, FOOD_COLOR_1)
    pygame.display.update()
    time.sleep(2)

    # Save only if player pressed P
    if saved:
        save_game_state(user_id, score, level)

    pygame.quit()
    sys.exit()

run_game()
