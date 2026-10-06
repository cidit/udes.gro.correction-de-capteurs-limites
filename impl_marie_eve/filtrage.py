"""
GRO120: Module filtrage - implémentation des filtres à appliquer sur les données
lidar 

Auteurs: Marie-Eve Le Ber (lebm2924) et Félix St-Gelais (stgf5468)
Date: 06/10/2026
""" 

import filtrage_utils as utils
import statistiques as stats


def filtre_min_max(points:list[float], distance_min=0.5, distance_max=15.0) -> list[float]:
    """
    DESC: Filtre les points en éliminant ceux qui sont hors des bornes min/max.
          Les valeurs inférieures à la borne min sont remplacées par -1.
          Les valeurs supérieures à la borne max sont remplacées par max.
          
    RETOUR: Tableau de données filtrées
    """
    # Nouvelle liste dans laquelle les points filtrés seront ajoutés
    points_filtres = []

    for point in points:
        # Si la valeur du point est inférieur au minimum, le point est invalide
        # et prendra la valeur de -1
        if (point < distance_min):
            points_filtres.append(-1)
        # Si la valeur du point est supérieure au maximum, elle est plafonnée
        elif (point > distance_max):
            points_filtres.append(distance_max)
        else:
            points_filtres.append(point)

    return points_filtres

def filtre_moyenne(points: list[float]):
    """
    DESC: Filtre une liste de points avec une moyenne mobile ayant une fenêtre 
    de 3 valeurs. Pour le premier et dernier point de la liste, seuls 2 valeurs 
    sont utilisées.
          
    RETOUR: Tableau de données filtrées
    """
    # Nouvelle liste dans laquelle les points filtrés seront ajoutés
    points_filtres = []

    # Liste décalée vers la droite ou la gauche pour représenter les points
    # précédants ou suivants. Comme il n'y a pas de point avant le premier
    # point de la liste ou après le dernier, des valeurs nulles sont présentes
    # à ces positions. 
    points_prec = [None] + points[:-1]
    points_suiv = points[1:] + [None]

    # On itère sur les trois listes en même temps. Pour chaque point de la liste,
    # on obtient la valeur du point précédant, du point et du point suivant.
    # La moyenne de ces trois points est calculée et ajoutée à la nouvelle liste.
    for point_prec, point, point_suiv in zip(points_prec, points, points_suiv):
        points_filtres.append(stats.moyenne([point_prec, point, point_suiv]))

    return points_filtres


def filtre_mediane(points: list[float]):
    """
    DESC: Filtre une liste de points avec une médiane mobile ayant une fenêtre 
    de 3 valeurs. Le premier et dernier point de la liste ne sont pas traités.
          
    RETOUR: Tableau de données filtrées
    """
    # Si la liste de points en entrée est vide, retourner une liste vide.
    try:
        points_filtres = [points[0]]
    except IndexError:
        return []

    # Liste décalée vers la droite ou la gauche pour représenter les points
    # précédants ou suivants. Les premier point n'est pas traité et retourné
    # tel quel.
    if len(points) > 2:
        points_prec = points[:-2]
        points_act = points[1:-1]
        points_suiv = points[2:]

        # On itère sur les trois listes en même temps. Pour chaque point, on
        # obtient la valeur du point précédant, du point et du point suivant.
        # La médiane de ces trois points est calculée et ajoutée à la nouvelle liste.
        for point_prec, point_act, point_suiv in zip(points_prec, points_act, points_suiv):
            points_filtres.append(utils.mediane_3nb([point_prec, point_act, point_suiv]))

    # Si la liste contient plus d'un point, ajouter le dernier point qui 
    # n'est pas traité et retourné tel quel.
    if len(points) > 1:
        points_filtres.append(points[-1])

    return points_filtres