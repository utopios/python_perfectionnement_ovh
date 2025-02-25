import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
class MonWidget(QWidget):
    def __init__(self, parent):
        super(). __init__(parent)
        layout = QVBoxLayout()
        label = QLabel('Mon Titre', self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(10, 10, 200, 20)
        imagelbl = QLabel(self)
        imagelbl.setPixmap(QPixmap('logo.svg').scaledToWidth(200))
        imagelbl.setGeometry(10, 30, 200, 100)
        imagelbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        imagelbl.setStyleSheet('border: 10px solid green;background-color: #5f68ad;')
        bouton = QPushButton('OK', self)
        bouton.setGeometry(10, 150, 200, 20)
        layout.addWidget(label)
        layout.addWidget(imagelbl)
        layout.addWidget(bouton)
        self.setLayout(layout)
class MaFenetre(QMainWindow):
    def __init__(self):
        super(). __init__()
        self.setWindowTitle('Pyqt')
        central_widget = MonWidget(self)
        self.setCentralWidget(central_widget)
        self.resize(250, 250)
def main():
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    app.exec()
if __name__ == '__main__':
    main()