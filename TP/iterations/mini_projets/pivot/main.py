#!/usr/bin/env python
"""
On se propose d'implémenter un algorithme qui partitionne un tableau en 2 autour d'un élément dit pivot.
La partition gauche, contient tous les éléments inférieurs ou égaux au pivot.
La partition droite, contient tous les éléments supérieurs au pivot.
"""

def pivote_dynamiquement(tableau, indice_pivot):
    tableau_inf, tableau_sup = [], []
    pivot = tableau[indice_pivot]
    for i in range(len(tableau)):
        if i == indice_pivot: continue
        elem = tableau[i]
        if elem <= pivot:
            tableau_inf.append(elem)
        else:
            tableau_sup.append(elem)
    return tableau_inf, tableau_sup

def echanger(tableau, indice1, indice2):
    tableau[indice1], tableau[indice2] = tableau[indice2], tableau[indice1]

def pivote_en_place(tableau, indice_pivot):
    # Pivot en indice 0 pour simplifier.
    echanger(tableau, 0, indice_pivot) 
    pivot = tableau[0]
    n = len(tableau)
    fini = False
    for i in range(1, n):
        if tableau[i] > pivot:
            fini = True
            for j in range(i+1, n):
                if tableau[j] <= pivot:
                    fini = False
                    echanger(tableau, i, j)
                    break
            # Pas d'éléments <= pivot
            if fini: return 
    return 

tableau = [5, 0, 87, 11, -1, 666, -23, 1, -570]
print(tableau)
pivote_en_place(tableau, 1)
print(tableau)

