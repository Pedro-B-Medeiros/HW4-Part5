import utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x, 0.00001) and utility.epsilon_equal(self.y, other.y, 0.00001) and utility.epsilon_equal(self.z, other.z, 0.00001)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x, 0.00001) and utility.epsilon_equal(self.y, other.y, 0.00001) and utility.epsilon_equal(self.z, other.z, 0.00001)


class Ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return (self.pt == other.pt) and utility.epsilon_equal(self.dir, other.dir, 0.00001)


class Sphere:
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        return (self.center == other.center) and utility.epsilon_equal(self.radius, other.radius, 0.00001) and (self.color == other.color) and utility.epsilon_equal(self.finish, other.finish, 0.00001)


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, other):
        return Color(self.r * other.r, self.g * other.g, self.b * other.b)

    def __imul__(self, multiplier):
        return Color(self.r * multiplier, self.g * multiplier, self.b * multiplier)

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __eq__(self, other):
        return utility.epsilon_equal(self.r, other.r, 0.00001) and utility.epsilon_equal(self.g, other.g, 0.00001) and utility.epsilon_equal(self.b, other.b, 0.00001)


class Finish:
    def __init__(self, ambient, diffuse):
        self.ambient = ambient  # percentage of ambient light reflected by the finish
        self.diffuse = diffuse  # percentage of diffuse light reflected by finish

    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient, 0.00001) and utility.epsilon_equal(self.diffuse, other.diffuse, 0.00001)

class Light:
    def __init__(self, pt: Point, color: Color):
        self.color = color
        self.pt = pt

    def __eq__(self, other):
        return self.pt == other.pt and self.color == other.color
