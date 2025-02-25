### **TP3 : Développement d'une Application Client-Serveur avec Interface Graphique et Traitement XML en Python**

#### **Contexte :**  
Ce TP vous place dans la peau d'un développeur chargé de créer une application de gestion des commandes de services cloud. L'application permettra de saisir des commandes au format XML, de les envoyer à un serveur distant pour traitement, et de récupérer les résultats calculés.

---

#### **Objectifs pédagogiques :**  
- Créer une interface graphique avec PyQt6 permettant la saisie d’informations au format XML.  
- Mettre en place un serveur TCP capable de recevoir, parser et traiter les données XML.  
- Implémenter un traitement serveur simulant le calcul de montants totaux de commandes.  
- Gérer la concurrence côté serveur pour accepter plusieurs requêtes simultanées.  
- Établir une communication bidirectionnelle entre le client (GUI) et le serveur.  

---

#### **Consignes :**

1. **Partie Client (Interface graphique avec PyQt6)**  
   - Créez une fenêtre permettant de saisir les informations suivantes :  
     - Nom du client  
     - Identifiant de commande  
     - Liste de produits avec le prix et la quantité  
   - Ajoutez un bouton **"Envoyer"** qui génère un fichier XML avec ces informations et l'envoie au serveur.  
   - Affichez le résultat retourné par le serveur (total de la commande) dans l'interface.

2. **Format XML attendu** *(exemple d’envoi)*  
```xml
<commande>
  <client>Jean Dupont</client>
  <id>CMD001</id>
  <produits>
    <produit>
      <nom>Hébergement Web</nom>
      <prix>9.99</prix>
      <quantite>2</quantite>
    </produit>
    <produit>
      <nom>Nom de Domaine</nom>
      <prix>12.50</prix>
      <quantite>1</quantite>
    </produit>
  </produits>
</commande>
```

3. **Partie Serveur (Traitement concurrent en Python)**  
   - Créez un serveur TCP capable de :  
     - Accepter plusieurs connexions simultanées (utilisez `threading` ou `asyncio`).  
     - Recevoir et parser les données XML.  
     - Calculer le total de la commande (`total = somme(prix * quantite)`).  
     - Retourner le total sous la forme d’une réponse XML.  

4. **Format de réponse XML** *(exemple de retour)*  
```xml
<resultat>
  <id>CMD001</id>
  <total>32.48</total>
</resultat>
```

---

#### **Aperçu de l'architecture :**

```plaintext
+--------------------+     TCP      +--------------------+
|  Client PyQt6      | <---------->  |     Serveur TCP    |
| (Envoi XML + GUI)  |               | (Parsing + Calcul) |
+--------------------+               +--------------------+
           ↑                                     ↓
 Affiche le total                       Gère plusieurs
 de la commande                           connexions
```
