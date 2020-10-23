#!/usr/bin/env python
""" Make PGM image. """
import sys
from random import randint
from math import sqrt
import time
 
# output = sys.stdout
output = open('output.pgm', 'w')

def make_disque(largeur, hauteur):
    """ Retourne un rayon (int) et un centre (int, int). """
    rayon = min(randint(1, largeur//2), randint(1, hauteur//2))
    centre = (randint(rayon, largeur-rayon), randint(rayon, hauteur-rayon))
    return rayon, centre

def is_indisque(point, disque):
    """ Retourne True si le point appartient au cercle. """
    rayon = disque[0]
    centre = disque[1]
    return sqrt((point[0]-centre[0])**2 + (point[1]-centre[1])**2) <= rayon

# Paramètres
MAX = 255 # blanc
SIZE = 5000
largeur = SIZE
hauteur = SIZE

# Dimensions de l'image
# largeur = int(input('Entrez la largeur: '))
# hauteur = int(input('Entrez la hauteur: '))

# En-tête
print('P2', file=output)
print(f'{largeur} {hauteur}', file=output)
print(MAX, file=output)

# Choisir les disques
disque_1 = make_disque(largeur, hauteur)
disque_2 = make_disque(largeur, hauteur)

# Dessiner les pixels
for y in range(1, hauteur + 1):
    # Ligne par ligne!
    for x in range(1, largeur + 1):
        point = (x, y)
        if not is_indisque(point, disque_1) and not is_indisque(point, disque_2):
            print(f'{MAX} ', file=output)
        else:
            print(f'{randint(0, MAX)} ', file=output)
    print(file=output)

        





