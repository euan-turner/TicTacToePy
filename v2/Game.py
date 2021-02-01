import pygame, random, itertools
from Board import Board
from Player import Player
from Display import Display
from Button import Button
from Pieces import draw_nought, draw_cross

##Colours
black = (0,0,0) ##For board lines
gold = (255,215,0) ##For board background
orchid = (213,92,208) ## For turn pieces and buttons
dark_orchid = (201,52,196) ## For hovered buttons


class Game():

    ##Passing players to the constructor is temporary for testing
    def __init__(self):
        self.display = Display(gold,black)
        self.players = self.get_players()
        self.board = Board()
    
    ##Functionality to create player instances
    ##Add case for player vs Minimax later
    def get_players(self):
        p1_name = input("Enter player 1 name: ")
        p1 = Player(p1_name,draw_nought((70,70),orchid,gold),1,orchid)
        p2_name = input("Enter player 2 name: ")
        p2 = Player(p2_name,draw_cross((70,70),orchid,gold),-1,orchid)
        players = [p1,p2]
        random.shuffle(players)
        self.create_name_surfs(players)
        return itertools.cycle(players)


    ##def init_display() ? May initialise display instance inside game class

    ##Functionality to create and draw buttons
    ##Need a way to monitor
    def set_buttons(self):
        pass

    def create_name_surfs(self,players):
        for player in players:
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
        player = next(self.players)
        self.display.window.blit(player.name_surf,player.name_rect)
        player=next(self.players)
        self.display.window.blit(player.name_surf,player.name_rect)


    def update_scores(self):
        for player in self.players:
            if player.is_winner:
                player.inc_score()
            player.is_winner = False

    ##Game loop
    def main(self):
        
        ##Variable set-up

        ##Testing
        self.display_scores()
        player = next(self.players)
        self.display.draw_piece((150,200),player.token)
        player = next(self.players)
        self.display.draw_piece((250,200),player.token)

        cont = True
        while cont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cont = False
                    continue
            pygame.display.flip()
        
                
            ##winner = self.board.check_win()
            ##if winner: inc_score on winner

