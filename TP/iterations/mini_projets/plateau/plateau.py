#!/usr/bin/env python
"""
Construit une image SVG à partir d'une largeur et une hauteur donnés.
"""
import sys
import svg
from math import copysign

output = sys.stdout

LARGEUR = 120
HAUTEUR = 80
CASE = 40

def output_case(x, y, nombre):
    """  
    Prints la case donnée.
    """
    print(svg.genere_balise_debut_groupe('black', 'white', 1), file=output)
    # Le module svg considère que le début du carré est le point
    # le plus haut à gauche.  
    print(svg.genere_rectangle(svg.Point(x, y-CASE), CASE, CASE), file=output)
    print(svg.genere_texte(svg.Point(x, y), nombre), file=output)
    print(svg.genere_balise_fin_groupe(), file=output)

def avancer_horizontalement(nombre_debut, debut, fin):
    """ 
    Avance dans la direction donnée en déssinant des carrés. 
    debut contient les coordonnées du point le plus bas à gauche du premier carré.
    fin est la coordonnée du point le plus haut à droite dans le premier carré.
    Retourne le nombre suivant.
                                - -      >      - +
                                + -      >      - -
    """
    var_horizontale = fin.x - (debut.x + CASE)

    x = debut.x
    x_max = fin.x
    # Because svg is not symmetric in its drawing, we need to offset the difference.
    if var_horizontale < 0: 
        x -= CASE
        x_max -= CASE
    y = debut.y
    step = copysign(CASE, var_horizontale)
    # On suppose que les points sont bien choisis!
    while x != x_max:
        output_case(x, y, nombre_debut)
        # Next square!
        nombre_debut += 1
        x += step
    return nombre_debut

def avancer_verticalement(nombre_debut, debut, fin):
    """ 
    Avance dans la direction donnée en déssinant des carrés. 
    debut contient les coordonnées du point le plus bas à gauche du premier carré.
    fin est la coordonnée du point le plus haut à droite dans le premier carré.
    Retourne le nombre suivant.
                                + -      >      - -
                                - -      >      - +
    """
    var_verticale = fin.y - (debut.y - CASE)

    y = debut.y
    y_max = fin.y
    # Because svg is not symmetric in its drawing.
    if var_verticale > 0: 
        pass
        y += CASE
        y_max += CASE
    x = debut.x
    step = copysign(CASE, var_verticale)
    # On suppose que les points sont bien choisis!
    while y != y_max:
        output_case(x, y, nombre_debut)
        # Next square!
        nombre_debut += 1
        y += step
    return nombre_debut

def main():
    """
    Fonction main.
    """
    
    nombre = 1

    outer_left = 0
    inner_left = CASE
    outer_right = LARGEUR
    inner_right = LARGEUR-CASE
    top = 0
    bottom = HAUTEUR

    sens_positif = True
    
    print(svg.genere_balise_debut_image(LARGEUR, HAUTEUR), file=output)
    
    y = bottom
    while y >= top:
        if sens_positif:
            nombre = avancer_horizontalement(nombre, svg.Point(outer_left, y), svg.Point(inner_right, y-CASE))
            nombre = avancer_verticalement(nombre, svg.Point(inner_right, y), svg.Point(outer_right, y-3*CASE))
        else:
            nombre = avancer_horizontalement(nombre, svg.Point(inner_right, y), svg.Point(inner_left, y-CASE))
            nombre = avancer_verticalement(nombre, svg.Point(outer_left, y), svg.Point(inner_left, y-3*CASE))
        y -= 2*CASE
        sens_positif = not sens_positif
    
    print(svg.genere_balise_fin_image(), file=output)


if __name__ == "__main__":
    main()