"""
GRO120: Fonctions utilitaires pour le module filtrage

Auteurs: Marie-Eve Le Ber (lebm2924) et Félix St-Gelais (stgf5468)
Date: 06/10/2026
"""

import statistiques as stats


def _ordonner_3nb(nombres: list[float]):
    """
    DESC: Ordonne une liste de 3 nombres en ordre croissant.
          
    RETOUR: Liste de 3 floats en ordre croissants
    """
    nombres_croissants = []

    # Ordonne les nombres et les ajoute ou insère dans nombres_croissants
    for nombre in nombres:
        # Le nombre le plus petit est inséré au début de la liste
        if nombre == stats.min(nombres):
            nombres_croissants.insert(0, nombre)
        # Le nombre le plus grande est inséré à la fin de la liste
        elif nombre == stats.max(nombres):
            nombres_croissants.append(nombre)
        else:
            # S'il y a déjà deux nombre dans la liste, le nombre du centre est
            # inséré à la deuxième position.
            if len(nombres_croissants) == 2:
                nombres_croissants.insert(1, nombre)
            # S'il y a déjà un seul nombre dans la liste, le nombre du centre
            # est inséré en ordre croissant
            elif len(nombres_croissants) == 1:
                if nombre < nombres_croissants[0]:
                    nombres_croissants.insert(0, nombre)
                elif nombre > nombres_croissants[0]:
                    nombres_croissants.append(nombre)
            # Si la liste est vide, le nombre du centre est ajouté à la liste
            else:
                nombres_croissants.append(nombre)

    return nombres_croissants


def mediane_3nb(nombres: list[float]):
    """
    DESC: Calcul la médiane de 3 nombres
          
    RETOUR: Valeur médiane
    """
    # Ordonne les trios nombres et sélectionne celui du centre commme médiane
    nombres_croissants = _ordonner_3nb(nombres)
    mediane = nombres_croissants[1]

    return mediane