# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

vec1 = np.array([2.8, -4.7, 0.4])   # u1, u2, u3
vec2 = np.array([-8.1, 3.0, -10.6]) # v1, v2, v3


def cross(vec1, vec2):
   xproduct = np.roll(vec1,2)*np.roll(vec2,1) - np.roll(vec1,1)*np.roll(vec2,2)
   return xproduct


def dot(vec1, vec2):
   dotproduct = np.sum(vec1*vec2)
   return dotproduct


def length(vec):
   return np.sqrt(np.sum(vec**2))


def angle(vec1, vec2):
   cos = dot(vec1, vec2)/ (length(vec1) * length(vec2))
   a = np.arccos(cos)
   return a
   

def check_ortho(vec1, vec2):
   a = angle(vec1, vec2)
   return np.isclose(a, np.pi/2)


   


cross1 = np.cross(vec1, vec2)
cross2 = cross(vec1, vec2)

print(cross1)
print(cross2)