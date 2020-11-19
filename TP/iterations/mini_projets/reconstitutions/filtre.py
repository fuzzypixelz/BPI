#!/usr/bin/env python

import svg
import sys

# SVG file
svg_file = sys.stdout

# Points
points_file = sys.stdin

# Params
largeur = 640
longeur = 480
radius = 6
stroke = 'white'
fill = 'black'
stroke_width = 2


# SVG opening tag
print(svg.genere_balise_debut_image(largeur, longeur), file=svg_file)

# Group opening tag
print(svg.genere_balise_debut_groupe(stroke, fill, stroke_width), file=svg_file)

# Circle tags
points = points_file.readlines()
points_length = len(points)
index = 0
current_coord = points[index]
while index < points_length:
    next_coord = points[index + 1]

    # Make and print the cricle
    circle = svg.Point(current_coord, next_coord)
    print(svg.genere_cercle(circle, radius))

    # Reset for next point, provided we're not done
    if index == points_length - 2: break
    index += 2
    current_coord = points[index]

# Group closing tag
print(svg.genere_balise_fin_groupe(), file=svg_file)

# SVG closing tag
print(svg.genere_balise_fin_image())



    




