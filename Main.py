import pygame as pg
from Board import Board

# Set some constants
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

class TicTacToe():

    def __init__(self):
        screen_size = [500,600]
        self.screen = pg.display.set_mode(screen_size)
        pg.display.set_caption("Torus Tic Tac Toe")
        self.clock = pg.time.Clock()
        
        self.board = Board(3)

        self.running=True
        self.loop()

    def loop(self):
        while self.running:
            self.clock.tick(20)

            self.process_user_input()
            self.render()
        pg.quit()
            
            
    def process_user_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running=False
                break
            elif event.type == pg.MOUSEBUTTONDOWN:
                if not self.board.game_over:
                    (x,y) = event.pos
                    self.board.apply_click(x,y)
                    print(self.board.board)

    def render(self):
        self.screen.fill(WHITE)
        self.board.render(self.screen)
        pg.display.flip()

game = TicTacToe()
    
    
