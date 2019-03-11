import random
from anytree import Node, RenderTree, find_by_attr


class Node:
    def __init__(self, row, col, parent):
        self.row = row
        self.col = col
        self.parent = parent


class AI:
    def __init__(self, ai_method_choice, game_choice, board_rows, board_cols, ai_num, color, board):
        self.current_row = 5
        self.current_col = 0
        self.board_rows = board_rows
        self.board_cols = board_cols
        self.ai_method_choice = ai_method_choice
        self.game_choice = game_choice
        self.ai_num = ai_num
        self.color = color
        self.board = board
        self.path = []
        self.perceived = board
        # self.grid_tree = Node("5,0", row=5, col=0)

    # AI plays using math.random to generate which col it will put a counter in.
    # if playing the second version of connect four, it will also random decide if it will remove one of its counters
    def choose_random_moves(self):
        valid_move = False

        while valid_move is False:
            self.current_col = random.randint(0, self.board_cols-1)
            if self.board.is_col_full(self.current_col) is False:
                valid_move = True
        print("AI " + str(self.ai_num) + ": placing counter on column " + str(self.current_col))

    # update AI move
    def update_counter(self):
        if self.ai_method_choice is 0:
            self.choose_random_moves()
            self.get_children(Node(self.current_row, self.current_col, None))
        elif self.ai_method_choice is 1:
            # self.form_tree()
            # self.heuristic_one()
            self.perceived.grid[self.current_row][self.current_col].color = self.color
            self.get_children(Node(self.current_row, self.current_col, None))
        elif self.ai_method_choice is 2:
            self.heuristic_two()

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

    # mini-max search with alpha beta pruning, heuristic one
    # https://www.youtube.com/watch?v=l-hh51ncgDI
    def heuristic_one(self, pos_row, pos_col, depth, alpha, beta, max_player):
        if depth == 0 or self.game_over():
            return self.eval_one(pos_row, pos_col)

        self.perceived_board.grid.add_counter(pos_col, self.color)

        if max_player is True:
            max_eval = float("inf")
            # for each child
            child = self.get_children()

        else:
            min_eval = -float("inf")

    # mini-max search with alpha beta pruning, heuristic two
    # https://www.youtube.com/watch?v=l-hh51ncgDI
    def heuristic_two(self):
        pass

    # check if game is over i.e. if there is four in a row anywhere
    def game_over(self):
        return False

    def eval_one(self, pos_row, pos_col):
        pass

    # input: parent node
    def get_children(self, parent):
        children = []
        num_cols_full = 0

        print("Parent: " + str(parent.row) + ", " + str(parent.col))
        for col in range(self.board_cols):
            for row in reversed(range(self.board_rows)):
                # if self.perceived.grid[row][col].color is None:
                if col is parent.col and row is parent.row:
                    children.append(Node(row-1, col, Node(parent.row, parent.col, parent)))
                    break
                elif self.perceived.grid[row][col].has_counter() is False:
                    children.append(Node(row, col, Node(parent.row, parent.col, parent)))
                    break
                if self.perceived.is_col_full(col) is True:  # if we get to the end of the col without
                    num_cols_full += 1
                    break

        print("Number of children is " + str(len(children)))
        print("Number of rows full is " + str(num_cols_full))
        for child in children:
            print(str(child.row) + ", " + str(child.col))
        return children
