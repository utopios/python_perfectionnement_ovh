from threading import Thread

# ma_liste = []

# def ajouter_elements():
#     for _ in range(1000):
#         ma_liste.append(1)

# threads = [Thread(target=ajouter_elements) for _ in range(10)]

# for t in threads: t.start()
# for t in threads: t.join()

# print("Taille réelle : ", len(ma_liste))

import random
# from threading import Thread
import time
# def print_vide():
#     print("Bonjour !")
# def print_avec_texte(text):
#     time.sleep(random.random()*3)
#     print("Mon texte:", text)
# for i in range(3):
#     t = Thread(target= print_vide)
#     t.start()
# for i in range(3):
#     t = Thread(target= print_avec_texte, args= (i,))
#     t.start()

class LogiqueCustomThread(Thread):
    def __init__(self, str):
        super().__init__()
        self.str = str
    def run(self):
        for i in range(6):
            print(self.str, i)
            time.sleep(random.random()*3)


customThread = LogiqueCustomThread("Hello ")
customThread.start()
customThread.join()

## Lire un fichier texte:
with open("file.txt", 'r') as ficher:
    contenu = ficher.read()