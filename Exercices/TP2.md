**TP - Gestion du Multithreading chez OVH : Gestion de requêtes client en parallèle**

## 🎯 **Contexte**
Chez OVH, le traitement de nombreuses requêtes simultanées (création de serveurs, suppression, redémarrage) est courant. La gestion efficace de ces requêtes est essentielle pour assurer la réactivité et l'intégrité des systèmes.

Ce TP vous propose de simuler un environnement où des clients envoient des requêtes variées en parallèle. L'objectif est d'utiliser le multithreading pour traiter ces requêtes tout en évitant les conditions de course.

---

## 📝 **Objectifs pédagogiques**
- Comprendre la création et la gestion de threads en Python.
- Utiliser les verrous (`Lock`, `Semaphore`) pour protéger les ressources partagées.
- Mettre en place un pool de threads avec `ThreadPoolExecutor`.
- Observer les impacts de la concurrence sur les données.
- Comparer les performances avec et sans multithreading.

---

## 🧩 **Consignes du TP**
1. Implémentez une classe `ServeurManager` qui :
   - Contient une liste partagée de serveurs.
   - Dispose de méthodes pour créer, redémarrer et supprimer des serveurs.
   - Protège les accès avec un `Lock`.
2. Simulez des clients envoyant des requêtes aléatoires à l'aide de threads.
3. Utilisez un `ThreadPoolExecutor` pour gérer un nombre limité de threads actifs.
4. Affichez les logs avec timestamps pour suivre le déroulement des opérations.


## 🧪 **Exercices supplémentaires**
1. **Limitation des accès :** Ajoutez un `Semaphore` pour restreindre le nombre de requêtes concurrentes.
2. **Gestion des exceptions :** Ajoutez des vérifications pour éviter les suppressions lorsque la liste est vide.
3. **Comparaison de performances :**
   - Exécutez le code avec et sans le pool de threads.
   - Mesurez les temps d'exécution et commentez les résultats.
4. **Ajout de fonctionnalités :**
   - Ajoutez une fonction de consultation des serveurs actifs.
   - Implémentez une file d'attente de requêtes pour simuler des pics de charge.


