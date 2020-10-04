#!/usr/bin/env python

import svg
import sys

PIPLINES = True

hauteur = 340
largeur = 360
couleur_ligne = 'white'
couleur_remplissage = 'red'
epaisseur_ligne = '4'
rayon = 15
points = [
    svg.Point(100, 20),
    svg.Point(260, 20),
    svg.Point(20, 120),
    svg.Point(180, 120),
    svg.Point(340, 120),
    svg.Point(100, 220),
    svg.Point(260, 220),
    svg.Point(180, 320)
]

if PIPLINES:
    output = sys.stdout
else:
    output = open('heart.svg', 'w')

# Get the opening svg tag
print(svg.genere_balise_debut_image(largeur, hauteur), file=output)

# Get the opening group tag
print(svg.genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne), file=output)

# Get all the points
for point in points:
    print(svg.genere_cercle(point, rayon), file=output)

# Get the closing group tag
print(svg.genere_balise_fin_groupe(), file=output)

# Get the closing svg tag
print(svg.genere_balise_fin_image(), file=output)

# Close the file, if any
if not PIPLINES: output.close()



