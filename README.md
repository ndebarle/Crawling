# Crawling
TP1 d'indexation web

# Pour lancer l'application

Il suffit d'executer le fichier main.py sans paramètre.

# Description de l'application

L'application part du lien "https://ensai.fr"
Elle lit le fichier robots.txt pour savoir si le crawling est autorisé.
Elle télécharge la page et récupère les liens qu'elle trouve dans les balises "a" 
et les balises "area".
Elle attend 5 secondes et renouvelle l'opération avec le premier lien trouvé 
si le nombre de liens en attente est inférieure à 50.

Elle enregistre alors les URL restant à explorer dans le fichier crawled_webpages.txt
