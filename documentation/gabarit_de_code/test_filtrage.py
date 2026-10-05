"""
GRO120: Tests unitaires pour le module filtrage

Auteur: Francois Ferland
Date: 18/09/2025

Modifié par: ...
Date: ...
""" 

import filtrage

#===========================================
def test_filtre_min_max():
    """
    DESC: Test la fonction filtre_min_max
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon les valeurs minimum et maximum spécifiées 
    """
    
    # Ne pas vous limiter à un seul test par filtre...
    
    donnees = [1,50,0]
    reponse = [1,10,-1]
    test = filtrage.filtre_min_max(donnees, 1, 10)
    assert test == reponse, f"Erreur: {test} != {reponse}"
    
    
    
    pass


#===========================================
# Autres tests à compléter...
#===========================================









#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme
    """ 
    test_filtre_min_max()


    
    print("Tous les tests ont réussi.")