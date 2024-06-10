import random
from src.abstract_object import Object

class Mine(Object):
    """
    Class represents a mine on the map.
    """
    def __init__(self, position: tuple):
        super().__init__(position)

    def get_body(self):
        yield (self.position[0], self.position[1])

    def get_area(self):
        for i in [0, 1, -1]:
            for j in [0, 1, -1]:
                yield (self.position[0] + i, self.position[1] + j)

    @classmethod
    def generate(cls, shape: tuple):
        max_x, max_y = shape
        x, y = random.randrange(max_x), random.randrange(max_y)
        return cls((x, y))

    def __repr__(self):
        return 'Mine'