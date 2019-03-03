class Board:
    def __init__(self, width, height):
        self.grid = [[0 for y in range(height)] for x in range(width)]
        self.width = width
        self.height = height
