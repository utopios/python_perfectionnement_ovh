### Sujet du TP : Analyse des Données COVID-19 avec Python et Pandas

#### **Objectif :**  
L’objectif de ce TP est d’analyser des données réelles sur le COVID-19 en utilisant la bibliothèque **Pandas** de Python. Vous manipulerez des données pour extraire des informations utiles telles que le nombre de cas confirmés, de décès, de personnes guéries, ainsi que la répartition par pays et provinces.

---

#### **Instructions :**  
1. Téléchargez le fichier de données **`covid_19.csv`** contenant les données mises à jour sur les cas de COVID-19.
2. Utilisez la bibliothèque `pandas` pour charger et analyser les données.
3. Réalisez les questions ci-dessous en produisant des résultats lisibles.

---

#### **Questions :**

### **Q1. Chargement et exploration des données**  
- Écrivez un programme Python pour afficher les **5 premières lignes** du jeu de données COVID-19.  
- Affichez également les **informations du jeu de données** (colonnes, types de données, valeurs non nulles).  
- Vérifiez la **présence de valeurs manquantes** dans chaque colonne.

---

### **Q2. Statistiques globales par pays**  
- Obtenez le **dernier nombre de cas confirmés, de décès, de personnes guéries et de cas actifs** pour chaque pays.  
- Ajoutez une colonne `Active` calculée par :  
  \[
  \text{Active} = \text{Confirmed} - \text{Deaths} - \text{Recovered}
  \]

---

### **Q3. Statistiques par pays et provinces/États**  
- Obtenez le **dernier nombre de cas confirmés, de décès et de personnes récupérées** par pays et par province/État.

---

### **Q4. Focus sur la Chine**  
- Affichez les **cas confirmés, les décès et les guérisons** pour chaque province de la Chine, triés par nombre de cas confirmés.

---

### **Q5. Liste des pays avec des décès signalés**  
- Affichez les **pays ayant enregistré au moins un décès** dû au COVID-19 avec le nombre de décès associés.

---

### **Q6. Liste des pays sans cas récupéré**  
- Identifiez les **pays où aucun cas n’a été récupéré**. Affichez les colonnes : `Country/Region`, `Confirmed`, `Deaths`, `Recovered`.

---

### **Q7. Liste des pays où tous les cas sont décédés**  
- Trouvez les **pays où tous les cas confirmés sont décédés**. Affichez le nombre total de cas et de décès.

---

### **Q8. Liste des pays où tous les cas sont récupérés**  
- Répertoriez les **pays où tous les cas confirmés ont été récupérés**. Affichez le nombre total de cas et de guérisons.

---

### **Q9. Top 10 des pays les plus touchés**  
- Affichez les **10 pays ayant le plus grand nombre de cas confirmés** avec les colonnes :  
  - Dernière mise à jour  
  - Pays/Région  
  - Confirmés  
  - Décès  
  - Récupérés  


#### **Bonus :**  
- Ajoutez des visualisations à l’aide de `matplotlib` ou `seaborn` pour représenter les données du **Top 10 des pays les plus touchés**.