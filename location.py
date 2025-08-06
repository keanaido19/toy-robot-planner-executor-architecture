class Location:
    x: int
    y: int

    def __init__(self):
        self.x = 0
        self.y = 0

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_x(self, x: int) -> None:
        self.x = x

    def set_y(self, y: int) -> None:
        self.y = y
