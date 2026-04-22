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
#  VARIABLES
# ─────────────────────────────────────────
font = pygame.font.Font(None, 36)

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

    # ── RENDER ───────────────────────────
    # Clear the screen
    screen.fill(BLACK)

    # Optional subtle grid
    draw_grid()

    # Flip / update the display
    pygame.display.flip()

    # Tick the clock (cap at FPS)
    clock.tick(FPS)

# ─────────────────────────────────────────
#  CLEAN UP
# ─────────────────────────────────────────
pygame.quit()
sys.exit()