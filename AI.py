import random

class AI:
    def __init__(self, ai_method_choice, game_choice, board_rows, board_cols, color):
        self.current_row = -1
        self.current_col = -1
        self.board_rows = board_rows
        self.board_cols = board_cols
        self.ai_method_choice = ai_method_choice
        self.game_choice = game_choice
        self.color = color

        self.update_row()

    # AI plays using math.random to generate which col it will put a counter in.
    # if playing the second version of connect four, it will also random decide if it will remove one of its counters
    def choose_random_moves(self):
        self.current_col = random.randint(0, self.board_cols)
        print(self.current_col)


    def update_row(self):
        if self.ai_method_choice is 0:
            self.choose_random_moves()
