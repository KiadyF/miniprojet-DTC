import sys
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QFile
from .Qt_designer import Ui_insciptionEtudiants


class InscriptionNewEtudiantFenetre(QWidget, Ui_insciptionEtudiants):
    def __init__(self):
        super(InscriptionNewEtudiantFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(450, 400)
        self.setWindowTitle("NEW STUDENT")

        self.submit.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)
        self.cancel.setStyleSheet("""
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
            "Merci de bien remplir tous les champs")
        layout.addWidget(label)
        ok_button = QPushButton("OK")
        # Closes the dialog when OK is clicked
        ok_button.clicked.connect(self.dialg.accept)
        layout.addWidget(ok_button)
        self.dialg.setLayout(layout)
