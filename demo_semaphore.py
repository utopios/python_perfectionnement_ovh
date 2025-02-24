import threading
import time
# Nombre total de ressources disponibles
nombre_ressources = 3
# Création du sémaphore
semaphore = threading.Semaphore(nombre_ressources)
# Fonction exécutée par chaque thread
def utiliser_ressource(thread_id):
    print(f"Thread {thread_id} en attente d'accès à la ressource.")
    # Acquérir le sémaphore
    semaphore.acquire()
    print(f"Thread {thread_id} accède à la ressource.")
    time.sleep(5)  # Simulation d'utilisation de la ressource
    print(f"Thread {thread_id} libère la ressource.")
    # Libérer le sémaphore
    semaphore.release()
def main():
    # Créer et démarrer plusieurs threads
    threads = []
    for i in range(6):
        thread = threading.Thread(target=utiliser_ressource, args=(i,))
        threads.append(thread)
        thread.start()
    # Attendre que tous les threads aient terminé leur travail
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    main()