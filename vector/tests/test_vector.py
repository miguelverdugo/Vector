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
vector3 = tuple(vector1)
vector4 = np.array(vector2)



