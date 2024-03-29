'''
This is the main driver file.
It will be responsible for handling user input and siplaying the current GameState object.
'''

#--------------------------------------------------
'''
Loading dependencies
'''
import pygame as p
from Chess import ChessEngine

#--------------------------------------------------
'''
Initializing global variables
'''
WIDTH = HEIGHT = 512 # 400 is another option, but larger might be an option later
DIMENSION = 8 # dimensions of a chess board are 8x8, might be extended later (e.g. 10x10 or four-players)
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animations later
IMAGES = {}

#--------------------------------------------------
'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK'] # insert dark knight joke here
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))
        # Note: we can access an image by saying 'IMAGES['wp']'

#--------------------------------------------------        
'''
The main driver for our code. This will handle user input and updating the graphics.
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() # only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

#--------------------------------------------------
'''
Responsibe for all the graphics within a current game state.
'''
def drawGameState(screen, gs):
    drawBoard(screen) # draw squares on the board
    drawPieces(screen, gs.board) # draw pieces on top of those squares

#--------------------------------------------------
'''
Draw the squares on the board. The top left square is always light.
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
#--------------------------------------------------
'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # not an empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

#--------------------------------------------------
'''
Actually run the code
'''
if __name__ == "__main__":
    main()