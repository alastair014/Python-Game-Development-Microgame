import asyncio
import pygame

pygame.init()

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
TITLE         = "Pygame"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
FPS = 60

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GRAY  = ( 40,  40,  40)

async def main():
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BLACK)
        pygame.display.flip()
        clock.tick(FPS)

        await asyncio.sleep(0)  # yield to browser each frame

    pygame.quit()

asyncio.run(main())