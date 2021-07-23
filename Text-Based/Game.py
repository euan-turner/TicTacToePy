import numpy as np
from prettytable import PrettyTable
from random import shuffle
from itertools import cycle
from dataclasses import dataclass

PLAYER = 1
AI = -1
EMPTY = 0

@dataclass
class Move:
    row : int
    col : int

class Board():

    def __init__(self):
        self.state = np.zeros((3,3), dtype = int)
        self.turns = 0
    
    def check_win(self):
        #Check columns
        col_sum = abs(np.sum(self.state, axis = 0))
        #Check rows
        row_sum = abs(np.sum(self.state, axis = 1))
        #Forward diagonal
        for_sum = abs(np.sum(self.state.diagonal()))
        #Backward diagonal 
        back_sum = abs(np.sum(np.fliplr(self.state).diagonal()))
        if 3 in col_sum or 3 in row_sum or 3 == for_sum or 3 == back_sum:
            return True
        else:
            return False
    
    def game_over(self):
        if len(np.where(self.state == EMPTY)[0]) == 0:
            return 0
        elif self.check_win():
            return 1
        else:
            return -1
    
    def reset(self):
        self.__init__()
    
    def valid_moves(self):
        moves = []
        for r in range(3):
            for c in range(3):
                if self.state[r][c] == EMPTY:
                    moves.append(Move(r,c))
        return moves
    
    def make_move(self, move, token):
        self.state[move.row][move.col] = token
    
    def undo(self,move):
        self.state[move.row][move.col] = EMPTY

    def output(self):
        table = PrettyTable()
        table.header = False
        table.hrules = True
        
        for row in self.state:
            r = []
            for col in row:
                if col == PLAYER:
                    r.append('x')
                elif col == AI:
                    r.append('o')
                else:
                    r.append(' ')
            table.add_row(r)
        print(table)

class Game():

    def __init__(self):
        self.board = Board()
        self.players = cycle(shuffle_arr([PLAYER,AI]))
        self.current = next(self.players)
    
    def turn(self):
        self.board.output()
        move = None

        if self.current == AI:
            move = self.find_best_move()

        else:
            valid = self.board.valid_moves()
            while move not in valid:
                choice = int(input("Enter square (1-9): ")) - 1
                move = Move(choice//3,choice%3)
        
        self.board.make_move(move, self.current)

        status = self.board.game_over()
        if status == 0:
            print("Game is drawn")
            self.board.reset()
        elif status == 1:
            print("Game is won")
            self.board.reset()
        
        self.board.turns += 1
        self.current = next(self.players)

    def find_best_move(self):
        best_move = None
        best_eval = -100000
        for move in shuffle_arr(self.board.valid_moves()):

            self.board.make_move(move, AI)
            move_eval = self.minimax(0, -100000, 100000, False)
            print(move, move_eval)
            self.board.undo(move)

            if move_eval > best_eval:
                best_eval = move_eval
                best_move = move

        return best_move
    
    def minimax(self, depth, alpha, beta, isMax):
        status = self.board.game_over()
        if status == 0:
            return 0 
        elif status == 1:
            if isMax:
                return -10 + depth
            else:
                return 10 - depth
        
        if isMax:
            best = -100000
            for move in shuffle_arr(self.board.valid_moves()):
                self.board.make_move(move, AI)
                best = max(best, self.minimax(depth+1, alpha, beta, False))
                self.board.undo(move)

                if best >= beta:
                    break
                alpha = max(alpha, best)
            return best
        else:
            best = 100000
            for move in shuffle_arr(self.board.valid_moves()):
                self.board.make_move(move, PLAYER)
                best = min(best, self.minimax(depth+1, alpha, beta, True))
                self.board.undo(move)

                if best <= alpha:
                    break
                beta = min(beta, best)
            return best
    
    def main(self):
        while True:
            self.turn()

def shuffle_arr(arr):
    shuffle(arr)
    return arr

game = Game()
game.main()



