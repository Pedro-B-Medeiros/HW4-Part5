import data
import math


def scale_vector(vector, scalar):
    new_vector = data.Vector(0, 0, 0)
    new_vector.x = vector.x * scalar
    new_vector.y = vector.y * scalar
    new_vector.z = vector.z * scalar
    return new_vector

def dot_vector(vector1, vector2):
    return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z

def length_vector(vector):
    return math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)

def normalize_vector(vector):
    scale = 1 / length_vector(vector)
    normalize_vector = scale_vector(vector, scale)
    return normalize_vector


def difference_point(point1, point2):
    difference_point = data.Vector(0, 0, 0)
    difference_point.x = point1.x - point2.x
    difference_point.y = point1.y - point2.y
    difference_point.z = point1.z - point2.z
    return difference_point


def difference_vector(vector1, vector2):
    difference_vector = data.Vector(0, 0, 0)
    difference_vector.x = vector1.x - vector2.x
    difference_vector.y = vector1.y - vector2.y
    difference_vector.z = vector1.z - vector2.z
    return difference_vector

def translate_point(point, vector):
    translate_point = data.Point(0, 0, 0)
    translate_point.x = point.x + vector.x
    translate_point.y = point.y + vector.y
    translate_point.z = point.z + vector.z
    return translate_point

def vector_from_to(from_point, to_point):
    vector_from_to = data.Vector(0, 0, 0)
    vector_from_to.x = to_point.x - from_point.x
    vector_from_to.y = to_point.y - from_point.y
    vector_from_to.z = to_point.z - from_point.z
    return vector_from_to
