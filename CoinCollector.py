import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Collector Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont('arial', 24)

# Game variables
clock = pygame.time.Clock()
player_size = 50
player_x = screen_width // 2
player_y = screen_height - player_size - 10
player_velocity = 5

coin_size = 30
coin_x = random.randint(0, screen_width - coin_size)
coin_y = random.randint(0, screen_height - coin_size)
coin_collected = 0

# Create the player object (a simple rectangle)
player = pygame.Rect(player_x, player_y, player_size, player_size)

# Create the coin object
coin = pygame.Rect(coin_x, coin_y, coin_size, coin_size)

# Function to draw the player
def draw_player():
    pygame.draw.rect(screen, GREEN, player)

# Function to draw the coin
def draw_coin():
    pygame.draw.rect(screen, RED, coin)

# Function to display the score
def draw_score():
    score_text = font.render(f"Coins: {coin_collected}", True, BLACK)
    screen.blit(score_text, (screen_width - 150, 10))

# Main game loop
running = True
while running:
    clock.tick(30)  # Set FPS to 30
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_velocity
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_size:
        player.x += player_velocity
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= player_velocity
    if keys[pygame.K_DOWN] and player.y < screen_height - player_size:
        player.y += player_velocity

    # Check for collision with the coin
    if player.colliderect(coin):
        coin_x = random.randint(0, screen_width - coin_size)
        coin_y = random.randint(0, screen_height - coin_size)
        coin = pygame.Rect(coin_x, coin_y, coin_size, coin_size)
        coin_collected += 1

    # Draw everything on the screen
    draw_player()
    draw_coin()
    draw_score()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
