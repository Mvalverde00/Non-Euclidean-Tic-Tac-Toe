import pygame as pg
from math import sqrt

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

pg.font.init()
font = pg.font.SysFont("Comic Sans MS", 24)
big_font = pg.font.SysFont("Comic Sans MS", 60)


def gen_winning_combos(n):
    solutions = []

    # Columns & Rows
    for i in range(n):
        c_solution = [] # Column
        r_solution = [] # Row
        for j in range(n):
            c_solution.append(i+j*n)
            r_solution.append(i*n + j)
        solutions.append(c_solution)
        solutions.append(r_solution)


    solution = []
    for i in range(n):
        solution.append(i*n + i)

    for i in range(n):
        temp = []
        for j, e in enumerate(solution):
            new = (e+i)%((j+1)*n)
            if (e+i) >= (j+1)*n:
                new += (j)*n
            temp.append(new)
        solutions.append(temp)

    solution = []
    for i in range(n):
        solution.append((n-1)*(i+1))
    print(solution)
    for i in range(n):
        temp = []
        for j, e in enumerate(solution):
            new = (e-i)
            if (e-i) < (j)*n:
                new += n
            temp.append(new)
        solutions.append(temp)
    return solutions
class Board():
    
    # Pixels
    LENGTH = 500;
    HEIGHT = 500;
    L_OFFSET = 100;
    H_OFFSET = 5;
    
    EMPTY = " "
    PLAYER_0 = "X"
    PLAYER_1 = "O"

    PLAYER_0_COLOR = RED
    PLAYER_1_COLOR = BLUE

    PLAYER_0_MESSAGE = font.render("Player X's Turn", False, PLAYER_0_COLOR)
    PLAYER_1_MESSAGE = font.render("Player 0's Turn", False, PLAYER_1_COLOR)
    PLAYER_1_MESSAGE_LEN = font.size("Player 0's Turn")[0] # Used to align placement of text

    PLAYER_0_VICTORY_MESSAGE = big_font.render("PLAYER X WINS", True, PLAYER_0_COLOR)
    PLAYER_0_VICTORY_MESSAGE_LEN = big_font.size("PLAYER X WINS") # Used to align placement of text
    PLAYER_1_VICTORY_MESSAGE = big_font.render("PLAYER 0 WINS", True, PLAYER_1_COLOR)
    PLAYER_1_VICTORY_MESSAGE_LEN = big_font.size("PLAYER 0 WINS")
    DRAW_MESSAGE = big_font.render("DRAW", True, BLACK)
    DRAW_MESSAGE_LEN = big_font.size("DRAW")
    

    def __init__(self, size):
        self.size = size

        self.board = [[self.EMPTY]*size for i in range(size)] # Create empty nxn board.  do NOT try [[self.EMPTY]*size]*size -- it does not work
        self.solutions = gen_winning_combos(size) # Get a list of winning permutations, for the sake of checking later

        self.turn = 0
        self.moves_made = 0 # used to easily track draw

        self.game_over = False
        self.game_over_message = None # 0 for X, 1 for 0, 2 for draw

    def check_winner(self):
        # Check all possible solutions
        for solution in self.solutions:
            # Get value in first cell of solution
            start = self.board[solution[0]//self.size][solution[0]%self.size]

            found = True

            # If the first cell is empty, abort early
            if start == self.EMPTY:
                found = False
            
            # Keep on going until a cell changes value -- at which point we can break, this solution is no-good
            for cell in solution:
                i = cell // self.size
                j = cell % self.size
                if self.board[i][j] != start:
                    found = False
                    break
            # If it makes it this far, the solution is valid
            if found:
                if start == self.PLAYER_0:
                    self.game_over_message = 0
                else:
                    self.game_over_message = 1

                self.game_over = True
                return

            if self.moves_made == self.size**2:
                self.game_over_message = 2
                self.game_over = True

    
    def apply_click(self, x,y):
        if x >= self.LENGTH or y >= self.HEIGHT:
            return
        (i,j) = int(x // (self.LENGTH/self.size)), int(y//(self.HEIGHT/self.size))
        print(i,j)
        if self.board[i][j] != self.EMPTY:
            return

        if self.turn == 0:
            self.board[i][j] = self.PLAYER_0
        else:
            self.board[i][j] = self.PLAYER_1

        self.turn = int(not self.turn) # Swap turn
        self.moves_made += 1

        self.check_winner()

    def render(self, screen):

        self.draw_board(screen)
        self.draw_player_marks(screen)
        self.draw_HUD(screen)
        self.draw_game_over(screen)
        
    def draw_board(self, screen):
        x0 = self.LENGTH/self.size
        y0 = self.HEIGHT/self.size

        for i in range(1,self.size):
            pg.draw.line(screen, BLACK, [x0*i, 0], [x0*i, self.HEIGHT], 5 ) # Top to bottom
            pg.draw.line(screen, BLACK, [0, y0*i], [self.LENGTH, y0*i], 5 ) # Left to Right
        
    
    def draw_player_marks(self, screen):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == self.PLAYER_0:
                    self.draw_x(screen, self.LENGTH/self.size * i + 10, self.HEIGHT/self.size * j + 10, self.LENGTH/self.size -20)
                elif cell == self.PLAYER_1:
                    self.draw_0(screen, self.LENGTH/self.size * i + 10, self.HEIGHT/self.size * j + 10, self.LENGTH/self.size -20)

    # x,y = top left coord
    def draw_x(self, screen, x, y, _len):
        pg.draw.line(screen, self.PLAYER_0_COLOR, [x, y], [x+_len, y+_len], 5)
        pg.draw.line(screen, self.PLAYER_0_COLOR, [x+_len ,y], [x, y+_len], 5)

    def draw_0(self, screen, x, y, _len):
        pg.draw.ellipse(screen, self.PLAYER_1_COLOR, (x, y, _len, _len), 5)

    def draw_HUD(self, screen):

        if not self.turn:
            self.PLAYER_0_MESSAGE.set_alpha(255)
            self.PLAYER_1_MESSAGE.set_alpha(60)
        else:
            self.PLAYER_0_MESSAGE.set_alpha(60)
            self.PLAYER_1_MESSAGE.set_alpha(255)
        screen.blit(self.PLAYER_0_MESSAGE, [10, self.HEIGHT + 20])
        screen.blit(self.PLAYER_1_MESSAGE, [self.LENGTH - self.PLAYER_1_MESSAGE_LEN - 20, self.HEIGHT + 20])

    def draw_game_over(self, screen):
        if self.game_over_message == 0:
             screen.blit(self.PLAYER_0_VICTORY_MESSAGE, [(self.LENGTH - self.PLAYER_0_VICTORY_MESSAGE_LEN[0])/2,  (self.HEIGHT - self.PLAYER_0_VICTORY_MESSAGE_LEN[1])/2])
        elif self.game_over_message == 1:
             screen.blit(self.PLAYER_1_VICTORY_MESSAGE, [(self.LENGTH - self.PLAYER_1_VICTORY_MESSAGE_LEN[0])/2,  (self.HEIGHT - self.PLAYER_1_VICTORY_MESSAGE_LEN[1])/2])
        elif self.game_over_message == 2:
             screen.blit(self.DRAW_MESSAGE, [(self.LENGTH - self.DRAW_MESSAGE_LEN[0])/2,  (self.HEIGHT - self.DRAW_MESSAGE_LEN[1])/2])

