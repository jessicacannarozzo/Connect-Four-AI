import pygame
from assets.Board import Board

boardHeight = 6
boardWidth = 7
board = Board(boardWidth, boardHeight)


def main():
    initializePygame()
    createBoard()
    running = True

    while running:
        pygame.display.update()
        pygame.time.delay(50)
        pygame.event.pump()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False


def initializePygame():
    pygame.init()
    pygame.display.set_caption("Connect Four: COMP4106 Style")
    screen = pygame.display.set_mode((1500, 1500))
    screen.fill((253, 253, 253))
    pygame.font.init()
    f = pygame.font.SysFont('Arial', 20)
    textsurface = f.render("Connect Four: COMP4106 Style", True, (0, 0, 0))
    screen.blit(textsurface, (625, 40))
    pygame.display.flip()


def createBoard():
    offsetX = 475
    offsetY = 125
    block_size = 30
    x = 50
    y = 50
    image = pygame.image.load("assets/images/empty-slot.png")
    # for x in range(board.height):
    #     for y in range(board.width):
    #         board[x][y] =

if __name__ == "__main__":
    main()


