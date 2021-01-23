import pygame,time
pygame.init()

window = pygame.display.set_mode((400,400))
background = pygame.Surface((400,400))
background.fill((255,255,255))
window.fill((255,255,255))
pygame.display.set_caption("Test")
pygame.display.flip()

##Old text
oldFont = pygame.font.SysFont('rockwell',40)
oldSurface = oldFont.render("1", False, (0,0,0))
left = 150
oldRight = 100
window.blit(oldSurface,(left,oldRight))
pygame.display.flip()


##New text
newFont = pygame.font.SysFont('rockwell',40)
newSurface = newFont.render("2", False, (0,0,0))

##Move new surface onto old surface
for right in range(75,0,-1):
    window.blit(background,(0,0))
    window.blit(oldSurface,(left,oldRight))
    window.blit(newSurface,(left,oldRight + right))
    pygame.display.flip()
    time.sleep(0.01)

##Get rid of old surface
window.blit(background, (0,0))
window.blit(newSurface,(left,oldRight))
pygame.display.flip()

##Formula to keep proportions of new surface the same
constant = newSurface.get_width() / newSurface.get_height()
##Centre co-ordinates of every surface
centreX,centreY = left + newSurface.get_width()/2,oldRight + newSurface.get_height()/2

for larger in range(30):
    ##Calculate new width of surface
    newWidth = newSurface.get_width() + larger
    ##Create a scaled, proportional new surface
    large = pygame.transform.scale(newSurface,(newWidth,int(newWidth//constant)))
    window.blit(background,(0,0))
    
    window.blit(large,(centreX - large.get_width()/2,centreY - large.get_height()/2))

    pygame.display.flip()
    time.sleep(0.01)

for smaller in range(30,0,-1):
    ##Calculate width of surface
    newWidth = newSurface.get_width() + smaller
    ##Create a scale,proportional new surface
    small = pygame.transform.scale(newSurface,(newWidth,int(newWidth//constant)))

    window.blit(background,(0,0))

    window.blit(small,(centreX - small.get_width()/2,centreY-small.get_height()/2))
    pygame.display.flip()
    time.sleep(0.01)

for larger in range(30):
    ##Calculate new width of surface
    newWidth = newSurface.get_width() + larger
    ##Create a scaled, proportional new surface
    large = pygame.transform.scale(newSurface,(newWidth,int(newWidth//constant)))
    window.blit(background,(0,0))
    
    window.blit(large,(centreX - large.get_width()/2,centreY - large.get_height()/2))

    pygame.display.flip()
    time.sleep(0.01)

for smaller in range(30,0,-1):
    ##Calculate width of surface
    newWidth = newSurface.get_width() + smaller
    ##Create a scale,proportional new surface
    small = pygame.transform.scale(newSurface,(newWidth,int(newWidth//constant)))

    window.blit(background,(0,0))

    window.blit(small,(centreX - small.get_width()/2,centreY-small.get_height()/2))
    pygame.display.flip()
    time.sleep(0.01)

for larger in range(30):
    ##Calculate new width of surface
    newWidth = newSurface.get_width() + larger
    ##Create a scaled, proportional new surface
    large = pygame.transform.scale(newSurface,(newWidth,int(newWidth//constant)))
    window.blit(background,(0,0))
    
    window.blit(large,(centreX - large.get_width()/2,centreY - large.get_height()/2))

    pygame.display.flip()
    time.sleep(0.01)

for smaller in range(30,0,-1):
    ##Calculate width of surface
    newWidth = newSurface.get_width() + smaller
    ##Create a scale,proportional new surface
    small = pygame.transform.scale(newSurface,(newWidth,int(newWidth//constant)))

    window.blit(background,(0,0))

    window.blit(small,(centreX - small.get_width()/2,centreY-small.get_height()/2))
    pygame.display.flip()
    time.sleep(0.01)


pygame.display.flip()
    
    
