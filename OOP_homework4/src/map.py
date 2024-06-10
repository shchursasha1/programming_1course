from src.abstract_object import Object
from src.ship import Ship
from src.mine import Mine

class Map:
    """
    Class represents a map of the game.
    """

    config = {
        'ships': {
            1: 4,
            2: 3,
            3: 2,
            4: 1
        },
        'mines': 2
    }

    def __init__(self, shape) -> None:
        self.shape = shape
        self._list_objects = []
        self._objects = [[None] * self.shape[1] for _ in range(self.shape[0])]
        self._misses = [[0] * self.shape[1] for _ in range(self.shape[0])]
        self._areas = [[None] * self.shape[1] for _ in range(self.shape[0])]
        self._occupied = [[0] * self.shape[1] for _ in range(self.shape[0])]
        self.ships_list = []

    def add_ship(self, ship: Ship):
        for x, y in ship.get_body():
            if x < 0 or x >= self.shape[0]:
                raise ValueError()
            if y < 0 or y >= self.shape[1]:
                raise ValueError()
        for x, y in ship.get_area():
            if 0 <= x < self.shape[0] and 0 <= y < self.shape[1] and isinstance(self._objects[x][y], (Ship, Mine)):
                raise ValueError()

        self._add_object(ship, area_occupied=True)
        self.ships_list.append(ship)

    def add_mine(self, mine: Mine):
        for x, y in mine.get_body():
            if x < 0 or x >= self.shape[0]:
                raise ValueError()
            if y < 0 or y >= self.shape[1]:
                raise ValueError()
            if isinstance(self._objects[x][y], (Ship, Mine)):
                raise ValueError()

        self._add_object(mine, area_occupied=True)

    def _add_object(self, obj: Object, area_occupied=False):
        for x, y in obj.get_body():
            self._occupied[x][y] = 1
            self._objects[x][y] = obj
            
        for x,y in obj.get_area():
            if isinstance(obj, Mine):
                break
            if area_occupied:
                if x < 0 or x >= self.shape[0]: continue
                if y < 0 or y >= self.shape[1]: continue
                self._occupied[x][y] = 1
            self._areas[x][y] = obj
        self._list_objects.append(obj)

    def clean_list(self):
        copy_list = self.ships_list.copy()
        index = []
        for i in range(len(copy_list)):
            if self.ships_list[i].health == 0:
                index.append(i)
            else:
                pass
        for i in index:
            self.ships_list.pop(i)

    def clc(self):
        self.shape = self.shape
        self._list_objects = []
        self._objects = [[None] * self.shape[1] for _ in range(self.shape[0])]
        self._misses = [[0] * self.shape[1] for _ in range(self.shape[0])]
        self._areas = [[None] * self.shape[1] for _ in range(self.shape[0])]
        self._occupied = [[0] * self.shape[1] for _ in range(self.shape[0])]

    @classmethod
    def generate(cls, shape, max_tries=1000):
        map = cls(shape)

        while True:
            try:
                for size, amount in cls.config['ships'].items():
                    for _ in range(amount):
                        for _ in range(max_tries):
                            try:
                                ship = Ship.generate(shape, size)
                                map.add_ship(ship)
                                break
                            except ValueError:
                                continue
                        else:
                            raise ValueError
                for amount in range(cls.config['mines']):
                    for _ in range(max_tries):
                        try:
                            mine = Mine.generate(shape)
                            map.add_mine(mine)
                            break
                        except ValueError:
                            continue
                    else:
                        raise ValueError
            except ValueError:
                map.clc()
                continue
            return map

    def show(self):
        res = [[' '] * self.shape[1] for _ in range(self.shape[0])]

        for obj in self._list_objects:
            for (x, y) in obj.get_area():
                if isinstance(obj, Mine):
                    break
                if 0 <= x < self.shape[0] and 0 <= y < self.shape[1]:
                    res[x][y] = '.'

            for (x, y) in obj.get_body():
                if isinstance(obj, Ship):
                    res[x][y] = 'x'
                elif isinstance(obj, Mine):
                    res[x][y] = 'o'

        for x in range(len(res)):
            for y in range(len(res)):
                if self._misses[x][y]:
                    res[x][y] = '#'
                else:
                    pass

        return res

    def war_mist(self):
        res = [[' '] * self.shape[1] for _ in range(self.shape[0])]

        for x in range(len(self._misses)):
            for y in range(len(self._misses)):
                if self._misses[x][y] and isinstance(self._objects[x][y], Ship):
                    res[x][y] = "$"
                elif self._misses[x][y]:
                    res[x][y] = "#"
                else:
                    pass
        return res