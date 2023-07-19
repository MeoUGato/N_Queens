from square import square
from const import *
from queen import *
class board:    
    def __init__(self,number_of_queens):
        self.squares = [[square(0,0) for j in range(COLS)] for i in range(ROWS)]
        self.grid = [[0 for j in range(COLS)] for i in range(ROWS)]
        self.queens = []
        self.ROWS = number_of_queens
        self.COLS = number_of_queens
        self.build()
    def build(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.squares[row][col] = square(row,col)

    def add_queen(self,row,col):
        self.queens.append([row,col])
        self.squares[row][col] = square(row,col,queen())
    def remove_queen(self,row,col):
        self.squares[row][col].queen = None

    