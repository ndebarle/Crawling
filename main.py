import urllib.request
from bs4 import BeautifulSoup
import time

URLS=['https://ensai.fr/'] # L'URL initiale qui sera explorée
limiteURL = 50 # Le nombre d'URLS limite à partir duquel on explore plus. 
fichier_sauvegarde = 'crawled_webpages.txt' # Le nom du fichier qui contiendra la sauvegarde

## La fonction explore_liens utilise la liste URLS qui contient tous les liens à explorer
## Elle interroge la première URL, récupère les liens que l'éventuelle page contient.
## Elle les ajoute alors à la liste URLS et supprime l'URL qu'elle vient de suivre

def explore_liens():
    print('Exploration de l\'URL',URLS[0])
    try:
        with urllib.request.urlopen(URLS[0]) as f:
            soup = BeautifulSoup(f, 'html.parser')
            print(len(soup.find_all('a')), ' liens trouvés.')
            for link in soup.find_all('a'):
                URLS.append(link.get('href'))
            for link in soup.find_all('area'):
                URLS.append(link.get('href'))
    except:
        print('Erreur sur ce lien')
    URLS.remove(URLS[0])


def enregistre_URLS():
    fichier = open(fichier_sauvegarde, "a")
    fichier.write("\n".join(URLS))
    fichier.close()


## Programme principal
## On vérifie que la liste d'URLS est inférieure à la limite et non vide 
## et on lance la fonction explore_liens

while (len(URLS)<limiteURL and len(URLS)>0):
    explore_liens()
    time.sleep(5)

enregistre_URLS()
