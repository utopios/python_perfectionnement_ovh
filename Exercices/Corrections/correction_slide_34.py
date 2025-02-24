import os
from collections import Counter
from threading import Thread

resultats = []

def traiter_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            taille = os.path.getsize(nom_fichier)
            compteur = Counter(contenu)
        resultats.append({
            'fichier': nom_fichier,
            "taille": taille,
            "caractères": compteur
        })
       
    except Exception as e:
        print(e)

def main():
    fichiers = [f for f in os.listdir('.') if os.path.isfile(f)]
    threads = []
    for fichier in fichiers:
        thread = Thread(target=traiter_fichier, args=(fichier,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(resultats)

main()