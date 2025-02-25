from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import random


class Jeu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jeu du nombre mystère")
        self.max_attempts = 5
        self.init_game()
        self.display_game()
    
    def init_game(self):
        self.secret_numer = random.randint(1,20)
        self.attempts = self.max_attempts
    
    def display_game(self):
        self.layout = QVBoxLayout()
        self.info_label = QLabel("Devinez le nombre entre 1 et 20 : ")
        self.layout.addWidget(self.info_label)
        self.attempts_label = QLabel(f"Essais restants : {self.attempts}")
        self.layout.addWidget(self.attempts_label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Entrez un nombre ...")
        self.layout.addWidget(self.input_field)

        self.submit_button = QPushButton("Valider")
        self.layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.check_guess)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)
        self.setLayout(self.layout)

    def check_guess(self):
        guess_text = self.input_field.text()
        if not guess_text.isdigit():
            self.result_label.setText("Merci de saisir un nombre entre 1 et 20")
            return
        
        guess = int(guess_text)

        self.attempts -=1
        self.attempts_label.setText(f"Essais restants : {self.attempts}")

        if guess < self.secret_numer:
            self.result_label.setText("Plus grand !!!!")
        elif guess > self.secret_numer:
            self.result_label.setText("Plus petit !!!!")
        else :
            self.result_label.setText("bravo vous avez gagné")
        
        if self.attempts == 0 and guess != self.secret_numer:
            self.result_label.setText("Perdu !!!!! ")
            self.init_game()
            self.attempts_label.setText(f"Essais restants : {self.attempts}")
            self.input_field.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = Jeu()
    window.show()
    app.exec()