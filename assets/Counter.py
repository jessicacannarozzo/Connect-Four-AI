class Counter:
    def __init__(self, color):
        self.color = color
        self.rect = None

    def has_counter(self):
        if self.color is not None:
            return True
        else:
            return False

    def set_rect(self, rect):
        self.rect = rect

