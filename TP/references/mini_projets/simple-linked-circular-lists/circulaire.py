#!/usr/bin/env python3

"""Listes simplement chaînées, triées, circulaires et avec sentinelle."""

class Cellule:
    """ Une cellule possède une valeur et un suivant
    """
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class ListeSimplementChaineeTriee:
    """Listes simplement chaînées, triées, circulaires et avec sentinelle."""
    def __init__(self, sentinelle, nombres=None):
        """Construit la liste avec le range de nombres donné.

        sentinelle precise la valeur de la cellule sentinelle.
        pre-condition: le range de nombres donné est trié.
        """
        cellule = Cellule(nombres[0])
        for valeur in nombres:
            if valeur == sentinelle:
                self.tete = cellule
            _cellule = Cellule(valeur)
            cellule.suivant = _cellule
            cellule = _cellule

    def __str__(self):
        """Renvoie val1 --> val2 --> val3 ..."""
        representation = ""
        for val in nombres[:-1]:
            representation += f"{val} --> "
        representation += str(val)
        return representation

def recupere_cellules(liste_chainee, inclure_sentinelle=False):
    """Renvoie un vecteur contenant toutes les cellules de la liste_chainee.

    inclure_sentinelle est un booleen permettant de preciser
    si la sentinelle est incluse ou non dans les cellules renvoyées.
    """
    sentinelle = liste_chainee.tete
    vecteur = [sentinelle.valeur] if inclure_sentinelle else []
    cellule = sentinelle.suivant
    while cellule.valeur != sentinelle.valeur:
        vecteur.append(cellule.valeur)
        cellule = cellule.suivant
    return vecteur

def decoupe(liste_chainee):
    """Coupe la liste en 2 (une cellule sur 2).

    Par exemple (1,4,2,3,5) produit (1,2,5) et (4,3).
    Renvoie les deux nouvelles listes.
    Aucune nouvelle cellule n'est creee (hormis les sentinelles
    des deux nouvelles listes),
    En sortie la liste liste_chainee est vide.
    """
    sentinelle = liste_chainee.tete.valeur
    liste_chainee_1 = ListeSimplementChaineeTriee(sentinelle)
    liste_chainee_1 = ListeSimplementCahineeTriee(sentinelle)
    cellule_1 = liste_chainee_1.tete
    cellule_2 = liste_chainee_2.tete
    tour = True
    for valeur in recupere_cellules(liste_chainee):
        if tour:
            cellule_1.suivant = Cellule(valeur)
            cellule_1 = cellule_1.suivant
        else:
            cellule_2.suivant = Cellule(valeur)
            cellule_2 = cellule_2.suivant
        tour = not tour

def ajoute(liste_chainee, valeur):
    """Ajoute la valeur donnee a la bonne place dans la liste.

    pre-condition : valeur n'est pas la valeur de la sentinelle.
    """
    # TODO
    ...

def supprime(liste_chainee, valeur):
    """Supprime la premiere cellule contenant la valeur donnée.

    pre-condition : valeur n'est pas la valeur de la sentinelle.
    """
    # TODO
    ...

def test():
    """Tests simples des différentes fonctions (à compléter)"""
    entiers = ListeSimplementChaineeTriee(float("inf"), range(8))
    print(entiers)
    resultat_decoupe = decoupe(entiers)
    pairs, impairs = resultat_decoupe
    print("pairs =", pairs, " impairs =", impairs)
    print("entiers après découpe =", entiers)
    supprime(pairs, 4)
    supprime(pairs, 0)
    supprime(pairs, 2)
    supprime(pairs, 6)
    print("pairs après supression de tous les éléments = ", pairs)
    ajoute(impairs, 6)
    ajoute(impairs, 0)
    print("impairs après ajout de 6 et 0 = ", impairs)

if __name__ == "__main__":
    test()
