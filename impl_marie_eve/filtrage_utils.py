"""
GRO120: Fonctions utilitaires pour le module filtrage

Auteurs: Marie-Eve Le Ber (lebm2924) et Félix St-Gelais (stgf5468)
Date: 06/10/2026
"""

import statistiques as stats


def ordonner(liste_originelle: list[float]):
    """
    DESC: Ordonne une liste en ordre croissant.

    RETOUR: Liste de floats en ordre croissants
    """
    # L'algorithme "bubble sort" est un algorithme existant et établit. Son
    # implémentation est répertoriée sur sa page Wikipedia: https://en.wikipedia.org/wiki/Bubble_sort

    # On copie le tableau pour éviter de le muter.
    nombres= liste_originelle[:]
    # L'implémentation suit le premier pseudocode de la page Wikipedia ci-haut.

    changement = True
    while changement:
        changement = False
        # Chaque nombre, en commençant par le deuxième, est comparé au nombre 
        # précédant. Si le nombre précédent est plus élevé, les deux nombres sont 
        # inversés.
        for i in range(1, len(nombres)):
            if nombres[i-1] > nombres[i]:
                tmp = nombres[i]
                nombres[i] = nombres[i-1]
                nombres[i-1] = tmp
                changement = True
        # Tant qu'il y aura des changements, la boucle se répète. Quand
        # il n'y en a plus, le tri de la liste est complété.
    return nombres


def mediane_3nb(nombres: list[float]):
    """
    DESC: Calcul la médiane de 3 nombres

    RETOUR: Valeur médiane
    """
    # Ordonne les trios nombres et sélectionne celui du centre commme médiane
    nombres_croissants = ordonner(nombres)
    mediane = nombres_croissants[1]

    return mediane
