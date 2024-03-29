"""
Test driving development for class vector
First write the tests for the class, then write the code that make these tests pass

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


from ..vector import Vector
import pytest
import numpy as np

vector1 = [10.5, 2.3, -3.3]
vector2 = [-15.1, 4.7, 8.5]


class TestVector:

    def test_ducktyping(self):
        v1 = Vector(vector1)
        v2 = Vector(tuple(vector1))
        v3 = Vector(np.array(vector1))
        assert v1 == v2
        assert v1 == v3

    def test_dot_product_input(self):
        v1 = Vector(vector1)
        v2 = Vector(vector2)
        result1 = v1.dot(v2)
        result2 = v1.dot(vector2)
        assert np.isclose(result1, result2)

    def test_dot_product_result(self):
        v1 = Vector(vector1)
        v2 = Vector(vector2)
        dot_result = v1.dot(v2)
        assert np.isclose(dot_result, np.dot(vector1, vector2))

    def test_cross_product(self):
        v1 = Vector(vector1)
        v2 = Vector(vector2)
        assert isinstance(v1.cross(v2), Vector)



