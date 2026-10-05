"""
GRO120: Module filtrage - implémentation des filtres à appliquer sur les données lidar

Auteurs: ...
Date: jj/mm/aaaa
"""


#===========================================
def filtre_min_max(points, distance_min=0.5, distance_max=15.0):
    """
    DESC: Filtre les points en éliminant ceux qui sont hors des bornes min/max.
          Les valeurs inférieures à la borne min sont remplacées par -1.
          Les valeurs supérieures à la borne max sont remplacées par max.

    RETOUR: Tableau de données filtrées
    """


    UNKNOWN = -1
    def determine(p):
        if distance_min <= p <= distance_max:
            return p
        elif p < distance_min:
            return UNKNOWN
        elif p > distance_max:
            return distance_max
    return [determine(p) for p in points]


#===========================================
# Autres fonctions à compléter...
#===========================================

def filtre_moyenne():
    pass

def filtre_mediane():
    pass
