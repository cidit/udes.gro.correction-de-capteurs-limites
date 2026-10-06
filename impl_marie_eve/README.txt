QUELQUES PISTES POUR RÉSOUDRE LA PROBLÉMATIQUE:

1. Lancez le programme de tests (« test_filtrage.py »). 
   Le programme va normalement déclencher une erreur. 
   C’est normal – la fonction de filtrage de « filtrage.py » ne retourne rien (« pass »). 

2. Concentrez-vous maintenant sur l’implémentation de la fonction de filtrage. 
   Commencez par relire les requis pour le filtrage selon les limites min-max. 
   Faites un diagramme d’activité simple pour réfléchir à l’algorithme qui peut être utilisé ici. 
   Normalement, vous devriez tester quelques conditions pour déterminer la valeur de sortie pour chaque valeur d’entrée. 
   Une fois que vous avec votre algorithme en tête, implémentez-le en Python. 
   Pour simplifier le travail, vous pouvez commencer par tester une seule condition, par exemple en ne traitant que la borne maximale.

3. Relancez le programme de tests (« test_filtrage.py »). 
   Est-ce qu’il fonctionne ? 
   	- Si c’est le cas, vous avez réussi ce premier test. 
   	- Sinon, pensez à utiliser le débogueur pour suivre les cas où la réponse est incorrecte. 
   Est-ce que le problème est dans votre diagramme d’activité originale ou dans la transcription en Python ?

4. Pour les tests, vous pouvez débuter par l’entrée de données à la main (tableau), 
   en gardant en tête qu’il faudra également tester avec une lecture de fichier 
   (voir les problèmes à cet effet en activité procédurale et les exemples dans vos lectures).
  
5. Maintenant que vous avez un filtre fonctionnel et testé, vous pouvez vous attaquer aux autres filtres. 
   Une piste de solution additionnelle : le filtre par moyenne et médiane auront sûrement une structure similaire. 
   N’essayez-pas de régler les deux en même temps. 
   Concentrez-vous plutôt à en rendre un 100% fonctionnel (et testé!), et la complétion du deuxième sera beaucoup plus simple.

6. Lorsque les 3 filtres sont testés et fonctionnels, vous pouvez poursuivre avec le module « banc_lidar.py ».
   Voir les commentaires en entête de ce module, pour connaitre les étapes de traitement attendues.
