import pygame,itertools,random,time
pygame.init()
 
##Colour variables
black = (0,0,0) ##For board lines
gold = (255,215,0) ##For board background
orchid = (213,92,208) ##For turn pieces and buttons
darkOrchid = (201,52,196) ##For hovered buttons


class board():

    def __init__(self,backColour,boardColour,pieceColour):
        self.gameBoard = [['.','.','.'],['.','.','.'],['.','.','.']]
        self.window = pygame.display.set_mode((400,400))
        self.backColour = backColour
        self.boardColour = boardColour
        self.pieceColour = pieceColour
        
    ##Create Game window
    def createWindow(self):
        pygame.display.set_caption("Tic Tac Toe")
        self.window.fill(self.backColour)
        pygame.display.flip()

    ##Draw on board lines
    def drawBoard(self):
        ##Vertical lines
        pygame.draw.line(self.window,self.boardColour,(150,50),(150,350),2)
        pygame.draw.line(self.window,self.boardColour,(250,50),(250,350),2)
        ##Horizontal lines
        pygame.draw.line(self.window,self.boardColour,(50,150),(350,150),2)
        pygame.draw.line(self.window,self.boardColour,(50,250),(350,250),2)
        ##Draw surrounding rectangle
        pygame.draw.rect(self.window,self.boardColour,(40,40,320,320),10)
        pygame.display.flip()

    ##Draw on a cross at a specified location
    ##Pos is a tuple for the centre of a position
    def drawCross(self,pos):
        midX,midY = pos[0],pos[1]
        ##Top left to bottom right line
        startX,endX = midX - 30, midX + 20
        startY,endY = midY - 20, midY + 30

        for line in range(10):
            pygame.draw.line(self.window,self.pieceColour,(startX,startY),(endX,endY),2)
            startX,endX = startX + 1,endX + 1
            startY,endY = startY - 1,endY - 1

        ##Top right to bottom left line
        startX,endX = midX + 20, midX - 30
        startY,endY = midY - 30, midY + 20

        for line in range(10):
            pygame.draw.line(self.window,self.pieceColour,(startX,startY),(endX,endY),2)
            startX,endX = startX + 1,endX + 1
            startY,endY = startY + 1,endY + 1
            
        pygame.display.flip()

    ##Draw a nought at a specified location
    ##Pos is atuple for the centre of a position
    def drawNought(self,pos):
        midX,midY = pos[0],pos[1]
        ##Drawing circle
        pygame.draw.circle(self.window,self.pieceColour,(midX,midY),30, 10)

        pygame.display.flip()

    ##Check for a win condition on gameBoard
    def checkWin(self):
        ##Check rows
        for row in self.gameBoard:
            ##3 in a row
            if len(set(row)) == 1 and '.' not in row:
                return True
            
        ##Check columns
        for column in range(3):
            col = []
            for row in range(3):
                col.append(self.gameBoard[row][column])
            ##3 in a row
            if len(set(col)) == 1 and '.' not in col:
                return True
            
        ##Check diagonals
        dia = []
        col = 0
        for row in range(3):
            dia.append(self.gameBoard[row][col])
            col += 1
        ##3 in a row
        if len(set(dia)) == 1 and '.' not in dia:
            return True

        dia = []
        col = 2
        for row in range(3):
            dia.append(self.gameBoard[row][col])
            col -= 1
        ##3 in a row
        if len(set(dia)) == 1 and '.' not in dia:
            return True
        return False

    ##Display the winner and the score
    def displayWinner(self,winnerName,player1,player2,backColour,textColour):
        self.window.fill(backColour)

        ##Create labels
        
            
        winnerFont = pygame.font.SysFont('rockwell',40)
        winnerSurface = winnerFont.render("Winner: " + winnerName,False,textColour)
        
        ##Centre text
        winnerRectWidth = winnerSurface.get_rect().width
        windowWidth = self.window.get_rect().width
        winnerLeft = windowWidth/2 - winnerRectWidth/2
        
        self.window.blit(winnerSurface,(winnerLeft,50))
        pygame.display.flip()
            
        
        player2.displayScore(self.window,gold)
        player1.displayScore(self.window,gold)

        
        
            
                
        
    
##Button class - buttons will be placed in the centre of each playable square, so that a player can select one to play
class button():

    def __init__(self,rect,colour,hoveredColour, revertColour):
        self.rect = pygame.Rect(rect)
        self.colour = colour
        self.hoveredColour = hoveredColour
        self.revertColour = revertColour
        self.hovered = False ##Will be used to change the colour of a button when it is hovered
        self.clicked = False ##Use to revert to gold colour

    ##Check if button is clicked
    def checkEvent(self,event,window):
        ##Pass events from event list
        ##Mouse button is clicked on the button
        if event.type == 5 and self.rect.collidepoint(event.pos):
            self.clicked = True
            self.update(window)
            
            return (self.rect[0] + 10,self.rect[1] + 10)
            

    ##Check if button is hovered over
    def checkHover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

    ##Update button every frame
    def update(self,surface):
        colour = self.colour
        self.checkHover()
        if self.clicked:
            colour = self.revertColour
        elif self.hovered:
            colour = self.hoveredColour
            
        surface.fill(colour,self.rect)
        pygame.display.flip()
        
##Create all button objects for the start of each game     
def drawButtons(window,colour,hoveredColour,revertColour):
    positions = [[90,90],[190,90],[290,90],[90,190],[190,190],[290,190],[90,290],[190,290],[290,290]]
    buttons = []
    for position in positions:
        tab = button((position,(20,20)),colour,hoveredColour,revertColour)
        buttons.append(tab)
    return buttons
    
    

class player():

    ##turnFunc is either board.drawNought or board.drawCross, depending on the player
    def __init__(self,name,turnFunc,val,textColour,side,window):
        self.name = name
        self.score = 0
        self.function = turnFunc
        self.val = val
        self.winner = False
        ##Side is a positive side for the left, negative for the right
        self.side = side
        self.textColour = textColour
        self.nameText,self.namePos = self.createText(window)
        

    ##Calculate namePos and therefore scorePos, create text surfaces
    def createText(self,window):
        ##Score name headings
        nameFont = pygame.font.SysFont('rockwell',40)
        nameText = nameFont.render(self.name,False,self.textColour)

        ##Calculate namePos centred points
        rightVal = 150
        windowWidth = window.get_rect().width
        nameWidth = nameText.get_rect().width
        quarterPoint = (windowWidth//2) - (self.side*(windowWidth//4))
        leftVal = quarterPoint - (nameWidth//2)

        return nameText,(leftVal,rightVal)
        
        
        
    ##will then call turn func on a given centre position
    def func(self,turn):
        self.function(turn)
                                     

    ##Used to display a player's score at the end of every round
    def displayScore(self,window,gold):
        
        ##Blit nameText
        window.blit(self.nameText,self.namePos)

        

        ##Old Score if winner, current if loser
        oldScoreFont = pygame.font.SysFont('rockwell',30)
        oldScoreText = oldScoreFont.render(str(self.score),False,self.textColour)

        ##Create background
        background = pygame.Surface((oldScoreText.get_width(),oldScoreText.get_height() + 75))
        background.fill(gold)
        
        ##Create scorePos
        rightVal = 225

        windowWidth = window.get_rect().width
        scoreWidth = oldScoreText.get_rect().width
        quarterPoint = (windowWidth//2) - (self.side*(windowWidth//4))

        leftVal = quarterPoint - (scoreWidth//2)
              
        window.blit(oldScoreText,(leftVal,rightVal))

        pygame.display.flip()

        
        ##If the player won
        if self.winner:

            ##Create new score
            self.score += 1


            ##New score label
            newScoreFont = pygame.font.SysFont('rockwell',30)
            newScoreText = newScoreFont.render(str(self.score),False,self.textColour)

            ##Move new score onto old score
            for right in range(75,0,-1):
                window.blit(background,(leftVal,rightVal))
                window.blit(oldScoreText,(leftVal,rightVal))
                window.blit(newScoreText,(leftVal,rightVal + right))
                pygame.display.flip()
                time.sleep(0.01)

            ##Get rid of old score surface
            window.blit(background,(leftVal,rightVal))
            window.blit(newScoreText,(leftVal,rightVal))
            pygame.display.flip()

            ##Formula to keep socre proportions of scaled surfaces the same
            constant = newScoreText.get_width()/newScoreText.get_height()
            ##Centre co-ordinates for every surface
            centreX,centreY = leftVal + newScoreText.get_width()/2,rightVal + newScoreText.get_height()/2
            ##New background for scaled scores
            newBack = pygame.Surface((newScoreText.get_width() + 30,(newScoreText.get_width() + 30)/constant))
            newBack.fill(gold)

            for flash in range(3):
                ##Enlage score
                for larger in range(30):
                    ##Calculate new width of surface
                    newWidth = newScoreText.get_width() + larger
                    ##Calculate new proportional height of surface
                    newHeight = int(newWidth//constant)
                    ##Create new, scaled surface
                    large = pygame.transform.scale(newScoreText,(newWidth,newHeight))

                    ##Find top left for background and new score surface
                    newX = centreX - large.get_width()/2
                    newY = centreY - large.get_height()/2        

                    window.blit(newBack,(newX,newY))
                    window.blit(large,(newX,newY))
                    pygame.display.flip()
                    time.sleep(0.01)
                                                                                                                            
                ##Shrink score
                for smaller in range(30,0,-1):
                    ##Calculate new width of surface
                    newWidth = newScoreText.get_width() + smaller
                    ##Calculate new proportional height of surface
                    newHeight = int(newWidth//constant)
                    ##Create new, scaled surface
                    small = pygame.transform.scale(newScoreText,(newWidth,newHeight))

                    ##Find top left for background and new score surface
                    newX = centreX - small.get_width()/2
                    newY = centreY - small.get_height()/2

                    window.blit(newBack,(newX,newY))
                    window.blit(small,(newX,newY))
                    pygame.display.flip()
                    time.sleep(0.01)
                    
                

        

        
            
        
        
        
        
        

                                     


board = board(gold,black,orchid)

##Create window
board.createWindow()
##Create board and buttons
board.drawBoard()
##Create buttons
buttons = drawButtons(board.window,orchid,darkOrchid,gold)
usedButtons = []
##Create players
name1 = input("Enter Player 1 name: ")
player1 = player(name1,board.drawCross,True,orchid,1,board.window)
name2 = input("Enter Player 2 name: ")
player2 = player(name2,board.drawNought,False,orchid,-1,board.window)
players = [player1,player2]
random.shuffle(players)
players = itertools.cycle(players)
currentPlayer = next(players)


        
running = True
while running:

    gameEnd = False
    while not gameEnd:
    
        ##Update buttons every frame
        for button in buttons:
            button.update(board.window)

        ##Check for user input
        for event in pygame.event.get():
            if event.type == 5:
                for button in buttons:
                    turn = button.checkEvent(event,board.window)
                    if turn:
                        ##Calculate indexes for gameBoard representation
                        row = (turn[1]//100) - 1
                        column = (turn[0]//100) - 1
                        board.gameBoard[row][column] = currentPlayer.val
                        ##Remove used button from button list
                        buttons.remove(button)
                        usedButtons.append(button)
                        ##Draw turn
                        currentPlayer.func(turn)
                        ##Increment to next player
                        currentPlayer = next(players)

                        ##Check for win condition after turn
                        gameEnd = board.checkWin()
                        
                    if gameEnd:
                        break
            if gameEnd:
                break
    ##Do winning screen, board reset and score update here
    ##Need functionality for a draw
    winningPlayer = next(players)
    winningPlayer.winner = True
    
    
    ##Display Winner: player.name
    board.displayWinner(winningPlayer.name,winningPlayer,next(players),gold,orchid)
    time.sleep(2)
    
    ##Show old scoreboard,display +1 and update

    ##Reset player winner variables
    winningPlayer.winner = False
    ##Board Reset
    board.window.fill(gold)
    board.drawBoard()

    ##Reset buttons
    for button in usedButtons:
        button.clicked = False
        buttons.append(button)
    usedButtons = []

    ##Reset gameBoard
    board.gameBoard = [['.','.','.'],['.','.','.'],['.','.','.']]
    

            
    
            
                
    
    

