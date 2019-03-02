import pygame
from assets.Board import Board

boardHeight = 6
boardWidth = 7
board = Board(boardWidth, boardHeight)


def main():
    pygame.init()
    pygame.display.set_caption("Connect Four: COMP4106 Style")
    screen = pygame.display.set_mode((1500, 1500))

    initialize_pygame(screen)
    create_board(screen)
    running = True

    while running:
        pygame.display.update()
        pygame.time.delay(50)
        pygame.event.pump()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

        pygame.display.flip()


def initialize_pygame(screen):
    screen.fill((253, 253, 253))
    pygame.font.init()
    f = pygame.font.SysFont('Arial', 20)
    textsurface = f.render("Connect Four: COMP4106 Style", True, (0, 0, 0))
    screen.blit(textsurface, (625, 40))
    pygame.display.flip()


def create_board(screen):
    offset_x = 100
    offset_y = 100
    start_x = 400
    start_y = 80
    block_size = 10
    image = pygame.image.load('assets/images/empty-slot.png').convert()

    for x in range(board.width):
        for y in range(board.height):
            rect = pygame.Rect(x*offset_x+start_x, y*offset_y+start_y, block_size, block_size)
            # board.grid[x][y] = screen.blit(image, rect)
            screen.blit(image, rect)

    pygame.display.update()


if __name__ == "__main__":
    main()


