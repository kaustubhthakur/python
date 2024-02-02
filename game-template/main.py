import pygame
import time
import random



WIDTH,HEIGHT=800,600
WIN=pygame.display.set_mode((WIDTH,HEIGHT));
BG= pygame.image.load("game/bg.jpeg")

pygame.display.set_caption("space interpreter")
def draw():
    WIN.blit(BG,(0,0))
    pygame.display.update()

def main():
    run=True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    
    pygame.quit()


if __name__=="__main__":
    main()