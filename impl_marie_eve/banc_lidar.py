"""
GRO120: Banc de test lidar
        Permet de tester le filtrage d'échantillons de données lidar.

        Les étapes sont :
           1. Lire les données d'un fichier texte (entrée)
           2. Filtrer les données lues (selon le filtre choisi)
           3. Écrire les données filtrées dans un fichier texte (sortie)
           4. Afficher les valeurs statistiques des données filtrées valides (>=0)

Auteurs: Marie-Eve Le Ber (lebm2924) et Félix St-Gelais (stgf5468)
Date: 06/10/2026
"""

import sys

import filtrage
import statistiques as stats


def lecture(path):
    """
    DESC: Ouvre, lit puis ferme un fichier texte contenant un nombre par ligne.

    RETOUR: Liste de nombres flottants
    """
    fichier = open(path, "r")
    points = []
    # Ajoute à la liste points le nombre inscrit à chacune des lignes du fichier.
    for ligne in fichier:
        points.append(float(ligne.strip()))
    fichier.close()
    return points


def ecriture(nom_fichier, liste):
    """
    DESC: Écrit une liste de nombres dans le fichier sous le format d'un nombre 
    par ligne. Si le fichier contenait déjà des données, celles-ci seront écrasées.

    RETOUR: Aucun
    """
    fichier = open(nom_fichier, "w")
    # Écrit chaque nombre de la liste sur une nouvelle ligne dans le fichier.
    for valeur in liste:
        fichier.write(str(valeur) + "\n")
    fichier.close()


def input_fichier_intrant():
    """
    DESC: Demande à l'utilisateur d'entrer un chemin d'accès vers un fichier
    texte contenant des données lidar. Ce fichier texte doit contenir un nombre
    entier ou flottant par ligne.

    RETOUR: String contenant le chemin d'accès vers un fichier de données lidar
    """
    while True:
        fichier_intrant = input(
            "> Entrez un fichier texte contenant des données lidar : "
        ).strip()

        # Si aucun chemin d'accès n'a été entré, redemande à l'utilisateur
        # d'entrer un chemin d'accès
        if fichier_intrant == "":
            print("Aucun fichier en entrée. Veuillez fournir un fichier texte.")
            continue

        # L'utilisateur peut quitter le programme en entrant q
        elif fichier_intrant == str.lower("q"):
            sys.exit()

        return fichier_intrant


def input_fichier_filtre():
    """
    DESC: Demande à l'utilisateur d'entrer le nom du chemin d'accès du fichier 
    texte en sortie. Les données filtrées seront écrites dans ce fichier.

    RETOUR: String contenant le chemin d'accès vers un fichier de données lidar
    """
    while True:
        fichier_filtre = input(
            "> Entrez le nom désiré du fichier filtré en sortie : "
        ).strip()

        # Si aucun nom de fichier n'a été entré, redemande à l'utilisateur
        # d'entrer un nom de fichier
        if fichier_filtre == "":
            print("Aucun nom indiqué. Veuillez fournir un nom pour le fichier en sortie.")
            continue

        # L'utilisateur peut quitter le programme en entrant q
        elif fichier_filtre == str.lower("q"):
            sys.exit()

        return fichier_filtre


def input_filtre():
    """
    DESC: Demande à l'utilisateur d'entrer le numéro du filtre choisi. Les options
    sont 1, 2 ou 3.

    Les filtres correspondants sont les suivants:
    1 - Limitation par plage minimum-maximum
    2 - Filtrage par moyenne mobile
    3 - Filtrage par médiane mobile

    RETOUR: String contenant le numéro 1, 2 ou 3
    """
    while True:
        filtre = input(
            "> Indiquez le numéro du filtre à appliquer: "
        ).strip()

        # Si aucun numéro de filtre n'a été entré, redemande à l'utilisateur
        # d'entrer un nunéro de filtre
        if filtre == "":
            print("Aucun filtre indiqué. Veuillez fournir un filtre à appliquer.")
            continue

        # Si une valeur autre que 1, 2 ou 3 a été entrée, redemande à l'utilisateur
        # d'entrer un nunéro de filtre
        if filtre not in ["1", "2", "3"]:
            print("Filtre invalide. Veuillez fournir un nombre entier entre 1 et 3.")
            continue

        # L'utilisateur peut quitter le programme en entrant q
        elif filtre == str.lower("q"):
            sys.exit()


        return filtre


def input_min():
    """
    DESC: Offre à l'utilisateur l'option d'entrer un minimum pour le filtre
    de limitation par plage minimum-maximum. Si aucune valeur n'est entrée,
    la valeur par défaut de 0,5 est sélectionnée.

    RETOUR: Float correspondant au minimum
    """
    while True:
        min = input("> Valeur minimum (facultatif): ").strip()

        # Comme enter une valeur minimum est facultative, une valeur par défaut
        # est utilisée si aucune valeur n'est entrée par l'utilisateur
        if min == "":
            min = 0.5

        # L'utilisateur peut quitter le programme en entrant q
        elif min == str.lower("q"):
            sys.exit()

        # Si la valeur entrée n'est pas un nombre, redemande à l'utilisateur
        # de fournir une valeur.
        try:
            min = float(min)

        except ValueError:
            print("Valeur invalide. Veuillez fournir un nombre.")
            continue

        return min


def input_max():
    """
    DESC: Offre à l'utilisateur l'option d'entrer un maximum pour le filtre
    de limitation par plage minimum-maximum. Si aucune valeur n'est entrée,
    la valeur par défaut de 15,0 est sélectionnée.

    RETOUR: Float correspondant au maximum
    """
    while True:
        max = input("> Valeur maximum (facultatif): ").strip()

        # Comme enter une valeur maximum est facultative, une valeur par défaut
        # est utilisée si aucune valeur n'est entrée par l'utilisateur
        if max == "":
            max = 15.0

        # L'utilisateur peut quitter le programme en entrant q
        elif max == str.lower("q"):
            sys.exit()

        # Si la valeur entrée n'est pas un nombre, redemande à l'utilisateur
        # de fournir une valeur.
        try:
            max = float(max)

        except ValueError:
            print("Valeur invalide. Veuillez fournir un nombre.")
            continue

        return max


def main():
    """
    DESC: Affiche des instructions à l'utilisateur et lui demande de fournir 
    un ficher de données lidar à filrer, un nom pour le fichier en sortie 
    et un choix de méthode de filtrage. Lis le ficher de données, filtre les 
    données, écris les données filtrées dans un fichier texte et affiche des 
    statistiques liées au résultat obtenu.

    RETOUR: Aucun
    """

    print("=== Filtrage des données lidar ===")
    print("""
    Entrez un ficher de données lidar à filrer, un nom pour le fichier en sortie 
    et un choix de méthode de filtrage. Entrez q pour quitter le programme. 
    Les options de filtre sont les suivantes: \n
          1 - Limitation par plage minimum-maximum
          2 - Filtrage par moyenne mobile
          3 - Filtrage par médiane mobile
          \n""")

    # Demande à l'utilisateur d'entrer les informations demandées
    fichier_intrant = input_fichier_intrant()
    fichier_filtre = input_fichier_filtre()
    filtre = input_filtre()

    # Lis le fichier de données lidar en entrée
    sample = lecture(fichier_intrant)

    # Applique le filtre selon le numéro de filtre choisi
    if filtre == "1":
        sample_filtre = filtrage.filtre_min_max(sample, input_min(), input_max())

    elif filtre == "2":
        sample_filtre = filtrage.filtre_moyenne(sample)

    elif filtre == "3":
        sample_filtre = filtrage.filtre_mediane(sample)

    # Écris les données filtrées dans un fichier texte
    ecriture(fichier_filtre, sample_filtre)

    # Crée une liste contenant uniquement les données filtrées valides (>=0)
    sample_valide = stats.nombres_valides(sample_filtre)

    # Affiche le nombre de points traités et le nombre de points valides
    print("\n=== Résultat du filtrage des données lidar ===")
    print(f"""
    Nombre de points d'entrée analysés: {len(sample)}

    Statistiques des valeurs valides après filrage:

    Nombre de points valides: {len(sample_valide)}""")

    # S'il y a des points valides, affiche les statistiques des données
    # filtrées valides
    if len(sample_valide) > 0:
        print(
    f"""    Valeur minimale: {round(stats.min(sample_valide), 3)}
    Valeur maximale: {round(stats.max(sample_valide), 3)}
    Médiane: {round(stats.mediane(sample_valide), 3)}
    Moyenne: {round(stats.moyenne(sample_valide), 3)}
        """)


# ===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme

    RETOUR: Aucun
    """
    main()
