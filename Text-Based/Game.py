import numpy as np, time
from prettytable import PrettyTable

class Board():

    def __init__(self):
        self.state = np.zeros((3,3),dtype=int)
        self.turns = 0
        self.scores = [0,0]
        self.mode = int(input("Mode? (1,-1): "))

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
            return 0

    def reset(self):
        time.sleep(1)
        self.__init__()

    def output(self):
        table = PrettyTable()
        table.header = False
        table.hrules = True
        for row in self.state:
            r = []
            for col in row:
                if col == 1:
                    r.append('x')
                elif col == -1:
                    r.append('o')
                else:
                    r.append(' ')
            table.add_row(r)
        print(table)

    def turn(self):
        ##Even turn and player plays first -> player turn
        ##Odd turn and player plays second -> player turn
        if (self.turns % 2 == 0 and self.mode == 1) or (self.turns % 2 != 0 and self.mode == -1):
            token = -1
            choice = -1
            while choice not in range(0,9) or self.state[choice//3][choice%3] != 0:
                choice = int(input("Enter square (1-9): "))-1
            self.state[choice//3][choice%3] = token
            self.turns+=1
        ##Both other cases coverd by Ai turn
        else:
            token = 1
            ai_move = self.find_best_move(token)
            self.state[ai_move[0]][ai_move[1]] = token
            self.turns += 1

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
        elif status == 0 and 0 not in self.state:
            self.output()
            print("Game is drawn")
            self.reset()

    def find_best_move(self, ai_token : int) -> (int,int):
        best_move = None
        best_eval = -1000
        
        ##Search valid moves
        for row in range(3):
            for col in range(3):
                
                if self.state[row][col] == 0:
                    self.state[row][col] = ai_token

                    curr_depth = len(np.where(self.state!=0)[0])
                    ##Inital alpha = -1000, beta = 1000
                    move_eval = self.minimax(curr_depth, False, ai_token, -1000, 1000)
                    self.state[row][col] = 0

                    if move_eval > best_eval:
                        best_move = (row,col)
                        best_eval = move_eval
        
        return best_move
     
    def minimax(self,depth : int, is_max : bool, ai_token : int, alpha : int, beta : int):
        score = self.check_win()
        ##AI win
        if score == 1:
            return 10
        ##Opponent win
        elif score == -1:
            return -10
        ##Draw
        elif len(np.where(self.state==0)[0]) == 0:
            return 0

        ##Maximising player -> AI
        if is_max:
            best_eval = -1000

            ##Search valid moves
            for row in range(3):
                for col in range(3):
                    if self.state[row][col] == 0:
                        self.state[row][col] = ai_token
                        move_eval = self.minimax(depth+1, not is_max, ai_token, alpha, beta)
                        self.state[row][col] = 0
                        best_eval = max(best_eval,move_eval)
                        alpha = max(alpha, best_eval)

                        if beta <= alpha:
                            break
            
            ##Work on incorporating depth for efficient wins and prolonged losses
            return best_eval
        
        ##Minimising player -> Human
        elif not is_max:
            best_eval = 1000

            ##Search valid moves
            for row in range(3):
                for col in range(3):
                    if self.state[row][col] == 0:
                        self.state[row][col] = - ai_token
                        move_eval = self.minimax(depth+1, not is_max, ai_token, alpha, beta)
                        self.state[row][col] = 0
                        best_eval = min(best_eval, move_eval)
                        beta = min(beta, best_eval)

                        if beta <= alpha:
                            break
            
            ##Work on incorporating depth for efficient wins and prolonged losses
            return best_eval

board = Board()


while True:
    board.output()
    board.turn()