import pygame, sys
from const import *
from loop  import *
from board import *
import time
class Main:
    def __init__(self):
        pygame.init()
        self.loop = loop(number_of_queens=8)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("N QUEENS")
        self.font = pygame.font.Font("rimouski sb.ttf",36)
        self.number_of_queen = 8
        self.menu = [
            "Start",
            f"Number of queens : {self.number_of_queen}",
            "Quit"
        ]
        self.current_op = 0
        
    def backtrack(self):
        have_find = False
        loop = self.loop
        screen = self.screen
        clock = pygame.time.Clock()
        def check(col,row) -> bool:
            flag = True
            for x in range(self.loop.ROWS):
                for y in range(self.loop.COLS):
                    if x == row and y == col:
                        self.loop.board.grid[x][y] = 2
                    elif x == row or y == col or x + y == row + col or x - y == row - col:
                        self.loop.board.grid[x][y] = 1
                        if self.loop.board.squares[x][y].has_queen():
                            flag = False
                    else:
                        self.loop.board.grid[x][y] = 0
            return flag
        def reset_board():
            for x in range(self.loop.ROWS):
                for y in range(self.loop.COLS):
                    loop.board.grid[x][y] = 0
            return
        def recursion(current_col):
            nonlocal have_find
            if have_find == True:
                return
            if current_col == self.loop.COLS:
                have_find = True
                time.sleep(5)
                self.loop.board = board(self.loop.COLS)
                self.menu_handler()
                return
            for r in range(self.loop.ROWS):
                if check(current_col,r):
                    self.loop.board.add_queen(r,current_col)
                    draw()
                    recursion(current_col+1)
                    self.loop.board.remove_queen(r,current_col)
                    draw()
                else:
                    self.loop.board.add_queen(r,current_col)
                    draw()
                    self.loop.board.remove_queen(r,current_col)
                    reset_board()
                    draw()
        def draw():
            font = self.font
            clock.tick(FPS)
            loop.render_background(screen)
            loop.render_queen(screen)
            text = font.render(f"speed : {self.loop.speed}",True,BLUE)
            img_center = (0,750)
            screen.blit(text,img_center)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.reset_to_menu()
                        self.menu_handler() 
                    elif event.key == pygame.K_LEFT and self.loop.speed >= 2:
                        self.loop.speed -= 1
                    elif event.key == pygame.K_RIGHT:
                        self.loop.speed += 1
            pygame.display.update()
            time.sleep(1.0/self.loop.speed)
        recursion(0)
        
        time.sleep(2)
        return have_find   
    def reset_to_menu(self):
        self.loop.board = board(number_of_queens=self.number_of_queen)
    def menu_handler(self):
        loop = self.loop
        screen = self.screen
        clock = pygame.time.Clock()
        def show_menu():
            menu = self.menu
            current_op = self.current_op
            font = self.font 
            screen = self.screen
            for i in range(len(menu)):
                option = menu[i]
                if i == current_op:
                    text = font.render(option, True, RED)
                else:
                    text = font.render(option, True, BLUE)
                img_center = (SCREEN_WIDTH // 2 - 150, 300 + i * 100)
                screen.blit(text,img_center)
        while True:
            menu = self.menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_op = (self.current_op - 1) % len(menu)
                    elif event.key == pygame.K_DOWN:
                        self.current_op = (self.current_op + 1) % len(menu)
                    elif event.key == pygame.K_RETURN:
                        if self.current_op == 0:
                            self.backtrack()
                        elif self.current_op == 2:
                            pygame.quit()
                            sys.exit()
                    elif event.key == pygame.K_LEFT and self.current_op == 1 and self.number_of_queen > 6:
                        self.number_of_queen -= 1
                        self.menu[1] = f"Number of queens : {self.number_of_queen}"
                        self.loop.modify(-1)
                    elif event.key == pygame.K_RIGHT and self.current_op == 1 and self.number_of_queen <= 24:
                        self.number_of_queen += 1
                        self.menu[1] = f"Number of queens : {self.number_of_queen}"
                        self.loop.modify(1)

            clock.tick(FPS)
            loop.render_background(screen)
            loop.render_queen(screen)
            show_menu()
            pygame.display.update()
main = Main()
main.menu_handler()
