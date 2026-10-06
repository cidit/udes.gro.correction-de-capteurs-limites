"""
GRO120: Tests unitaires pour le module filtrage

Auteur: Francois Ferland
Date: 18/09/2025

Modifié par: Marie-Eve Le Ber (lebm2924) et Félix St-Gelais (stgf5468)
Date: 06/10/2026
""" 

import filtrage


def test_filtre_min_max():
    """
    DESC: Test la fonction filtre_min_max
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon les valeurs minimum et maximum spécifiées 

    RETOUR: Aucun
    """
    # Test la fonction filtre_min_max avec les données input
    input = [1,50,0]
    output = [1,10,-1]
    test = filtrage.filtre_min_max(input, 1, 10)
    # Compare le résultat de la fonction avec le résultat attendu
    assert test == output, f"Erreur: {test} != {output}"


def test_filtre_moyenne():
    """
    DESC: Test la fonction filtre_moyenne
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon une moyenne mobile ayant une fenêtre de 3 valeurs. Pour le 
          premier et dernier point du tableau, seuls 2 valeurs sont utilisées.

    RETOUR: Aucun
    """
    # Test la fonction filtre_moyenne avec les données input
    input = [1, 3, 2, 4, 5, 3]
    output = [2.0, 2.0, 3.0, 3.7, 4.0, 4.0]
    test = filtrage.filtre_moyenne(input)
    # Compare le résultat de la fonction avec le résultat attendu.
    # We round each member before the comparison because the provided expected
    # output doesnt take into account that the actual answer has a period in one
    # of the entries.
    assert [round(num) for num in test] == [round(num) for num in output], f"Erreur: {test} != {output}"

def test_filtre_moyenne_1nb():
    """
    DESC: Test la fonction filtre_moyenne avec un tableau qui ne contient qu'un 
    nombre.

    RETOUR: Aucun
    """
    # Test la fonction filtre_moyenne avec les données input
    input = [1]
    output = [1.0]
    test = filtrage.filtre_moyenne(input)
    # Compare le résultat de la fonction avec le résultat attendu.
    # We round each member before the comparison because the provided expected
    # output doesnt take into account that the actual answer has a period in one
    # of the entries.
    assert [round(num) for num in test] == [round(num) for num in output], f"Erreur: {test} != {output}"

def test_filtre_moyenne_2nb():
    """
    DESC: Test la fonction filtre_moyenne avec un tableau qui ne contient que 2 
    nombres.

    RETOUR: Aucun
    """
    # Test la fonction filtre_moyenne avec les données input
    input = [1, 3]
    output = [2.0, 2.0]
    test = filtrage.filtre_moyenne(input)
    # Compare le résultat de la fonction avec le résultat attendu.
    # We round each member before the comparison because the provided expected
    # output doesnt take into account that the actual answer has a period in one
    # of the entries.
    assert [round(num) for num in test] == [round(num) for num in output], f"Erreur: {test} != {output}"

def test_filtre_mediane():
    """
    DESC: Test la fonction filtre_mediane
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon une médiane mobile ayant une fenêtre de 3 valeurs. Le premier et
          dernier point de la liste ne sont pas traités.
    
    RETOUR: Aucun
    """
    # Test la fonction filtre_mediane avec les données input
    input = [1, 3, 2, 4, 5, 3]
    output = [1, 2, 3, 4, 4, 3]
    test = filtrage.filtre_mediane(input)
    # Compare le résultat de la fonction avec le résultat attendu.
    assert test == output, f"Erreur: {test} != {output}"

def test_filtre_mediane_1nb():
    """
    DESC: Test la fonction filtre_mediane avec un tableau qui ne contient qu'une
    valeur.

    RETOUR: Aucun
    """
    # Test la fonction filtre_mediane avec les données input
    input = [1]
    output = [1]
    test = filtrage.filtre_mediane(input)
    # Compare le résultat de la fonction avec le résultat attendu.
    assert test == output, f"Erreur: {test} != {output}"

def test_filtre_mediane_2nb():
    """
    DESC: Test la fonction filtre_mediane avec un tableau qui ne contient que 2
    valeurs.

    RETOUR: Aucun
    """
    # Test la fonction filtre_mediane avec les données input
    input = [1, 3]
    output = [1, 3]
    test = filtrage.filtre_mediane(input)
    # Compare le résultat de la fonction avec le résultat attendu.
    assert test == output, f"Erreur: {test} != {output}"


def main():
    """
    DESC: Effectue l'ensemble des tests unitaires un à la suite de l'autre.
    Les tests sont les suivants:
        - Test de la fonction filtre_min_max
        - Test de la fonction filtre_moyenne avec un tableau d'entrée standard,
            un tableau avec deux valeurs et un tableau avec une seule valeur
        - Test de la fonction filtre_mediane avec un tableau d'entrée standard,
            un tableau avec deux valeurs et un tableau avec une seule valeur

    RETOUR: Aucun
    """
    test_filtre_min_max()
    test_filtre_moyenne()
    test_filtre_moyenne_1nb()
    test_filtre_moyenne_2nb()
    test_filtre_mediane()
    test_filtre_mediane_1nb()
    test_filtre_mediane_2nb()
    
    print("Tous les tests ont réussi.")


#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme

    RETOUR: Aucun
    """
    main()
