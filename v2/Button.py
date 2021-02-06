import pygame
 
class Button():

    def __init__(self,rect,colour,hoveredColour,revertColour):
        self.rect = rect
        self.colour = colour
        self.hov_colour = hoveredColour
        self.rev_colour = revertColour
        self.hovered = False
        self.clicked = False
    
    ##Check if button is clicked
    ##Returns centre of button, used to place token
    def check_click(self,event : pygame.event ,window):
        
        if (event.type == pygame.MOUSEBUTTONDOWN and 
            self.rect.collidepoint(event.pos) and 
            not self.clicked):
            self.clicked = True
            self.update(window)
            return self.rect.center
        else:
            return None
    
    ##Check if mouse is hovering on button
    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False
    
    ##Update button every frame
    def update(self,window):
        colour = self.colour
        self.check_hover()
        if self.clicked:
            colour = self.rev_colour
        elif self.hovered:
            colour = self.hov_colour
        
        ##Update button colour
        window.fill(colour,self.rect)
        pygame.display.flip()
    

    
