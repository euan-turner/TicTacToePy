import pygame, sys

class Display():

    def __init__(self, backColour, boardColour):
        self.back_colour = backColour
        self.board_colour = boardColour

        self.create_window()
        self.draw_board()
    
    def create_window(self):
        self.window = pygame.display.set_mode((400,400))
        pygame.display.set_caption("Tic Tac Toe")
        self.window.fill(self.back_colour)

    def draw_board(self):
        ##Vertical lines 
        pygame.draw.line(self.window,self.board_colour, (150,50), (150,350),2)
        pygame.draw.line(self.window,self.board_colour, (250,50), (250,350),2)
        ##Horizontal lines
        pygame.draw.line(self.window,self.board_colour, (50,150), (350,150),2)
        pygame.draw.line(self.window,self.board_colour, (50,250), (350,250),2)
        ##Surrounding rectangle
        pygame.draw.rect(self.window,self.board_colour,(40,40,320,320),10)
        pygame.display.flip()
    
    def draw_piece(self, pos : (int,int), token : pygame.Surface):
        x,y = pos[0]-token.get_width()//2, pos[1]-token.get_height()//2
        self.window.blit(token, (x,y))
        pygame.display.flip()
    
    ##Uses player instances
    def update_score(self):
        pass

def test():
    black = (0,0,0)
    gold = (255,215,0)
    orchid = (213,92,208)
    disp = Display(gold,black)

    temp = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        temp += 1
        if temp == 50:
            piece = pygame.Surface((70,70))
            piece.fill(orchid)
            disp.draw_piece((200,200),piece)
        pygame.display.flip()

    
    


test()