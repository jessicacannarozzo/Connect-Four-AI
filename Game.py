import pygame
from assets.Board import Board


class Game:

    def __init__(self):
        self.boardHeight = 6
        self.boardWidth = 7
        self.board = Board(self.boardWidth, self.boardHeight)
        self.player1Color = 'GREEN'
        self.player2Color = 'PURPLE'
        self.empty_slot_path = 'assets/images/empty-slot.png'
        self.player1_counter_path = 'assets/images/green-counter.png'
        self.player2_counter_path = 'assets/images/purple-counter.png'

    def main(self):
        pygame.init()
        pygame.display.set_caption("Connect Four: COMP4106 Style")
        screen = pygame.display.set_mode((1500, 1500))

        self.initialize_pygame(screen)
        self.create_board(screen)
        running = True

        while running:
            pygame.time.delay(50)

            # both AI make a move
            self.change_counter(screen, 2, 0, 2)
            self.change_counter(screen, 3, 0, 2)
            self.change_counter(screen, 1, 0, 2)
            self.change_counter(screen, 4, 0, 2)

            # check if game's over
            if self.check_win(screen, self.player1Color) is True:
                print("Green won the game!")
                self.board = Board(self.boardWidth, self.boardHeight)  # reset board
                self.create_board(screen)  # reset UI
            elif self.check_win(screen, self.player2Color) is True:
                print("Purple won the game!")
                self.board = Board(self.boardWidth, self.boardHeight)  # reset board
                self.create_board(screen)  # reset UI

            pygame.event.pump()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

            pygame.display.flip()

    def initialize_pygame(self, screen):
        screen.fill((253, 253, 253))
        pygame.font.init()
        f = pygame.font.SysFont('Arial', 20)
        textsurface = f.render("Connect Four: COMP4106 Style", True, (0, 0, 0))
        screen.blit(textsurface, (625, 40))
        pygame.display.flip()

    def create_board(self, screen):
        offset_x = 100
        offset_y = 100
        start_x = 400
        start_y = 80
        block_size = 10
        empty_slot = pygame.image.load(self.empty_slot_path).convert()

        for x in range(self.board.width):
            for y in range(self.board.height):
                rect = pygame.Rect(x*offset_x+start_x, y*offset_y+start_y, block_size, block_size)
                self.board.grid[y][x].set_rect(rect)
                screen.blit(empty_slot, rect)

        pygame.display.update()

    def change_counter(self, screen, x, y, player_num):
        if player_num == 1:
            green_slot = pygame.image.load(self.player1_counter_path).convert()
            self.board.set_counter_color(x, y, self.player1Color)
            # print(self.board.grid[x][y].color)
            screen.blit(green_slot, self.board.grid[x][y].rect)

        elif player_num == 2:
            purple_slot = pygame.image.load(self.player2_counter_path).convert()
            self.board.set_counter_color(x, y, self.player2Color)
            screen.blit(purple_slot, self.board.grid[x][y].rect)

        pygame.display.update()

    # check if a player has four in a row: | - / \
    def check_win(self, screen, color):
        # check if horizontal win -
        for x in range(self.board.height):
            for y in range(self.board.width-3):
                # print(self.board.grid[x][y].color)
                if self.board.grid[x][y].color is color:
                    if self.board.grid[x][y+1].color is color and self.board.grid[x][y+2].color is color and self.board.grid[x][y+3].color is color:
                        return True

        # check if vertical win |
        for x in range(self.board.width):
            for y in range(self.board.height-3):
                if self.board.grid[y][x].color is color:
                    if self.board.grid[y+1][x].color is color and self.board.grid[y+2][x].color is color and self.board.grid[y+3][x].color is color:
                        return True


if __name__ == "__main__":
    g = Game()
    g.main()

