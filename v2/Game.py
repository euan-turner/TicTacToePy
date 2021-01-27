import pygame

class Game():

    def __init__(self,display : Display):
        self.display = display
        self.players = self.get_players()
    
    ##Functionality to create player instances
    ##Add case for player vs Minimax later
    def get_players(self):
        pass

    def create_name_surfs(self):
        for player in self.players:
            font = pygame.font.SysFont('rockwell',40)
            name_surf = font.render(player.name,False,player.text_colour)

            top = (3/8)*self.display.window.get_height()
            ##Use player.val to determine side
            quarter = (self.display.window.get_width()//2) + (player.val*(self.display.window.get_width()//4))
            left = quarter - (name_surf.get_width()//2)
            name_rect = pygame.rect(left,top,name_surf.get_width(),name_surf.get_height())

            player.name_surf = name_surf
            player.name_rect = name_rect
    
    ##Temporary functionality for testing
    def display_scores(self):
        for player in self.players:
            self.display.windpw.blit(player.name_surf,player.name_rect)


    def update_scores(self):
        pass
