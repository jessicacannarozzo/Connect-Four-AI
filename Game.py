import pygame
from assets.Board import Board

boardHeight = 6
boardWidth = 7
board = Board(boardWidth, boardHeight)
player1Color = 'GREEN'
player2Color = 'PURPLE'
empty_slot_path = 'assets/images/empty-slot.png'
player1_counter_path = 'assets/images/green-counter.png'
player2_counter_path = 'assets/images/purple-counter.png'


def main():
    pygame.init()
    pygame.display.set_caption("Connect Four: COMP4106 Style")
    screen = pygame.display.set_mode((1500, 1500))

    initialize_pygame(screen)
    create_board(screen)
    running = True

    while running:
        pygame.time.delay(50)

        change_counter(screen, 2, 2, 2)
        change_counter(screen, 2, 0, 1)
        change_counter(screen, 2, 1, 1)
        change_counter(screen, 1, 2, 1)

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
    empty_slot = pygame.image.load(empty_slot_path).convert()

    for x in range(board.width):
        for y in range(board.height):
            rect = pygame.Rect(x*offset_x+start_x, y*offset_y+start_y, block_size, block_size)
            board.grid[y][x].set_rect(rect)
            screen.blit(empty_slot, rect)

    pygame.display.update()


def change_counter(screen, x, y, player_num):
    if player_num is 1:
        green_slot = pygame.image.load(player1_counter_path).convert()
        board.grid[x][y].set_color = player1Color
        screen.blit(green_slot, board.grid[x][y].rect)

    elif player_num is 2:
        purple_slot = pygame.image.load(player2_counter_path).convert()
        board.grid[x][y].set_color = player2Color
        screen.blit(purple_slot, board.grid[x][y].rect)

    pygame.display.update()


if __name__ == "__main__":
    main()


