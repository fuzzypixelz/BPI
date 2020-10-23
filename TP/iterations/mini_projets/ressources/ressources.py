#!/usr/bin/env python3
"""Manipulations complexes de tableaux : listes d'intervalles"""

from collections import namedtuple

# Un ensemble de ressource est représenté par un intervalle et le nombre total
# de ressources qu'il peut contenir
EnsembleRessources = namedtuple("EnsembleRessources",
                                "intervalles, nb_ressources")

def cree_ensemble_ressource(nb_ressources):
    """Créé un ensemble de ressources de taille nb_ressources.

    L'ensemble est représenté par un namedtuple EnsembleRessources.

    L'ensemble créé contient toutes les ressources avec un identifiant id
    tel que 0 <= id < nb_ressources.
    """
    return EnsembleRessources([[0, nb_ressources]], nb_ressources) 

def contient(ensemble_ressources, identifiant):
    """ Test d'appartenance d'une ressource à un ensemble.

    Renvoie True si la ressource identifiée par l'identifiant donné
    est contenu dans ensemble_ressources et False sinon.
    """
    for intervalle in ensemble_ressources.intervalles:
        if identifiant >= intervalle[0] and identifiant < intervalle[1]:
            return True
    return False

def get_chaine(ensemble_ressources):
    """Renvoie une chaîne de caractère représentant l'ensemble donné".

    Par exemple, '|x..xxxxx..|' indique qu'il y a 10 ressources,
    et que les ressources 0, 3, 4, 5, 6 et 7 sont contenues dans l'ensemble.
    """
    chaine = ''
    for identifiant in range(ensemble_ressources.nb_ressources):
        chaine += 'x' if contient(ensemble_ressources, identifiant) else '.'
    chaine = f'|{chaine}|'
    return chaine

def ajoute(ensemble_ressources, ensemble_ressources_a_ajouter):
    """Ajoute des ressources précédemment enlevées dans un ensemble.

    Ajoute toutes les ressources de ensemble_ressources_a_ajouter dans
    l'ensemble ensemble_ressources.
    """
    ressources = ensemble_ressources.intervalles
    intervalles_disjoints = []
    for intervalle in ressources:
        for nouvel_intervalle in ensemble_ressources_a_ajouter.intervalles:
            print(intervalle, nouvel_intervalle)
            if intervalle[1] <= nouvel_intervalle[0] or nouvel_intervalle[1] <= intervalle[0]:
                intervalles_disjoints.append(nouvel_intervalle)    
            else:
                intervalle = [
                        min(nouvel_intervalle[0], intervalle[0]),
                        max(nouvel_intervalle[1], intervalle[1])
                    ]
            
    for intervalle in intervalles_disjoints:
        ressources.append(intervalle)
    ressources.sort()
        
def enleve(ensemble_ressources, nb_ressources):
    """Enleve nb_ressources de l'ensemble donnée.

    Les ressources enlevées sont les nb_ressources *premières ressources* de
    l'ensemble donné.

    Cette fonction *doit renvoyer* un nouvel ensemble de ressources de même
    taille que l'ensemble donné contenant uniquement les ressources qui ont
    été enlevées.
    """
    from copy import deepcopy
    ensemble_ressources_enlevees = deepcopy(ensemble_ressources)
    indice = 0
    nb_enleve = 0
    ressources = ensemble_ressources.intervalles
    ressources_enlevees = ensemble_ressources_enlevees.intervalles
    while nb_enleve < nb_ressources: 
        if ressources[indice][0] == ressources[indice][-1] and indice < len(ressources)-1:
            indice += 1 # Exhausted interval
        print(ressources, indice)
        ressources[indice][0] += 1
        nb_enleve += 1
    ressources_enlevees = ressources_enlevees[0:indice+1]
    ressources_enlevees[indice][1] = ressources[indice][0]
    return ensemble_ressources_enlevees

def test():
    """On teste en gruyerisant un ensemble de ressources"""
    ressources_disponibles = cree_ensemble_ressource(10)
    print("Disponibles après création d'un ensemble à 10 éléments     :",
          get_chaine(ressources_disponibles))
    ressources_reservees = [enleve(ressources_disponibles, c)
                            for c in (2, 2, 3, 2, 1)]
    print(ressources_reservees)
    print("Disponibles après 5 appels à enleve pour un total de 10    :",
          get_chaine(ressources_disponibles))
    ajoute(ressources_disponibles, ressources_reservees[1])
    print("Disponibles après appel à ajout avec ressources 2 et 3     :",
          get_chaine(ressources_disponibles))
    ajoute(ressources_disponibles, ressources_reservees[3])
    print("Disponibles après appel à ajout avec ressources 7 et 8     :",
          get_chaine(ressources_disponibles))
    print("Reservees renvoyées par appel à enleve 3 sur disponibles   :",
          get_chaine(enleve(ressources_disponibles, 3)))
    print("Disponibles après le même appel à enleve 3                 :",
          get_chaine(ressources_disponibles))
    print("Les intervalles de disponibles avec uniquement ressource 8 :",
          ressources_disponibles.intervalles)

if __name__ == "__main__":
    test()
