import pygame
from assets.Board import Board
from AI import AI
import time


class Game:

    def __init__(self):
        # 0: play option 1 of game, 1: play option 2 of game where players are allowed to remove pieces from the bottom
        self.gameChoice = 0
        self.first_ai_method_choice = 1
        self.second_ai_method_choice = 2

        self.boardHeight = 6
        self.boardWidth = 7
        self.board = Board(self.boardWidth, self.boardHeight)
        self.player1Color = 'GREEN'
        self.player2Color = 'PURPLE'
        self.empty_slot_path = 'assets/images/empty-slot.png'
        self.player1_counter_path = 'assets/images/green-counter.png'
        self.player2_counter_path = 'assets/images/purple-counter.png'
        self.is_human = 0  # 0 for false, 1 for true

    def main(self):
        self.is_human = int(input("0: AI or 1:Human?"))
        pygame.init()
        pygame.display.set_caption("Connect Four: COMP4106 Style")
        screen = pygame.display.set_mode((1500, 1500))
        wait_time = 10


        self.initialize_pygame(screen)
        self.create_board(screen)
        running = True
        ai_one = AI(self.first_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 1, self.player1Color, self.board)
        ai_two = AI(self.second_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 2, self.player2Color, self.board)

        purple_win = 0
        green_win = 0
        tie = 0
        # self.add_counter(screen, 4, 1)
        # self.add_counter(screen, 4, 2)
        # self.add_counter(screen, 4, 1)
        # self.add_counter(screen, 4, 2)

        while running:
            pygame.time.delay(50)

            # both AI make a move
            ai_one.update_counter()
            self.add_counter(screen, ai_one.current_col, 1)

            if self.is_human == 0:
                ai_two.update_grid(self.board)

            # check if game's over
            if self.check_win(self.player1Color) is True:
                print("Green won the game!")
                green_win += 1
                self.board = Board(self.boardWidth, self.boardHeight)  # reset board
                ai_one = AI(self.first_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 1, self.player1Color, self.board)
                ai_two = AI(self.second_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 2, self.player2Color, self.board)
                time.sleep(wait_time)
                self.create_board(screen)  # reset UI
            elif self.check_win(self.player2Color) is True:
                print("Purple won the game!")
                purple_win += 1
                self.board = Board(self.boardWidth, self.boardHeight)  # reset board
                ai_one = AI(self.first_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 1, self.player1Color, self.board)
                ai_two = AI(self.second_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 2, self.player2Color, self.board)
                time.sleep(wait_time)
                self.create_board(screen)  # reset UI
            elif self.board.is_full() is True:
                print("Tie game, all spaces are filled.")
                tie += 1
                self.board = Board(self.boardWidth, self.boardHeight)  # reset board
                ai_one = AI(self.first_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 1, self.player1Color, self.board)
                ai_two = AI(self.second_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 2, self.player2Color, self.board)
                time.sleep(wait_time)
                self.create_board(screen)  # reset UI

            if self.is_human == 0:
                ai_two.update_counter()
                self.add_counter(screen, ai_two.current_col, 2)
            else:
                print(str(self.is_human))
                self.add_counter(screen, int(input("Enter a col")), 2)

            ai_one.update_grid(self.board)

            # if self.gameChoice is 1:
            #     self.board.grid = self.remove_from_bottom(screen, 4, self.player1Color, self.board.grid)

            # check if game's over
            if self.check_win(self.player1Color) is True:
                print("Green won the game!")
                green_win += 1
                self.board = Board(self.boardWidth, self.boardHeight)  # reset board
                ai_one = AI(self.first_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 1, self.player1Color, self.board)
                ai_two = AI(self.second_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 2, self.player2Color, self.board)
                time.sleep(wait_time)
                self.create_board(screen)  # reset UI
            elif self.check_win(self.player2Color) is True:
                print("Purple won the game!")
                purple_win += 1
                self.board = Board(self.boardWidth, self.boardHeight)  # reset board
                ai_one = AI(self.first_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 1, self.player1Color, self.board)
                ai_two = AI(self.second_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 2, self.player2Color, self.board)
                time.sleep(wait_time)
                self.create_board(screen)  # reset UI
            elif self.board.is_full() is True:
                print("Tie game, all spaces are filled.")
                tie += 1
                self.board = Board(self.boardWidth, self.boardHeight)  # reset board
                ai_one = AI(self.first_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 1, self.player1Color, self.board)
                ai_two = AI(self.second_ai_method_choice, self.gameChoice, self.boardHeight, self.boardWidth, 2, self.player2Color, self.board)
                time.sleep(wait_time)
                self.create_board(screen)  # reset UI
            pygame.event.pump()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                print("\n\n")
                print("Player 1 (Green) has won: " + str(green_win) + " out of " + str(green_win+purple_win+tie) + " games.")
                print("Player 2 (Purple) has won: " + str(purple_win) + " out of " + str(green_win+purple_win+tie) + " games.")
                print("Number of ties: " + str(tie) + " out of " + str(green_win+purple_win+tie) + " games.")

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

    def remove_from_bottom(self, screen, col, color, grid):
        empty_slot = pygame.image.load(self.empty_slot_path).convert()
        green_slot = pygame.image.load(self.player1_counter_path).convert()
        purple_slot = pygame.image.load(self.player2_counter_path).convert()

        if self.board.grid[self.boardHeight-1][col].color is color:  # it is the right color
            # move all elements down
            for row in reversed(range(self.boardWidth-1)):
                if self.board.grid[row-1][col].color is self.player1Color:
                    screen.blit(green_slot, self.board.grid[row][col].rect)
                elif self.board.grid[row-1][col].color is self.player2Color:
                    screen.blit(purple_slot, self.board.grid[row][col].rect)
                else:
                    screen.blit(empty_slot, self.board.grid[row][col].rect)

                if row == 0:
                    screen.blit(empty_slot, self.board.grid[row][col].rect)

                new_color = self.board.grid[row-1][col].color
                self.board.grid[row][col].color = new_color
                pygame.display.update()

        return grid

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

    def add_counter(self, screen, col, player_num):
        if player_num == 1:
            green_slot = pygame.image.load(self.player1_counter_path).convert()
            x = self.board.add_counter(col, self.player1Color)
            self.board.grid[x][col].color = self.player1Color
            screen.blit(green_slot, self.board.grid[x][col].rect)

        elif player_num == 2:
            purple_slot = pygame.image.load(self.player2_counter_path).convert()
            x = self.board.add_counter(col, self.player2Color)
            self.board.grid[x][col].color = self.player2Color
            screen.blit(purple_slot, self.board.grid[x][col].rect)

        pygame.display.update()

    # check if a player has four in a row: | - / \
    def check_win(self, color):
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

        # check diagonal \
        for x in range(self.board.height-3):
            for y in range(self.board.width-3):
                if self.board.grid[x][y].color is color:
                    if self.board.grid[x+1][y+1].color is color and self.board.grid[x+2][y+2].color is color and self.board.grid[x+3][y+3].color is color:
                        return True

        # check diagonal /
        for x in range(self.board.height-3):
            for y in reversed(range(3, self.board.width)):
                if self.board.grid[x][y].color is color:
                    if self.board.grid[x + 1][y - 1].color is color and self.board.grid[x + 2][y - 2].color is color and self.board.grid[x + 3][y - 3].color is color:
                        return True


if __name__ == "__main__":
    g = Game()
    g.main()

