from concurrent.futures import ThreadPoolExecutor
import time
def task(num):
    print(f"Task {num} started.")
    time.sleep(2)  # Simulation d'une tâche prenant du temps
    print(f"Task {num} finished.")
    return f"Task {num} result"

def main():
    # Création d'un ThreadPoolExecutor avec 3 threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Soumettre des tâches au pool d'exécution
        futures = [executor.submit(task, i) for i in range(5)]
        time.sleep(2)
        for future in futures:
            print(future.done(), future.running())
            
        # Récupérer les résultats des tâches
        for future in futures:
            result = future.result()
            print(result)
main()