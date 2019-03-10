import random

class AI:
    def __init__(self, ai_method_choice, game_choice, board_rows, board_cols, ai_num, color, board):
        self.current_row = 0
        self.current_col = 0
        self.board_rows = board_rows
        self.board_cols = board_cols
        self.ai_method_choice = ai_method_choice
        self.game_choice = game_choice
        self.ai_num = ai_num
        self.color = color
        self.board = board

    # AI plays using math.random to generate which col it will put a counter in.
    # if playing the second version of connect four, it will also random decide if it will remove one of its counters
    def choose_random_moves(self):
        valid_move = False
        # if self.board.is_col_full(0) is False:
        #     self.current_col = 0
        #

        while valid_move is False:
            self.current_col = random.randint(0, self.board_cols-1)
            if self.board.is_col_full(self.current_col) is False:
                valid_move = True

            if valid_move is False:
                print("Finding a new current col")
                print("Attempted col: " + str(self.current_col))

        print("AI " + str(self.ai_num) + ": placing counter on column " + str(self.current_col))

    # update AI move
    def update_counter(self):
        if self.ai_method_choice is 0:
            self.choose_random_moves()

    def update_grid(self, board):
        print("AI " + str(self.ai_num) + ": board updated!")
        self.print_board()
        self.board = board
        self.print_board()

    def print_board(self):
        output = []
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                output.append(self.board.grid[row][col].color)

        print(output)
