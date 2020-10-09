#!/usr/bin/env python
"""
Cherche la sous suite monotone la plus longue dans un fichier.
Reçoit le nom du fichier en paramètre.
"""

import sys

output = sys.stdout

def traite_nombre(suite, type_suite, nombre):
    """ 
    Traite le nombre donné vis à vis de la suite donnée.

    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite à changer de sens
    type_suite est soit 'C' pour 'Croissante', soit 'D' pout 'Décroissante'
    """

    if len(suite) == 0: return True, type_suite

    nombre_dernier = suite[len(suite)-1]

    toujours_monotone = nombre >= nombre_dernier if type_suite == 'C' else nombre <= nombre_dernier
    
    type_suite_change = 'D' if type_suite == 'C' else 'C'

    nouveau_type = type_suite if toujours_monotone else type_suite_change

    return toujours_monotone, nouveau_type
        

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} file', file=output)
    else:
        path = sys.argv[1] 
        file = open(path, 'r')
        numbers = file.read().split()
        print(numbers)
        suite_list = []
        indice_fin = 0
        indice_debut = 0
        type_suite = 'C' if numbers[1] >= numbers[0] else 'D'
        while indice_fin < len(numbers)-1:
            indice_fin += 1
            suite = numbers[indice_debut:indice_fin]
            nombre_suivant = numbers[indice_fin]
            toujours_monotone, type_suite_nouveau = traite_nombre(
                suite, 
                type_suite, 
                nombre_suivant
            )
            if type_suite_nouveau != type_suite:
                suite_list.append(suite)
                indice_debut = indice_fin-1
            type_suite = type_suite_nouveau
        # This is a terrible way of doing this.
        suite_list[-1].append(numbers[-1])

        # Test
        print(suite_list)
        print(max([len(suite) for suite in suite_list]))

if __name__ == "__main__":
     main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                      