### 📝 Sujet de TP : **"Développement d’un Gestionnaire de Capteurs Connectés"**

#### 🎯 **Objectif du TP**  
Ce TP consiste à concevoir une application simulant la gestion d'un réseau de capteurs connectés. Vous développerez un système capable de recevoir des données de capteurs simulés, de les persister, de les manipuler sous différents formats et de les visualiser via une interface graphique.

---

#### 🧩 **Compétences mobilisées**  
Ce TP couvre les thématiques de la formation :  
✅ Utilisation avancée des collections et fonctions Python (*args, **kwargs, lambda, map, filter)  
✅ Programmation orientée objet (POO) appliquée au réseau et multithreading  
✅ Synchronisation multithread avec `lock`, `mutex`, `sémaphore`  
✅ Programmation réseau avec sockets (TCP/UDP)  
✅ Persistance des données avec JSON et SQLite  
✅ Manipulation de fichiers XML (DOM, SAX, Xpath)  
✅ Interface graphique avec PyQt ou Tkinter  

---

#### 🖥️ **Contexte**  
Vous êtes chargé de développer une application pour surveiller des capteurs environnementaux envoyant des données de température et d'humidité. Le système doit :  
1. Simuler des capteurs (clients réseau) envoyant périodiquement des données.  
2. Gérer un serveur recevant des données de plusieurs capteurs simultanément.  
3. Persister les données dans des fichiers JSON et une base SQLite.  
4. Permettre l’export des données en XML et la recherche avec Xpath.  
5. Offrir une interface graphique affichant les données en temps réel.  

---

#### 📝 **Fonctionnalités demandées**  

### 🧪 **1. Simulation des capteurs (clients réseau)**  
- Créez une classe `Sensor` avec les attributs :  
  - `id` : identifiant unique  
  - `location` : emplacement du capteur  
  - `temperature` : valeur aléatoire entre -10°C et 40°C  
  - `humidity` : valeur aléatoire entre 0% et 100%  
- Implémentez la génération de données envoyées au serveur via des sockets TCP toutes les 2 secondes.  
- Permettez la configuration dynamique des capteurs avec *args et **kwargs.  

---

### 🖧 **2. Gestion du serveur (multithread et synchronisation)**  
- Créez un serveur capable de gérer plusieurs connexions simultanées grâce au module `threading`.  
- Utilisez un `ThreadPoolExecutor` pour optimiser la gestion des connexions.  
- Protégez l’accès aux fichiers partagés avec des `locks` pour éviter les conflits d’écriture.  
- Limitez le nombre de connexions simultanées avec un `sémaphore` (maximum 5 capteurs connectés).  

---

### 💾 **3. Persistance des données**  
- À chaque réception de données :  
  - Enregistrez-les dans un fichier JSON (`data.json`).  
  - Insérez-les dans une base SQLite avec les colonnes : `id`, `timestamp`, `location`, `temperature`, `humidity`.  
- Implémentez des requêtes SQLite pour :  
  - Récupérer l’historique des données d’un capteur donné.  
  - Calculer la moyenne de température et d’humidité sur une période.  

---

### 📄 **4. Manipulation de fichiers XML**  
- Créez une fonction permettant d’exporter les données de la base SQLite vers un fichier XML.  
- Implémentez deux méthodes de lecture du fichier XML :  
  - **DOM** : Pour lire et manipuler la structure entière du fichier.  
  - **SAX** : Pour lire des fichiers volumineux sans consommer trop de mémoire.  
- Ajoutez des requêtes Xpath pour rechercher :  
  - Les entrées avec une température supérieure à 30°C.  
  - Les données d’un capteur spécifique.  

---

### 🖥️ **5. Interface graphique (PyQt ou Tkinter)**  
- Créez une interface graphique avec les fonctionnalités suivantes :  
  - Affichage en temps réel des données reçues.  
  - Bouton pour exporter les données en XML.  
  - Zone de recherche pour afficher l’historique d’un capteur spécifique.  
  - Graphique affichant l’évolution de la température et de l’humidité sur les dernières 5 minutes.  
 

