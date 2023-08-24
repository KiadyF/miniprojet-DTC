import sys
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import QFile
from .Qt_designer import Ui_Fenetrelogin


class FenetreLogin(QWidget, Ui_Fenetrelogin):
    def __init__(self):
        super(FenetreLogin, self).__init__()
        self.setupUi(self)
        self.setFixedSize(403, 463)
        self.setWindowTitle("LOGIN")
        self.login.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)
        self.signup.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)

        # Qdialog à afficher lorsque le mot de pass ou l'username est erroné
        self.dialg = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(
            "Mot de passe ou nom d'utlisateur erroné. Veuillez reessayer.")
        layout.addWidget(label)
        ok_button = QPushButton("OK")
        # Closes the dialog when OK is clicked
        ok_button.clicked.connect(self.dialg.accept)
        layout.addWidget(ok_button)
        self.dialg.setLayout(layout)
