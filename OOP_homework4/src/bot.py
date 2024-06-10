import random
from src.player import Player
from src.map import Map
from src.ship import Ship
from src.mine import Mine

class Bot(Player):
    """
    Class represents a bot in the game.
    """

    def __init__(self, map: Map):
        self.map = map

    def fill_map(self):
        self.map = Map.generate(self.map.shape)

    def do_attack(self, other):
        max_x, max_y = self.map.shape
        x, y = random.randrange(max_x), random.randrange(max_y)
        while self.map._misses[x][y]:
            max_x, max_y = self.map.shape
            x, y = random.randrange(max_x), random.randrange(max_y)

        if isinstance(other.map._objects[x][y], Ship):
            other.map._objects[x][y].get_hit()
            other.map._misses[x][y] = 1
        elif isinstance(other.map._objects[x][y], Mine):
            other.map._misses[x][y] = 1
            for (i, j) in other.map._objects[x][y].get_area():
                if isinstance(self.map._objects[i][j], Ship):
                    self.map._objects[i][j].get_hit()
                    self.map._misses[i][j] = 1
                else:
                    self.map._misses[i][j] = 1
        else:
            other.map._misses[x][y] = 1

    def place_ships(self):
        pass

    def place_mines(self):
        pass