"""
Main entry script for pygame-web
"""
import asyncio
import pygame
from pygame.locals import *

async def main():
    """Main function of the game.\nIt\n"""
    # initialize and set variables.
    pygame.init()
    display_surface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("TEST")
    font = pygame.font.SysFont(None, 48)
    count = 0
    while True:
        # update loop
        display_surface.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                # Use return instead of sys.exit()
                return
        img = font.render(f"frame: {count}", True, (128,0,0))
        rect = img.get_rect()
        pygame.draw.rect(img, (0,0,0), rect, 1)
        display_surface.blit(img, rect)
        pygame.display.update()
        await asyncio.sleep(0)
        count += 1

asyncio.run(main())