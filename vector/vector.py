"""
simple package to manage 3D vectors
The purpose of it is purely pedagogical and shouldn't be used in production environment

I want the following operations
TODO::
    v1 = Vector(list1)     -> It should also work with tuples, numpy arrays, etc ducktyping
    v2 = Vector(list2)
    v1 + v2 = Vector   ->  valid operation
    v1 - v2 = Vector   -> valid operation
    3 * v1  = Vector   -> valid operation
    v1 * v2 = Exception   ->  invalid operation
    v1 / v2 = Exception   ->  invalid operation
    v1 + 3  = Exception   ->  invalid operation
    v1.magnitude = float     -> returns the magnitude of the vector
    v1.direction = Vector    -> returns a Vector of magnitude = 1, so v1 = v1.magnitude * v1.direction
    v1.distance(v2) = Vector -> returns the vector between these two points
    v1.dot(v2) = float       -> returns the dot product of two vectors
    v1.cross(v2) = Vector    -> returns the cross product of two vectors
    v1.angle(v2) = float     -> returns the angle between two vectors
"""

import math
import numbers


class Vector(object):
    """
    class to work with vectors without help of numpy
    vector1 = Vector(list) = Vector(tuple)

    """


    def __init__(self, vector):
        if len(vector) != 3:
            raise ValueError("not a 3D vector")
        self.source = vector
        self.magnitude = sum([x**2 for x in vector])**0.5
        self.direction = Vector([x/self.magnitude for x in vector])

    def distance(self, vector):
        dist = sum([ (x - y)**2 for x, y in zip(self.source, vector)])**2

        return dist

    def angle(self, vector):
        vector = Vector(vector)
        cos = self.dot(vector) / (self.magnitude * vector.magnitude)

        return math.acos(cos)

    def dot(self, vector):
        result =sum([ x*y for x, y in zip(self.source, vector)])

        return result


    def cross(self, vector):

        a1, a2, a3 = self.source
        b1, b2, b3 = vector
        result = [a2*b3 - a3*b2,
                  a1*b3 - a3*b1,
                  a1*b2 - a2*b1]

        return Vector(result)

    def __add__(self, other):
        if not isinstance(other, (self.__class__, list, tuple):
            raise ValueError(
                'Can only operate on {0}.'.format(self.__class__.__name__))

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

