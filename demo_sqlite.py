import sqlite3

DB_FILE = "testdb.sqlite"


conn = sqlite3.connect(DB_FILE)
# Création d'un curseur
cursor = conn.cursor()
# Création d'une table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# Insertion de quelques données
users_data = [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35)
]
cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users_data)
# Commit des modifications et fermeture du curseur
conn.commit()
# Utilisation d'un curseur pour récupérer les données et les afficher
cursor.execute('SELECT * FROM users')
print("Données dans la table users :")
for row in cursor.fetchall():
    print(row)
# Fermeture de la connexion
conn.close()

