"""Affiche les balises relatives à l'image SVG.
Aussi génère des couleurs.
"""

from random import randint
import svg
import sys

output = sys.stdout

TRASPARENCY = 0.6

def couleur_aleatoire():
    """Retourne une couleur RGB.  
    """

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return f'rgb({r}, {g}, {b})'

def affiche_triangle(triangle, couleur):
    """Affiche un triangle transparent (format liste de points) avec bes balises SVG.  
    """
    print(svg.genere_balise_debut_groupe(couleur, couleur, 0), file=output)
    print(svg.genere_balise_debut_groupe_transp(TRASPARENCY), file=output)
    print(svg.genere_polygone(triangle), file=output)
    print(svg.genere_balise_fin_groupe(), file=output)
    print(svg.genere_balise_fin_groupe(), file=output)


    


