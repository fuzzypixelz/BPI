#!/usr/bin/env python3

"""Listes simplements chainees + quelques operations"""

class Cellule:
    """Une cellule d'une liste."""
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

class ListeSimplementChainee:
    """Une liste simplement chainee."""
    # How to force the user to set all args, or none at all?
    def __init__(self, tete=None, queue=None, taille=0):
        self.tete = tete
        self.queue = queue
        self.taille = taille

def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tete"""
    ancienne_tete = liste_chainee.tete
    nouvelle_tete = Cellule(valeur, ancienne_tete)
    liste_chainee.tete = nouvelle_tete
    liste_chainee.taille += 1

def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une cellule en queue."""
    nouvelle_queue = Cellule(valeur, None)
    liste_chainee.queue.suivant = nouvelle_queue
    liste_chainee.taille += 1

def recupere_cellules(liste_chainee):
    """Renvoie un vecteur contenant toutes les cellules de la liste_chainee"""
    cellules = []
    cellule = liste_chainee.tete
    while cellule != None:
        cellules.append(cellule.valeur) 
        cellule = cellule.suivant 
    return cellules

def recherche(liste_chainee, valeur):
    """Recherche uen valeur dans la liste_chainee donnée.

    Renvoie la premiere cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    cellule = liste_chainee.tete
    while cellule != None:
        if cellule.valeur == valeur: return cellule
        cellule = cellule.suivant
    return None

def supprime(liste_chainee, valeur):
    """Enleve la premiere cellule contenant la valeur donnée."""
    cellule_avant = liste_chainee.tete
    while cellule_avant.suivant != None:
        if cellule_avant.suivant.valeur == valeur: break
        cellule_avant = cellule_avant.suivant
    if cellule_avant is liste_chainee.tete:
        liste_chainee.tete = liste_chainee.tete.suivant
    elif cellule_avant.suivant is liste_chainee.queue:
        cellule_avant.suivant = None
        liste_chainee.queue = cellule_avant
    else:
        cellule_suivante = cellule_avant.suivant.suivant
        cellule_avant.suivant = cellule_suivante

def test_listes():
    """On teste les operations de base, dans differentes configurations."""
    liste_chainee = ListeSimplementChainee()
    ajoute_en_tete(liste_chainee, 3)
    ajoute_en_tete(liste_chainee, 5)
    ajoute_en_tete(liste_chainee, 2)
    ajoute_en_tete(liste_chainee, 4)
    print("liste_chainee : ", recupere_cellules(liste_chainee))
    print("recherche : ", recherche(liste_chainee, 3).valeur)
    supprime(liste_chainee, 5)
    print("apres suppression de 5 : ", recupere_cellules(liste_chainee))
    supprime(liste_chainee, 4)
    print("apres suppression de 4 : ", recupere_cellules(liste_chainee))

if __name__ == "__main__":
    test_listes()
