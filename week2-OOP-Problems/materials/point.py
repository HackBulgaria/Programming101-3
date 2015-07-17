# Immutable


class MutablePoint2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "2DPoint::({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class ImmutablePoint2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "2DPoint::({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def move(self, dx, dy):
        return ImmutablePoint2D(self.x + dx, self.y + dy)
