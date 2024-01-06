import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen configuration
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Race")

# Color definitions
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Class definitions
class Car(pygame.sprite.Sprite):
    """Class to represent a car sprite."""
    def __init__(self, color, width, height, x, y):
        """
        Initialize a car sprite.

        Args:
            color (tuple): RGB color tuple (e.g., (255, 0, 0) for red).
            width (int): Width of the car sprite.
            height (int): Height of the car sprite.
            x (int): Initial x-coordinate of the car sprite.
            y (int): Initial y-coordinate of the car sprite.
        """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x_change, y_change):
        """
        Move the car by changing its x and y coordinates.

        Args:
            x_change (int): Change in the x-coordinate.
            y_change (int): Change in the y-coordinate.
        """
        self.rect.x += x_change
        self.rect.y += y_change

# Function to generate random obstacles
def generate_obstacles():
    """
    Generate a group of random obstacles.

    Returns:
        pygame.sprite.Group: Group of obstacle sprites.
    """
    obstacles = pygame.sprite.Group()
    for _ in range(5):
        obstacle = Car(black, 30, 30, random.randrange(width - 30), random.randrange(height - 30))
        obstacles.add(obstacle)
    return obstacles

# Create players and obstacles
player1 = Car(red, 50, 50, 50, height // 2 - 25)
player2 = Car(red, 50, 50, 50, height // 2 - 25)
obstacles = generate_obstacles()

# Sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, obstacles)

# Clock to control game speed
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game logic
    keys = pygame.key.get_pressed()
    player1.move(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])

    # Collision detection with obstacles
    collisions = pygame.sprite.spritecollide(player1, obstacles, False)
    if collisions:
        player1.rect.x = 50
        player1.rect.y = height // 2 - 25

    # Update the screen
    screen.fill(white)
    all_sprites.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Control game speed
    clock.tick(30)
