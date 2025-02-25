import socket
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

HOST = '127.0.0.1'
PORT = 65432
MAX_WORKERS=3

def handle_client(conn, addr):
    print(f"connecté à {addr}")
    try:
        data = conn.recv(4096).decode('utf-8')
        if not data:
            return
        try:
            root = ET.fromstring(data)
            total = 0.0
            for produit in root.find('produits'):
                prix = float(produit.find('prix').text)
                quantite = int(produit.find('quantite').text)
                total += prix * quantite

            resultat = ET.Element('resultat')
            ET.SubElement(resultat, 'id').text = root.find('id').text
            ET.SubElement(resultat, 'total').text = f"{total:.2f}"

            response = ET.tostring(resultat, encoding='utf-8')
            conn.sendall(response)
        except ET.ParseError:
            conn.sendall(b"<error>Invalid XML Format</error>")
    finally:
        conn.close()
        print(f"déconnecté de {addr}")

def start_server():
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((HOST, PORT))
            server.listen()
            print(f"Serveur sur {HOST}:{PORT} avec {MAX_WORKERS} threads.")

            while True:
                conn, addr = server.accept()
                executor.submit(handle_client, conn, addr)
                print(f"connexion prise en charge.")

if __name__ == "__main__":
    start_server()