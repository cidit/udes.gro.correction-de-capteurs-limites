"""
GRO120: Module statistiques - statistiques liées au résultat du filtrage des
données lidar. Les fonctions min, max et moyenne sont également utilisée dans le
module de filtrage.

Auteurs: Marie-Eve Le Ber (lebm2924) et Félix St-Gelais (stgf5468)
Date: 06/10/2026
"""

def nombres_valides(sample_filtre):
    """
    DESC: Filtre une liste de nombres pour conserver uniquement les valeurs
    valides (>=0).
          
    RETOUR: Liste de nombres valides
    """
    nb_valides = []
    # Vérifie si les nombres sont >= 0 et les ajoute à la liste de nombres valides
    for valeur in sample_filtre:
        if valeur >= 0:
            nb_valides.append(valeur)

    return nb_valides


def min(nombres):
    """
    DESC: Détermine la valeur minimale d'une liste de nombres
          
    RETOUR: Valeur minimale
    """
    # Compare chaque nombre au nombre le plus petit déjà traité. La première 
    # comparaison de la boucle se fait avec le premier nombre de la liste.
    min = nombres[0]
    for nombre in nombres:
        if nombre < min:
            min = nombre

    return min

def max(nombres):
    """
    DESC: Détermine la valeur maximale d'une liste de nombres
          
    RETOUR: Valeur maximale
    """
    # Compare chaque nombre au nombre le plus grand déjà traité. La première 
    # comparaison de la boucle se fait avec le premier nombre de la liste.
    max = nombres[0]
    for nombre in nombres:
        if nombre > max:
            max = nombre
            
    return max


def moyenne(nombres: list[float | None]):
    """
    DESC: Calcul la moyenne d'une liste de nombres. Celle liste peut contenir
    des nombres manquants (None).
          
    RETOUR: Valeur moyenne
    """
    somme = 0
    len_nombres = 0
    # Ajoute les nombres qui ne sont pas None à la somme. Le compteur len_nombres
    # est utilisé pour compter le nombre de nombres ajoutés à la sommme.
    for nombre in nombres:
        if nombre:
            somme += nombre
            len_nombres += 1

    # Moyenne calculée selon la somme des valeurs divisée par le nombre de valeurs
    moyenne = somme/len_nombres

    return moyenne


def mediane(nombres: list[float]):
    """
    DESC: Calcul la médiane d'une liste de nombres.
          
    RETOUR: Valeur médiane
    """
    # Ordonner la liste de nombres en ordre croissant
    nombres_croissants = sorted(nombres)

    # Calcul de la médiane si la liste contient un nombre pair de valeurs
    # Une moyenne des deux nombres centraux est effectuée
    if len(nombres_croissants)%2 == 0:
        index_med1 = int(len(nombres_croissants)/2 - 1)
        index_med2 = int(len(nombres_croissants)/2)
        med = moyenne([nombres_croissants[index_med1], nombres_croissants[index_med2]])

    # Calcul de la médiane si la liste contient un nombre impair de valeurs
    # La médiane correspond à la valeur centrale
    else:
        index_med = len(nombres_croissants)//2
        med = nombres_croissants[index_med]

    return med