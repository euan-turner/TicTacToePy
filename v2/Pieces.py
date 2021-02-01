import pygame
##Creating piece token surfaces - 70x70 pxs

def draw_nought(dims : (int,int), piece_colour : (int,int,int), back_colour : (int,int,int)) -> pygame.Surface:
    surf = pygame.Surface(dims)
    surf.fill(back_colour)
    centre = (dims[0]//2,dims[1]//2)
    radius = dims[0]//2
    pygame.draw.circle(surf,piece_colour, centre, radius, 14)
    return surf

def draw_cross(dims : (int,int), piece_colour : (int,int,int), back_colour : (int,int,int)) -> pygame.Surface:
    surf = pygame.Surface(dims)
    surf.fill(back_colour)
    ##Top-left to bottom-right
    for_points = [(10,0),(0,10),(dims[0]-10,dims[1]),(dims[0],dims[1]-10)]
    ##Top-right to bottom-left
    back_points = [(dims[0]-10,0),(dims[0],10),(10,dims[1]),(0,dims[1]-10)]
    pygame.draw.polygon(surf,piece_colour,for_points,0)
    pygame.draw.polygon(surf,piece_colour,back_points,0)
    return surf

def testing():
    window = pygame.display.set_mode((400,400))
    window.fill((255,255,255))
    nought = draw_nought((70,70),(128,0,0),(255,255,255))
    cross = draw_cross((70,70),(0,128,0),(255,255,255))
    window.blit(nought, (100,200))
    window.blit(cross,(300,200))
    while True:
        pygame.display.flip()



    