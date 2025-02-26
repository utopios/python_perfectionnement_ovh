import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'database': 'demo',
    'user': 'root',
    'password': ''
}

def create_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Erreur de connexion : {e}")
    return None

def init_db():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Race (
                Id INT AUTO_INCREMENT PRIMARY KEY,
                Nom VARCHAR(50) NOT NULL
            );""")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Chien (
                Id INT AUTO_INCREMENT PRIMARY KEY,
                Nom VARCHAR(50) NOT NULL,
                Age INT NOT NULL,
                RaceId INT,
                FOREIGN KEY (RaceId) REFERENCES Race(Id)
            );""")

            races = [("Labrador",), ("Berger Allemand",), ("Bulldog",)]
            cursor.executemany("INSERT INTO Race (Nom) VALUES (%s);", races)

            chiens = [("Max", 3, 1), ("Rex", 5, 2), ("Bella", 2, 3)]
            cursor.executemany("INSERT INTO Chien (Nom, Age, RaceId) VALUES (%s, %s, %s);", chiens)

            conn.commit()

        except Error as e:
            print(f"Erreur : {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    init_db()
