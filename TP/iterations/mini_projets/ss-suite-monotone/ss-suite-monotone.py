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
    """
    ...

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} file', file=output)
    else:
        path = sys.argv[1] 
        file = open(path, 'r')
        numbers = file.read().split(' ')
        for n in numbers:
            print(n, file=output)

if __name__ == "__main__":
     main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                      