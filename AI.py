# Author: Jess Cannarozzo
# sources:
# https://github.com/Gimu/connect-four-js/blob/master/plain/alphabeta/js/connect-four.js
# https://www.youtube.com/watch?v=l-hh51ncgDI
# https://www.youtube.com/watch?v=y7AKtWGOPAE

import random
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
        # self.current_row = -1
        self.current_col = -1
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
            self.other_color = "PURPLE"


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
            self.current_col = self.alpha_beta_search(copy.deepcopy(self.board))
        elif self.ai_method_choice is 2:
            self.current_col = self.alpha_beta_search_two(copy.deepcopy(self.board))
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

    def alpha_beta_search_two(self, state):
        move = self.max_value_two(state, 4, -99999, 99999)
        print(str(move[0]) + " with value of " + str(move[1]))
        return move[0]

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

    # get board with child move
    def get_children(self, state, color):
        children_states = {}  # col num : grid
        num_cols_full = 0

        # print("Parent: " + str(parent.row) + ", " + str(parent.col))
        for col in range(self.board_cols):
            for row in reversed(range(self.board_rows)):
                if state.is_col_full(col) is True:  # if we get to the end of the col without
                    print(str(col) + "YO")
                    num_cols_full += 1
                    break
                if state.grid[row][col].has_counter() is False:
                    # children.append(Node(row, col, Node(parent.row, parent.col, other_color, parent)))
                    # children.append(Node(row, col, color, state))
                    children_states[col] = copy.deepcopy(state)
                    children_states[col].add_counter(col, color)
                    break

        print("Number of children is " + str(len(children_states)))
        print("Number of rows full is " + str(num_cols_full))
        # for child in children_states:
        #     print(child.is_full() is False)
        return children_states

    # https://github.com/Gimu/connect-four-js/blob/master/plain/alphabeta/js/board.js
    # https://www.youtube.com/watch?v=y7AKtWGOPAE
    # count how many counters of ours VS theirs there are
    def eval_one(self, state):
        total_points = 0
        output = []
        for row in range(self.board_rows):
            output.append("\n")
            for col in range(self.board_cols):
                output.append(state.grid[row][col].color)

        print(str(output) + "FINAL")

        if self.game_over(state, self.color):
            total_points += 1000
            return total_points
        elif self.game_over(state, self.other_color):
            total_points += -1000
            return total_points
        else:
            # check if adjacent nodes horizontally
            for x in range(self.board_rows):
                for y in range(self.board_cols - 2):
                    if state.grid[x][y].color is self.color:
                        if state.grid[x][y + 1].color is self.color:
                            total_points += 2
                            if state.grid[x][y + 2].color is self.color:
                                total_points += 5
                        if y == int(self.board_cols/2):
                            total_points += 4
                    elif state.grid[x][y].color is self.other_color:
                        if state.grid[x][y + 1].color is self.other_color:
                            total_points -= 2
                            if state.grid[x][y + 2].color is self.other_color:
                                total_points -= 100

            # check if adjacent nodes vertically
            for x in range(self.board_cols):
                for y in range(self.board_rows - 2):
                    num_adjacent = 0
                    if state.grid[y][x].color is self.color:
                        num_adjacent += 1
                        if state.grid[y + 1][x].color is self.color:
                            num_adjacent += 1
                            total_points += 2
                            if state.grid[y + 2][x].color is self.color:
                                num_adjacent += 1
                                total_points += 5
                        if y == int(self.board_cols/2):
                            # or y+1 == int(self.board_cols/2) or y+2 == int(self.board_cols/2):
                            total_points += 4*num_adjacent
                    elif state.grid[y][x].color is self.other_color:
                        if state.grid[y + 1][x].color is self.other_color:
                            total_points -= 2
                            if state.grid[y + 2][x].color is self.other_color:
                                total_points -= 100

            # check diagonal \
            for x in range(self.board_rows - 2):
                for y in range(self.board_cols - 2):
                    if state.grid[x][y].color is self.color:
                        if state.grid[x + 1][y + 1].color is self.color:
                            total_points += 2
                            if y+1 == int(self.board_cols/2):
                                total_points += 4
                            if state.grid[x + 2][y + 2].color is self.color:
                                total_points += 5
                                if y+2 == int(self.board_cols/2):
                                    total_points += 4
                        if y == int(self.board_cols/2):
                            total_points += 4
                    elif state.grid[x][y].color is self.other_color:
                        if state.grid[x + 1][y + 1].color is self.other_color:
                            total_points -= 2
                            if state.grid[x + 2][y + 2].color is self.other_color:
                                total_points -= 100

            # check diagonal /
            for x in range(self.board_rows - 2):
                for y in reversed(range(2, self.board_cols)):
                    if state.grid[x][y].color is self.color:
                        if state.grid[x + 1][y - 1].color is self.color:
                            total_points += 2
                            if y - 1 == int(self.board_cols/2):
                                total_points += 4
                            if state.grid[x + 2][y - 2].color is self.color:
                                total_points += 5
                                if y - 2 == int(self.board_cols/2):
                                    total_points += 4
                        if y == int(self.board_cols/2):
                            total_points += 4
                    elif state.grid[x][y].color is self.other_color:
                        if state.grid[x + 1][y - 1].color is self.other_color:
                            total_points -= 2
                            if state.grid[x + 2][y - 2].color is self.color:
                                total_points -= 100

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

    # get max value for mini max search with alpha-beta pruning: heuristic one
    def max_value(self, state, depth, alpha, beta):
        max_return = [None, -99999]
        if depth == 0 or self.game_over(state, self.color) or self.game_over(state, self.other_color) or state.is_full() is True:
            max_return[1] = self.eval_one(state)
            return max_return

        child_dict = self.get_children(state, self.color)
        for successor_col in list(child_dict):
            new_move = self.min_value(child_dict[successor_col], depth - 1, alpha, beta)
            # max_return[0] = a
            if max_return[0] is None or new_move[1] > max_return[1]:
                max_return[0] = successor_col
                max_return[1] = new_move[1]
                alpha = new_move[1]

            if alpha >= beta:
                return max_return
        # print("HELLO" + str(max_return))
        return max_return

    # get min value for mini max search with alpha-beta pruning: heuristic one
    def min_value(self, state, depth, alpha, beta):
        min_return = [None, 99999]
        if depth == 0 or self.game_over(state, self.color) or self.game_over(state, self.other_color) or state.is_full() is True:
            min_return[1] = self.eval_one(state)
            return min_return

        child_dict = self.get_children(state, self.other_color)
        for successor_col in list(child_dict):
            new_move = self.max_value(child_dict[successor_col], depth - 1, alpha, beta)
            if min_return[0] is None or new_move[1] < min_return[1]:
                min_return[0] = successor_col
                min_return[1] = new_move[1]
                beta = new_move[1]
            if alpha >= beta:
                return min_return
        return min_return

    # get max value for mini max search with alpha-beta pruning: heuristic two
    def max_value_two(self, state, depth, alpha, beta):
        max_return = [None, -99999]
        if depth == 0 or self.game_over(state, self.color) or self.game_over(state, self.other_color) or state.is_full() is True:
            max_return[1] = self.eval_two(state)
            return max_return

        child_dict = self.get_children(state, self.color)
        for successor_col in list(child_dict):
            new_move = self.min_value_two(child_dict[successor_col], depth - 1, alpha, beta)
            # max_return[0] = a
            if max_return[0] is None or new_move[1] > max_return[1]:
                max_return[0] = successor_col
                max_return[1] = new_move[1]
                alpha = new_move[1]

            if alpha >= beta:
                return max_return
        return max_return

    # get min value for mini max search with alpha-beta pruning: heuristic two
    def min_value_two(self, state, depth, alpha, beta):
        min_return = [None, 99999]
        if depth == 0 or self.game_over(state, self.color) or self.game_over(state, self.other_color) or state.is_full() is True:
            min_return[1] = self.eval_two(state)
            return min_return

        child_dict = self.get_children(state, self.other_color)
        for successor_col in list(child_dict):
            new_move = self.max_value_two(child_dict[successor_col], depth - 1, alpha, beta)
            if min_return[0] is None or new_move[1] < min_return[1]:
                min_return[0] = successor_col
                min_return[1] = new_move[1]
                beta = new_move[1]
            if alpha >= beta:
                return min_return
        return min_return

    # like eval one, but puts more emphasis on the AI playing defensively. It also does not have any preference towards the center of the board
    def eval_two(self, state):
        total_points = 0
        output = []
        for row in range(self.board_rows):
            output.append("\n")
            for col in range(self.board_cols):
                output.append(state.grid[row][col].color)

        if self.game_over(state, self.color):
            total_points += 1000
            return total_points
        elif self.game_over(state, self.other_color):
            total_points += -1000
            return total_points
        else:
            # check if adjacent nodes horizontally
            for x in range(self.board_rows):
                for y in range(self.board_cols - 2):
                    if state.grid[x][y].color is self.color:
                        if state.grid[x][y + 1].color is self.color:
                            total_points += 2
                            if state.grid[x][y + 2].color is self.color:
                                total_points += 5
                    elif state.grid[x][y].color is self.other_color:
                        if state.grid[x][y + 1].color is self.other_color:
                            total_points -= 5
                            if state.grid[x][y + 2].color is self.other_color:
                                total_points -= 100

            # check if adjacent nodes vertically
            for x in range(self.board_cols):
                for y in range(self.board_rows - 2):
                    if state.grid[y][x].color is self.color:
                        if state.grid[y + 1][x].color is self.color:
                            total_points += 2
                            if state.grid[y + 2][x].color is self.color:
                                total_points += 5
                    elif state.grid[y][x].color is self.other_color:
                        if state.grid[y + 1][x].color is self.other_color:
                            total_points -= 2
                            if state.grid[y + 2][x].color is self.other_color:
                                total_points -= 100

            # check diagonal \
            for x in range(self.board_rows - 2):
                for y in range(self.board_cols - 2):
                    if state.grid[x][y].color is self.color:
                        if state.grid[x + 1][y + 1].color is self.color:
                            total_points += 2
                            if state.grid[x + 2][y + 2].color is self.color:
                                total_points += 5
                    elif state.grid[x][y].color is self.other_color:
                        if state.grid[x + 1][y + 1].color is self.other_color:
                            total_points -= 2
                            if state.grid[x + 2][y + 2].color is self.other_color:
                                total_points -= 100

            # check diagonal /
            for x in range(self.board_rows - 2):
                for y in reversed(range(2, self.board_cols)):
                    if state.grid[x][y].color is self.color:
                        if state.grid[x + 1][y - 1].color is self.color:
                            total_points += 2
                            if state.grid[x + 2][y - 2].color is self.color:
                                total_points += 5
                    elif state.grid[x][y].color is self.other_color:
                        if state.grid[x + 1][y - 1].color is self.other_color:
                            total_points -= 2
                            if state.grid[x + 2][y - 2].color is self.color:
                                total_points -= 100

        print("Total points for this path: "+str(total_points))
        return total_points

