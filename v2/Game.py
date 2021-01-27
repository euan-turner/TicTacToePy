import pygame
 
class Game():

    ##Passing players to the constructor is temporary for testing
    def __init__(self,display,players):
        self.display = display
        self.players = players
        ##self.players = self.get_players()
    
    ##Functionality to create player instances
    ##Add case for player vs Minimax later
    def get_players(self):
        pass

    ##def init_display() ? May initialise display instance inside game class

    ##Functionality to create and draw buttons
    ##Need a way to monitor
    def set_buttons(self):
        pass

    def create_name_surfs(self):
        for player in self.players:
            font = pygame.font.SysFont('rockwell',40)
            name_surf = font.render(player.name,False,player.text_colour)

            top = (3/8)*self.display.window.get_height()
            ##Use player.val to determine side
            quarter = (self.display.window.get_width()//2) + (player.val*(self.display.window.get_width()//4))
            left = quarter - (name_surf.get_width()//2)
            name_rect = pygame.Rect(left,top,name_surf.get_width(),name_surf.get_height())

            player.name_surf = name_surf
            player.name_rect = name_rect
    
    ##Temporary functionality for testing
    def display_scores(self):
        for player in self.players:
            self.display.window.blit(player.name_surf,player.name_rect)


    def update_scores(self):
        pass

    ##Game loop
    def main(self):

        cont = True
        while cont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cont = False
                    continue
        
        pass