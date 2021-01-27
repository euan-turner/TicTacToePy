import numpy as np

class Board():

    def __init__(self):
        self.state = np.zeros((3,3),dtype=int)
         
    
    def check_win(self) -> int:
        ##Check columns
        col_sum = np.sum(self.state, axis=0)
        ##Check rows
        row_sum = np.sum(self.state, axis=1)
        ##Forward diagonal
        for_sum = np.sum(self.state.diagonal())
        ##Backward diagonal
        back_sum = np.sum(np.fliplr(self.state).diagonal())

        ##returns 1 if player(1) wins
        ##returns -1 if player(-1) wins
        ##returns 0 no win
        if 3 in col_sum or 3 in row_sum or for_sum == 3 or back_sum == 3:
            return 1
        elif -3 in col_sum or -3 in row_sum or for_sum == -3 or back_sum == -3:
            return -1
        ##Game is either drawn, or no win
        else:
            return 0
        
    def reset(self):
        self.state = np.zeros((3,3),dtype=int)
        


def testing():
    drawtest = np.array([[1,0,-1],[0,1,1],[0,-1,-1]])
    coltest = np.array([[1,-1,0],[1,0,-1],[1,0,0]])
    rowtest = np.array([[0,0,1],[0,1,1],[-1,-1,-1]])
    backtest = np.array([[0,0,1],[0,1,-1],[1,-1,0]])
    fortest = np.array([[-1,1,1],[0,-1,1],[0,0,-1]])

    b = Board(drawtest)
    print(b.check_win())
    b.state = coltest.copy()
    print(b.check_win())
    b.state = rowtest.copy()
    print(b.check_win())
    b.state = backtest.copy()
    print(b.check_win())
    b.state = fortest.copy()
    print(b.check_win())
