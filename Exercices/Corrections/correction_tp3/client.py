import socket
import xml.etree.ElementTree as ET
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)

HOST = '127.0.0.1'
PORT = 65432

class ClientApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Client - Saisie de commande')

        self.client_label = QLabel('Nom du client:')
        self.client_input = QLineEdit()

        self.id_label = QLabel('ID de la commande:')
        self.id_input = QLineEdit()

        self.products_label = QLabel('Produits (nom,prix,quantité - un par ligne):')
        self.products_input = QTextEdit()

        self.send_button = QPushButton('Envoyer')
        self.send_button.clicked.connect(self.send_data)

        self.result_label = QLabel('Résultat:')
        self.result_display = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.client_label)
        layout.addWidget(self.client_input)
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(self.products_label)
        layout.addWidget(self.products_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def build_xml(self):
        commande = ET.Element('commande')
        ET.SubElement(commande, 'client').text = self.client_input.text()
        ET.SubElement(commande, 'id').text = self.id_input.text()
        produits = ET.SubElement(commande, 'produits')

        for line in self.products_input.toPlainText().split('\n'):
            if line.strip():
                try:
                    nom, prix, quantite = line.split(',')
                    produit = ET.SubElement(produits, 'produit')
                    ET.SubElement(produit, 'nom').text = nom.strip()
                    ET.SubElement(produit, 'prix').text = prix.strip()
                    ET.SubElement(produit, 'quantite').text = quantite.strip()
                except ValueError:
                    QMessageBox.warning(self, "Erreur", f"Format incorrect : {line}")
                    return None

        return ET.tostring(commande, encoding='utf-8')

    def send_data(self):
        xml_data = self.build_xml()
        if not xml_data:
            return

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(xml_data)
                response = s.recv(4096)

            try:
                root = ET.fromstring(response.decode('utf-8'))
                total = root.find('total').text
                self.result_display.setText(f"Total: {total} €")
            except ET.ParseError:
                self.result_display.setText("Erreur dans la réponse du serveur.")
        except ConnectionRefusedError:
            QMessageBox.critical(self, "Erreur", "Connexion au serveur impossible.")

if __name__ == '__main__':
    app = QApplication([])
    window = ClientApp()
    window.show()
    app.exec()
