class Object:
    """
    Base abcract class for all objects on the map.
    """

    def __init__(self, position) -> None:
        self.position = position

    def get_body(self):
        pass

    def get_area(self):
        pass

    def get_hit(self):
        pass