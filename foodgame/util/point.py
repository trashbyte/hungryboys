from math import floor

## An immutable structure representing the integer coordinates of a grid space.
class Point(tuple):
    __slots__ = []


    def __new__(cls, x, y):
        return tuple.__new__(cls, (floor(x), floor(y)))


    ## The x coordinate.
    @property
    def x(self):
        return tuple.__getitem__(self, 0)


    ## The y coordinate.
    @property
    def y(self):
        return tuple.__getitem__(self, 1)


    def __getitem__(self, item):
        raise TypeError


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


    ## Multiply a Point by another Point, or by a scalar.
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)