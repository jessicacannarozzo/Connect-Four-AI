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
    def set(self, height, width, color):
        self.grid[height][width] = Counter(color)

