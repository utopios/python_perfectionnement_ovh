from threading import Lock
import random
import time
from concurrent.futures import ThreadPoolExecutor
class ServerManager:
    def __init__(self):
        self.serveurs = []
        self.lock = Lock()
    
    def creer_serveur(self, client_id):
        
        # self.lock.acquire()
        # serveur = f"Serveur-{client_id}-{random.randint(1000, 9999)}"
        # self.serveurs.append(serveur)
        # print(f"[{time.strftime('%H:%M:%S')}] Client {client_id} : Créé {serveur}")
        # self.lock.release()
        
        with self.lock:
            serveur = f"Serveur-{client_id}-{random.randint(1000, 9999)}"
            self.serveurs.append(serveur)
            print(f"[{time.strftime('%H:%M:%S')}] Client {client_id} : Créé {serveur}")
            
        time.sleep(random.uniform(0.5, 1.5))

    def redemarrer_serveur(self, client_id):
        with self.lock:
            if self.serveurs:
                serveur = random.choice(self.serveurs)
                print(f"[{time.strftime('%H:%M:%S')}] Client {client_id} : Redémarre {serveur}")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] Client {client_id} : Aucun serveur à redémarrer.")

    def supprimer_serveur(self, client_id):
        with self.lock:
            if self.serveurs:
                serveur = self.serveurs.pop()
                print(f"[{time.strftime('%H:%M:%S')}] Client {client_id} : Supprimé {serveur}")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] Client {client_id} : Aucun serveur à supprimer.")


def traitement_requete(manager, client_id, action):
    actions = {
        "creer": manager.creer_serveur,
        "redemarrer": manager.redemarrer_serveur,
        "supprimer": manager.supprimer_serveur
    }
    actions.get(action)(client_id)


def main():
    manager = ServerManager()
    actions = ["creer", "redemarrer", "supprimer"]

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(traitement_requete, manager, i, random.choice(actions)) for i in range(20)]
        for future in futures:
            future.result()


if __name__ == "__main__":
    main()