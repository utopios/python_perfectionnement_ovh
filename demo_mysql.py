"""Module pour tester intéraction avec du sql (mysql)"""

import mysql.connector  # pip install mysql-connector-python

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="demo"
)
# Création d'un curseur
cursor = conn.cursor()
# Création d'une table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users
                  (id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255),
                   age INT)"""
)
# Insertion de quelques données
users_data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
cursor.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", users_data)
# Commit des modifications
conn.commit()
# Sélection des données et affichage
cursor.execute("SELECT * FROM users")
print("Données dans la table users :")
for row in cursor.fetchall():
    print(row)
# Fermeture du curseur et de la connexion
cursor.close()
conn.close()

def add(a:int, b:int) -> int:
    return a+b

add(10, "2")