#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    xs = sorted([a, b, c])

    for x in xs:
        if not (x > 0): raise TriangleError

    is_triangle = (xs[0] + xs[1]) > xs[2]
    if not is_triangle:
        raise TriangleError

    if len(set(xs)) == 3:
        return 'scalene'
    elif len(set(xs)) == 2:
        return 'isosceles'
    else:
        return 'equilateral'

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
