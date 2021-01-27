from Board import Board
from Player import Player
from Display import Display
from Game import Game

import pygame,sys

black = (0,0,0)
gold = (255,215,0)
red = (255,0,0)
green = (0,255,0)
 


p1token = pygame.Surface((80,80))
p1token.fill(red)
p1 = Player("one",p1token,1,red)

p2token = pygame.Surface((80,80))
p2token.fill(green)
p2 = Player("two",p2token,-1,green)
disp = Display(gold,black)
players = [p1,p2]

game = Game(disp,players)

for player in game.players:
    game.display.draw_piece((200+50*player.val,250),player.token)

game.create_name_surfs()
game.display_scores()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        pygame.display.flip()

