class Counter:
    def __init__(self, color):
        self.color = color

    def has_counter(self):
        if self.color is not None:
            return True
        else:
            return False

