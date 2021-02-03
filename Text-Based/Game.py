import numpy as np, time

class Board():

    def __init__(self):
        self.state = np.zeros((3,3),dtype=int)
        self.turns = 0
        self.scores = [0,0]

    def check_win(self) -> int:
        ##Check columns
        col_sum = np.sum(self.state, axis=0)
        ##Check rows
        row_sum = np.sum(self.state, axis=1)
        ##Forward diagonal
        for_sum = np.sum(self.state.diagonal())
        ##Backward diagonal
        back_sum = np.sum(np.fliplr(self.state).diagonal())

        if 3 in col_sum or 3 in row_sum or for_sum == 3 or back_sum == 3:
            return 1
        elif -3 in col_sum or -3 in row_sum or for_sum == -3 or back_sum == -3:
            return -1
        ##Game is either drawn, or no win
        else:
            if 0 not in self.state:
                print("Game is drawn")
                self.reset()
            else:
                return 0
    
    def reset(self):
        time.sleep(1)
        self.__init__()

    def output(self):
        print("--------")
        for row in self.state:
            print(end = "|")
            for col in row:
                if col == 1:
                    char = 'x'
                elif col == -1:
                    char = 'o'
                else:
                    char = ' '
                print(char, end = "|")
            print("\n--------")

    def turn(self):
        ##Use to differentiate between AI and player
        if self.turns % 2 == 0:
            token = 1
        else:
            token = -1

        choice = int(input("Enter square (1-9): "))-1
        self.state[choice//3][choice%3] = token
        self.turns+=1
        status = self.check_win()
        if status == 1:
            self.output()
            print("Player 1 wins")
            self.scores[0] += 1
            print("Score: ", self.scores)
            self.reset()
        elif status == -1:
            self.output()
            print("Player 2 wins")
            self.scores[1] += 1
            self.reset()
        
    

    

board = Board()


while True:
    board.output()
    board.turn()