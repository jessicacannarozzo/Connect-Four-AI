import random
from anytree import Node, RenderTree, find_by_attr
import copy


class Node:
    def __init__(self, row, col, color, state=None, parent=None):
        self.row = row
        self.col = col
        self.color = color
        self.parent = parent
        self.state = state


class AI:
    def __init__(self, ai_method_choice, game_choice, board_rows, board_cols, ai_num, color, board):
        self.current_row = 5
        self.current_col = 3
        self.board_rows = board_rows
        self.board_cols = board_cols
        self.ai_method_choice = ai_method_choice
        self.game_choice = game_choice
        self.ai_num = ai_num
        self.color = color
        self.board = board
        self.path = []
        self.perceived = copy.deepcopy(self.board)
        # self.grid_tree = Node("5,0", row=5, col=0)

        if self.color is "PURPLE":
            self.other_color = "GREEN"
        else:
            self.other_color = "GREEN"

    # AI plays using math.random to generate which col it will put a counter in.
    # if playing the second version of connect four, it will also random decide if it will remove one of its counters
    def choose_random_moves(self):
        valid_move = False

        while valid_move is False:
            self.current_col = random.randint(0, self.board_cols-1)
            if self.board.is_col_full(self.current_col) is False:
                valid_move = True

    # update AI move
    def update_counter(self):
        if self.ai_method_choice is 0:
            self.choose_random_moves()
            # self.get_children(Node(self.current_row, self.current_col, self.color, None))
        elif self.ai_method_choice is 1:
            self.alpha_beta_search(copy.deepcopy(self.board))
            # self.current_col = self.heuristic_one(self.perceived, 4, -99999, 99999, True)[0]
            print(str(self.current_row) + ", " + str(self.current_col) + " hello")
        elif self.ai_method_choice is 2:
            self.heuristic_two()
        print("AI " + str(self.ai_num) + ": placing counter on column " + str(self.current_col))

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

    def alpha_beta_search(self, state):
        move = self.max_value(state, 4, -99999, 99999)
        print(str(move[0]) + " with value of " + str(move[1]))
        return move[0]

    # mini-max search with alpha beta pruning, heuristic one
    # https://www.youtube.com/watch?v=l-hh51ncgDI
    # https://github.com/Gimu/connect-four-js/blob/master/plain/alphabeta/js/connect-four.js
    def heuristic_one(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.game_over(state, self.color) or self.game_over(state, self.other_color) or state.is_full() is True:
            return self.eval_one(state)

        if maximizing_player:
            max_eval = [-1, -99999]
            children = self.get_children(state, self.other_color)
            for i, child in enumerate(children):
                eval_child = self.heuristic_one(child, depth - 1, alpha, beta, False)
                max_eval = [i, max(max_eval[1], eval_child[1])]
                alpha = max(alpha, eval_child[1])
                if beta <= alpha:
                    break
            return max_eval

        else:
            min_eval = [-1, 99999]
            children = self.get_children(state, self.color)
            for i, child in enumerate(children):
                eval_child = self.heuristic_one(child, depth - 1, alpha, beta, True)
                min_eval = [i, min(min_eval[1], eval_child[1])]
                beta = min(beta, eval_child[1])
                if beta <= alpha:
                    break
            return min_eval

    # mini-max search with alpha beta pruning, heuristic two
    # https://www.youtube.com/watch?v=l-hh51ncgDI
    def heuristic_two(self):
        pass

    # check if game is over i.e. if there is four in a row anywhere
    def game_over(self, temp_board, color):
        # check if horizontal win -
        for x in range(self.board_rows):
            for y in range(self.board_cols-3):
                # print(self.board.grid[x][y].color)
                if temp_board.grid[x][y].color is color:
                    if temp_board.grid[x][y+1].color is color and temp_board.grid[x][y+2].color is color and temp_board.grid[x][y+3].color is color:
                        return True

        # check if vertical win |
        for x in range(self.board_cols):
            for y in range(self.board_rows-3):
                if temp_board.grid[y][x].color is color:
                    if temp_board.grid[y+1][x].color is color and temp_board.grid[y+2][x].color is color and temp_board.grid[y+3][x].color is color:
                        return True

        # check diagonal \
        for x in range(self.board_rows-3):
            for y in range(self.board_cols-3):
                if temp_board.grid[x][y].color is color:
                    if temp_board.grid[x+1][y+1].color is color and temp_board.grid[x+2][y+2].color is color and temp_board.grid[x+3][y+3].color is color:
                        return True

        # check diagonal /
        for x in range(self.board_rows-3):
            for y in reversed(range(3, self.board_cols)):
                if temp_board.grid[x][y].color is color:
                    if temp_board.grid[x + 1][y - 1].color is color and temp_board.grid[x + 2][y - 2].color is color and temp_board.grid[x + 3][y - 3].color is color:
                        return True

    # input: parent node
    # def get_children(self, parent):
    #     children = []
    #     num_cols_full = 0
    #
    #     perceived = self.form_grid(parent)
    #
    #     if parent.color is "PURPLE":
    #         other_color = "GREEN"
    #     else:
    #         other_color = "PURPLE"
    #
    #     print("Parent: " + str(parent.row) + ", " + str(parent.col))
    #     for col in range(self.board_cols):
    #         for row in reversed(range(self.board_rows)):
    #             # if self.perceived.grid[row][col].color is None:
    #             if col is parent.col and row is parent.row and row-1 >= 0 and perceived.grid[row][col-1].has_counter() is False:
    #                 # children.append(Node(row-1, col, Node(parent.row, parent.col, other_color, parent)))
    #                 children.append(Node(row-1, col, other_color, parent))
    #                 break
    #             elif perceived.grid[row][col].has_counter() is False:
    #                 # children.append(Node(row, col, Node(parent.row, parent.col, other_color, parent)))
    #                 children.append(Node(row, col, other_color, parent))
    #                 break
    #             if perceived.is_col_full(col) is True:  # if we get to the end of the col without
    #                 num_cols_full += 1
    #                 break
    #
    #     print("Number of children is " + str(len(children)))
    #     print("Number of rows full is " + str(num_cols_full))
    #     for child in children:
    #         print(str(child.row) + ", " + str(child.col))
    #     return children

    # get board with child move
    def get_children(self, state, color):
        children_states = []
        num_cols_full = 0
        index = 0

        # print("Parent: " + str(parent.row) + ", " + str(parent.col))
        for col in range(self.board_cols):
            for row in reversed(range(self.board_rows)):
                if state.grid[row][col].has_counter() is False:
                    # children.append(Node(row, col, Node(parent.row, parent.col, other_color, parent)))
                    # children.append(Node(row, col, color, state))
                    children_states.append(copy.deepcopy(state))
                    children_states[index].add_counter(col, color)
                    index += 1
                    break
                if state.is_col_full(col) is True:  # if we get to the end of the col without
                    num_cols_full += 1
                    break

        print("Number of children is " + str(len(children_states)))
        print("Number of rows full is " + str(num_cols_full))
        for child in children_states:
            print(child.is_full() is False)
        return children_states

    # https://github.com/Gimu/connect-four-js/blob/master/plain/alphabeta/js/board.js
    # count how many counters of ours VS theirs there are
    def eval_one(self, state):
        total_points = 0

        if self.game_over(state, self.color):
            total_points += 1000
            return total_points
        elif self.game_over(state, self.other_color):
            total_points += -1000
            return total_points
        else:
            for row in reversed(range(self.board_rows)):
                for col in range(self.board_cols):
                    if state.grid[row][col].color is self.color:
                        total_points += 1
                    elif state.grid[row][col].color is self.other_color:
                        total_points -= 1

        print("Total points for this path: "+str(total_points))
        return total_points

    # form perceived grid
    def form_grid(self, position_node):
        grid = copy.deepcopy(self.board)

        while position_node is not None and grid.grid[position_node.row][position_node.col].has_counter() is False:
            grid.add_counter(position_node.col, position_node.color)
            position_node = position_node.parent
            # print(position_node.row)

        # output = []
        # print("Here it is!")
        # for row in range(self.board_rows):
        #     for col in range(self.board_cols):
        #         output.append(grid.grid[row][col].color)
        #
        # print(output)

        return grid

    def max_value(self, state, depth, alpha, beta):
        max_return = [None, -99999]
        if depth == 0 or self.game_over(state, self.color) or self.game_over(state, self.other_color) or state.is_full() is True:
            max_return[1] = self.eval_one(state)
            return max_return

        for a, successor in enumerate(self.get_children(state, self.color)):
            max_return = self.min_value(state, depth - 1, alpha, beta)
            if max_return[1] >= beta:
                return max_return
            alpha = max(alpha, max_return[1])
        return max_return

    def min_value(self, state, depth, alpha, beta):
        min_return = [None, 99999]
        if depth == 0 or self.game_over(state, self.color) or self.game_over(state, self.other_color) or state.is_full() is True:
            min_return[1] = self.eval_one(state)
            return min_return
        for a, successor in enumerate(self.get_children(state, self.other_color)):
            min_return = self.max_value(state, depth - 1, alpha, beta)
            if min_return[1] <= alpha:
                return min_return
            beta = min(beta, min_return[1])
        return min_return

