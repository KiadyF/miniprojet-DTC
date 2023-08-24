import sys
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import QFile
from .Qt_designer import Ui_UserinscriptionFenetre


class InscriptionNewUserFenetre(QWidget, Ui_UserinscriptionFenetre):
    def __init__(self):
        super(InscriptionNewUserFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(403, 463)
        self.setWindowTitle("NEW USER")
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

        # Qdialog à afficher lorsque le mot de pass ou l'username est erroné
        self.dialg = QDialog(self)
        layout = QVBoxLayout()
        self.dialg_label = QLabel(
            "Merci de bien remplir tous les champs. Veuillez reessayer.")
        layout.addWidget(self.dialg_label)
        ok_button = QPushButton("OK")
        # Closes the dialog when OK is clicked
        ok_button.clicked.connect(self.dialg.accept)
        layout.addWidget(ok_button)
        self.dialg.setLayout(layout)
