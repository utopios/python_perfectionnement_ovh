from init_db import create_connection
from mysql.connector import Error

def ajouter_chien(nom, age, race_id):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Chien (Nom, Age, RaceId) VALUES (%s, %s, %s);", (nom, age, race_id))
            conn.commit()
            print(f"Last Id {cursor.lastrowid}")
        except Error as e:
            print(f"Erreur : {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

def consulter_tous_les_chiens():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Chien.Id, Chien.Nom, Chien.Age, Race.Nom FROM Chien INNER JOIN Race ON Chien.RaceId = Race.Id;")
            chiens = cursor.fetchall()
            for chien in chiens:
                print(f"ID: {chien[0]}, Nom: {chien[1]}, Age: {chien[2]}, Race: {chien[3]}")
        except Error as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            conn.close()

def consulter_chiens_par_race(race_id):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Id, Nom, Age FROM Chien WHERE RaceId = %s;", (race_id,))
            chiens = cursor.fetchall()
            for chien in chiens:
                print(f"ID: {chien[0]}, Nom: {chien[1]}, Age: {chien[2]}")
        except Error as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            conn.close()

def supprimer_chien(chien_id):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Chien WHERE Id = %s;", (chien_id,))
            conn.commit()
        except Error as e:
            print(f"Erreur : {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

def menu():
    while True:
        print("\n1. Ajouter un chien")
        print("2. Consulter tous les chiens")
        print("3. Consulter les chiens par race")
        print("4. Supprimer un chien")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom du chien : ")
            age = input("Âge du chien : ")
            race_id = input("ID de la race : ")
            ajouter_chien(nom, int(age), int(race_id))
        elif choix == "2":
            consulter_tous_les_chiens()
        elif choix == "3":
            race_id = input("ID de la race : ")
            consulter_chiens_par_race(int(race_id))
        elif choix == "4":
            chien_id = input("ID du chien à supprimer : ")
            supprimer_chien(int(chien_id))
        elif choix == "5":
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu()
