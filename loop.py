import pygame
from const import *
from board import *
class loop:
    def __init__(self,number_of_queens):
        self.board = board(number_of_queens)
        self.ROWS = number_of_queens
        self.COLS = number_of_queens
        self.BLOCK_SIZE = SCREEN_WIDTH // self.ROWS
        self.speed = 4
    def render_background(self,surface):
        self.BLOCK_SIZE = SCREEN_WIDTH // self.ROWS
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board.grid[row][col] == 2:
                    color = (30,210,30)
                elif self.board.grid[row][col] == 1:
                    if (row + col) % 2 == 0:
                        color = (210,60,30)
                    else:
                        color = (160,60,30)
                    
                elif (row + col) % 2 == 0:
                    #sand castle color, the top left corner is [0,0] and have light color
                    #Dark 184,139,74
                    #Light 227,193,111
                    color = (227,193,111)
                else:
                    color = (184,139,74)
                square = (col * self.BLOCK_SIZE, row * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)

                pygame.draw.rect(surface,color,square)
    def render_queen(self,surface):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board.squares[row][col].has_queen() == True:
                    qu = self.board.squares[row][col].queen
                    img = pygame.image.load(qu.texture)
                    img = pygame.transform.scale(img,(80/self.ROWS*8,80/self.ROWS*8))
                    img_center = col * self.BLOCK_SIZE + self.BLOCK_SIZE / 2, row * self.BLOCK_SIZE + self.BLOCK_SIZE/ 2
                    qu.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img,qu.texture_rect)
    def modify(self,add):
        self.ROWS += add
        self.COLS += add
        self.board.ROWS += add
        self.board.COLS += add
    


