#!/usr/bin/env python

from collections import namedtuple

Point = namedtuple("Point", "x, y")

Triangle = namedtuple("Triangle", "p1, p2, p3")

def affiche_triangle(triangle):
    """ Affiche les trois points de triangle sur la sortie standard """
    print(
        f"p1 = ({triangle.p1.x}, {triangle.p1.y}), " + 
        f"p2 = ({triangle.p2.x}, {triangle.p2.y}), " +
        f"p3 = ({triangle.p3.x}, {triangle.p3.y})")

# Named tuples are not mutable either
point1 = Point(1, 2)
point2 = Point(4, 7)
point3 = Point(8, 5)

triangle = Triangle(point1, point2, point3)

affiche_triangle(triangle)