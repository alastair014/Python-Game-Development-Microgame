import os
import sys

# ── Headless / Codespaces environment fixes ───────────────────────────────────
# Xvfb virtual display (started by postStartCommand)
if not os.environ.get("DISPLAY"):
    os.environ["DISPLAY"] = ":99"

# Suppress the "XDG_RUNTIME_DIR is invalid" warning
if not os.environ.get("XDG_RUNTIME_DIR"):
    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-vscode"
    os.makedirs("/tmp/runtime-vscode", exist_ok=True)

# Tell SDL to use a dummy audio driver — silences all ALSA "no sound card" errors
# (Codespaces has no audio hardware; this is safe and expected)
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame

# ─────────────────────────────────────────
#  INITIALISE pygame
# ─────────────────────────────────────────
pygame.init()

# ─────────────────────────────────────────
#  SCREEN / WINDOW SETUP
# ─────────────────────────────────────────
SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
TITLE         = "Pygame"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# ─────────────────────────────────────────
#  CLOCK  (controls frames-per-second)
# ─────────────────────────────────────────
clock = pygame.time.Clock()
FPS = 60

# ─────────────────────────────────────────
#  COLOURS  (R, G, B)
# ─────────────────────────────────────────
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN = (0,   255,   0)
GRAY   = ( 40,  40,  40)   # subtle grid / background tint

# ─────────────────────────────────────────
#  GAME OBJECTS
# ─────────────────────────────────────────
player = pygame.Rect(300, 200, 40, 40)
PLAYER_SPEED = 5             # Pixels moved per frame

enemy = pygame.Rect(100, 100, 30, 30)

# ─────────────────────────────────────────
#  VARIABLES
# ─────────────────────────────────────────
font = pygame.font.Font(None, 36)

# Tracks which screen is currently active
state = "menu"

# ─────────────────────────────────────────
#  HELPER: draw a simple grid (optional visual)
# ─────────────────────────────────────────
def draw_grid():
    for x in range(0, SCREEN_WIDTH, 40):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, 40):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

# ─────────────────────────────────────────
#  GAME LOOP
# ─────────────────────────────────────────
running = True

while running:

    # ── EVENT HANDLING ───────────────────
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Escape key quits the game from any state
            if event.key == pygame.K_ESCAPE:
                running = False

            # Space bar on the menu transitions to gameplay
            if state == "menu" and event.key == pygame.K_SPACE:
                state = "gameplay"

    # ── UPDATE: GAMEPLAY ───────────────────
    if state == "gameplay":
        # ── PLAYER MOVEMENT ──────────────────────────────────────────────────
        # Read which arrow keys are currently held and move the player accordingly
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            player.y -= PLAYER_SPEED    # In pygame, y decreases going up
        if keys[pygame.K_DOWN]:
            player.y += PLAYER_SPEED

        # ── BOUNDARY CLAMPING ────────────────────────────────────────────────
        # Prevent the player from moving outside the window edges
        player.clamp_ip(screen.get_rect())

        enemy.x -= 3
        if enemy.x < -30:               # Wrap from left edge back to right
            enemy.x = SCREEN_WIDTH

        if player.colliderect(enemy):
            state = "gameover"

    # ── RENDER: MENU ─────────────────────────────────────────────────────────
    # Draw the title screen with instructions when in menu state
    if state == "menu":
        screen.fill(BLACK)

        # Render and position the game title and start prompt
        title_text = font.render("SURVIVE THE ARENA", True, WHITE)
        start_text = font.render("Press SPACE to start", True, (200, 200, 200))
        screen.blit(title_text, (150, 150))
        screen.blit(start_text, (160, 220))

        # Push the drawn frame to the display and cap the loop speed
        pygame.display.flip()
        clock.tick(FPS)

    # ── RENDER: GAMEPLAY ───────────────────────────
    elif state == "gameplay":

        # Clear the screen
        screen.fill(BLACK)

        # Subtle background grid
        draw_grid()

        # Draw the Player square
        pygame.draw.rect(screen, WHITE, player)

        # Draw the Enemy square
        pygame.draw.rect(screen, RED, enemy)

        # Flip / update the display
        pygame.display.flip()

        # Tick the clock (cap at FPS)
        clock.tick(FPS)

# ─────────────────────────────────────────
#  CLEAN UP
# ─────────────────────────────────────────
pygame.quit()
sys.exit()