"""
main.py — pygame Starter Project
=================================
Session 1 — Part 4 Solution: Player Movement

HOW TO RUN:
    python main.py

CONTROLS:
    Arrow Keys  → Move the white player square
    ESC         → Quit the game
"""

import os
import sys

# ── Headless / Codespaces environment fixes ───────────────────────────────────
if not os.environ.get("DISPLAY"):
    os.environ["DISPLAY"] = ":99"

if not os.environ.get("XDG_RUNTIME_DIR"):
    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-vscode"
    os.makedirs("/tmp/runtime-vscode", exist_ok=True)

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
GRAY   = ( 40,  40,  40)

# ─────────────────────────────────────────
#  GAME OBJECTS
# ─────────────────────────────────────────

# Player — white square, starts near top-left
# pygame.Rect(x, y, width, height)
player = pygame.Rect(100, 100, 40, 40)
PLAYER_SPEED = 5

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
            if event.key == pygame.K_ESCAPE:
                running = False

    # ── UPDATE ───────────────────────────

    # 1. Read keyboard input & move player
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED      # NOTE: UP decreases y in pygame
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED

    # 2. Keep player inside the window
    player.clamp_ip(screen.get_rect())

    # ── RENDER ───────────────────────────

    # 1. Clear the screen
    screen.fill(BLACK)

    # 2. Optional subtle grid
    draw_grid()

    # 3. Draw the player
    pygame.draw.rect(screen, WHITE, player)

    # 4. Flip / update the display
    pygame.display.flip()

    # 5. Tick the clock (cap at FPS)
    clock.tick(FPS)

# ─────────────────────────────────────────
#  CLEAN UP
# ─────────────────────────────────────────
pygame.quit()
sys.exit()