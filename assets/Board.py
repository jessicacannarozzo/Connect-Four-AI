from assets.Counter import Counter


class Board:
    def __init__(self, width, height):
        self.grid = [[0 for y in range(width)] for x in range(height)]

        for x in range(height):
            for y in range(width):
                self.grid[x][y] = (Counter(None))  # empty board

        self.width = width
        self.height = height

    # Change color of counter at index height,width
    # empty space => color = None
    def set_counter_color(self, height, width, color):
        self.grid[height][width].color = color

    # adds counter to bottom
    def add_counter(self, column, color):
        for x in reversed(range(self.height)):
            # print(str(x) + ", " + str(column))
            if self.grid[x][column].has_counter() is False:
                self.set_counter_color(x, column, color)
                # print(self.grid[x][column].color)
                return x

    def set_rect(self, height, width, rect):
        self.grid[height][width].set_rect = rect

    def is_full(self):
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y].has_counter() is False:
                    return False
        return True

    def is_col_full(self, col):
        # print(str(0) + ", " + str(col))
        # print(self.grid[0][col].color)
        if self.grid[0][col].has_counter() is True:
            return True
        else:
            return False

