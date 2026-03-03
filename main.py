import pygame
import sys

# 1. INITIALIZE
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Pygame")
clock = pygame.time.Clock()

# PART 4 & 5 — Define Player and Enemy Rectangles
# player = pygame.Rect(x, y, width, height)
player = pygame.Rect(100, 100, 40, 40)
enemy = pygame.Rect(300, 200, 40, 40)

# PART 6 — The Game Loop
running = True
while running:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- UPDATE (PART 4: Player Movement) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5  # Corrected from x to y
    if keys[pygame.K_DOWN]:
        player.y += 5  # Corrected from x to y

    # --- UPDATE (PART 5: Enemy Movement) ---
    enemy.x -= 3
    if enemy.x < -40: # If it goes off the left edge
        enemy.x = 640 # Reset to the right edge

    # --- RENDER (PART 6) ---
    screen.fill((0, 0, 0)) # Clear screen with Black
    
    # Draw the Player (White)
    pygame.draw.rect(screen, (255, 255, 255), player)
    
    # Draw the Enemy (Red)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()