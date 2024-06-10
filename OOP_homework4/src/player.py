from src.ship import Ship
from src.mine import Mine
from src.map import Map

class Player:
    """
    Class represents a player in the game.
    """

    def __init__(self, map: Map):
        self.map = map

    def fill_map(self):
        self.palce_ships()
        self.place_mines()

    def do_attack(self,other):
        while True:
            cordinats = [int(i) for i in input("Choose cordinats: ").split()]
            x = cordinats[0]
            y = cordinats[1]

            if x < 0 or x >= len(other.map._misses) or y < 0 or y >= len(other.map._misses[0]):
                raise ValueError("Invalid coordinates. Please enter coordinates within the map.")

            if not other.map._misses[x][y]:
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
                break
            else:
                print("Select other coordinats!")

        other.map.clean_list()
        self.map.clean_list()

    def is_lose(self):
        if not self.map.ships_list:
            return True
        
        return False

    def place_ships(self):
        for size, amount in self.map.config['ships']:
            for _ in range(amount):
                cordinats = [int(i) for i in input(f"Choose cordinats for ship with size {size}: ").split()]
                orient = int("Choose orientation(0 or 1): ")

                if orient not in [0, 1]:
                    raise ValueError("Incorrect orientation!")
                
                x = cordinats[0]
                y = cordinats[1]

                ship = Ship((x, y), orient, size)
                self.map.add_ship(ship)

    def place_mines(self):
        for _ in range(len(self.map.config['mines'])):
            cordinats = [int(i) for i in input(f"Choоse coordinats for mine: ").split()]
            x = cordinats[0]
            y = cordinats[1]
            mine = Mine((x, y))
            self.map.add_mine(mine)
