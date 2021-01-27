import pygame

class Button():
 
    def __init__(self,rect,colour,hoveredColour,revertColour):
        self.rect = pygame.Rect(rect)
        self.colour = colour
        self.hovered_col = hoveredColour
        self.revert_col = revertColour
        self.hovered = False
        self.clicked = False
    
    ##Check if button is clicked
    ##Returns centre of button, used to place token
    def check_click(self,events : list,window):
        ##Pass list of current events
        for event in events:
            if event.type == 5 and self.rect.collidepoint(event.pos):
                self.clicked = True
                self.update(window)
                return self.rect.center
    
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
            colour = self.revert_col
        elif self.hovered:
            colour = self.hovered_col
        
        ##Update button colour
        window.fill(colour,self.rect)
        pygame.display.flip()
    

    
