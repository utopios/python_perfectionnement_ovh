## **Travaux Pratiques (TP) Global : Gestion d'une plateforme de services**

### **Contexte :** Vous devez gérer des clients, des commandes, des services et leur facturation.

### **Consignes :**
1. **Gestion des services (POO avancée)** : 
   - Créez une classe abstraite `Service` avec des sous-classes comme `Serveur`, `Cloud`, et `Domaine`. 
   - Implémentez le polymorphisme via la méthode `calculer_prix`.
2. **Gestion des clients et commandes (collections avancées)** :
   - Utilisez un dictionnaire pour stocker les clients et leurs commandes.
   - Mettez en place une file d'attente pour les commandes en attente de traitement.
3. **Traitement des commandes (\*args, \**kwargs)** :
   - Créez une fonction `passer_commande(*args, **kwargs)` qui accepte plusieurs services avec des options comme "urgent", "remise".
4. **Facturation (lambda, filter, map)** :
   - Utilisez `map` pour calculer les montants.
   - Filtrez les commandes dépassant un certain montant avec `filter`.
5. **Passage des arguments et copies** :
   - Mettez en place un historique des commandes avec des copies pour préserver les états initiaux.
