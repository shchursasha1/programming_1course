import random
from src.abstract_object import Object
from src.constants import VERTICAL, HORIZONT

class Ship(Object):
    """
    Class represents a ship on the map.
    """

    def __init__(self, position: tuple, orient: int, size: int) -> None:
        super().__init__(position)
        self.size = size
        self.orient = orient
        self.health = size

    def get_body(self):
        if self.orient == VERTICAL:
            for i in range(self.size):
                yield self.position[0] + i, self.position[1]
        elif self.orient == HORIZONT:
            for i in range(self.size):
                yield self.position[0], self.position[1] + i

    def get_area(self):
        if self.orient == VERTICAL:
            x1, x2 = self.position[0] - 1, self.position[0] + self.size + 1
            y1, y2 = self.position[1] - 1, self.position[1] + 2
        elif self.orient == HORIZONT:
            x1, x2 = self.position[0] - 1, self.position[0] + 2
            y1, y2 = self.position[1] - 1, self.position[1] + self.size + 1

        for x in range(x1, x2):
            for y in range(y1, y2):
                yield (x, y)

    def get_hit(self):
        self.health -= 1

    @classmethod
    def generate(cls, shape: tuple, size):
        max_x, max_y = shape
        x, y = random.randrange(max_x), random.randrange(max_y)
        orient = random.choice([HORIZONT, VERTICAL])
        return cls((x,y), orient=orient, size=size)

    def __repr__(self) -> str:
        return f'Ship({self.size})'