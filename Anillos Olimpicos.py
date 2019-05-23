import pygame
from pygame.locals import * 
import sys

pygame.init()
fpsClock=pygame.time.Clock()

surface = pygame.display.set_mode((800,600))


while True:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.draw.circle(surface, (0,0,250),(200, 200), 150, 30)
    pygame.draw.circle(surface, (255,255,255),(400, 200), 150, 30)
    pygame.draw.circle(surface, (255,0,0),(600, 200), 150,30)
    pygame.draw.circle(surface, (255,255,0),(300, 410), 150, 30)
    pygame.draw.circle(surface, (0,255,0),(500, 410), 150, 30)
    
    
    
    
    pygame.display.update()
    fpsClock.tick(30)