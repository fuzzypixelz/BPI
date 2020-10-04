"""Génère et manipule des triangles.
Notamment la rotation. 
"""

from random import randint
from collections import namedtuple
from math import cos, sin

Point = namedtuple('Point', ['x', 'y'])

def genere_point(intervalle_x, intervalle_y):
    """Génère un point dont les coordonnées respectent les intervalles donnés,
    dans chaque direction.  
    """

    return Point(
        randint(intervalle_x[0], intervalle_x[1]),
        randint(intervalle_y[0], intervalle_y[1])
    )

def triangle_aleatoire(intervalle_x, intervalle_y):
    """Retourne une liste de Points du triangle.
    Le triangle doit être contenu dans l'espace definit par un couple de deux intervalles,
    les intervalles sont aussi des couples.
    """

    triangle = []
    for _ in range(3):
        triangle.append(genere_point(intervalle_x, intervalle_y))
    return triangle

def tourne_point(point, centre, angle):
    """Tourne un point de l'angle donné autour du centre.
    Retourne le point resultant.  
    """

    coord_x = centre.x + (point.x - centre.x) * cos(angle) - (point.y - centre.y) * sin(angle)
    coord_y = centre.y + (point.x - centre.x) * sin(angle) + (point.y - centre.y) * cos(angle)
    return Point(coord_x, coord_y)

def tourne_triangle_autour(triangle, centre, angle):
    """Tourne les trois points d'un triangle de l'angle autour du centre.
    Retourne le triangle tourné.
    """
    
    triangle_tourne = []
    for point in triangle:
        triangle_tourne.append(tourne_point(point, centre, angle))

    return triangle_tourne




