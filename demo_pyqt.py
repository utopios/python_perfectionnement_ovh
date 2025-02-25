from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
# Création d'une application
app = QApplication([])
# Création d'une fenêtre principale
fenetre = QWidget()
fenetre.setWindowTitle("Ma première application PyQt6")
fenetre.resize(300,150)

layout = QVBoxLayout()

def direBonjour(): 
    label3.setText("Bnjour après click")

# Ajout d'un label
label1 = QLabel("Bonjour, PyQt6!")
label2 = QLabel("Bonjour, PyQt6!")
label3 = QLabel()
button1 = QPushButton("Dire bonjour")
button1.clicked.connect(direBonjour)
layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(button1)
layout.addWidget(label3)
fenetre.setLayout(layout)

fenetre.show()
# Lancement de la boucle principale
app.exec()