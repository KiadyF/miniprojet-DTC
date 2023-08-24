import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QDialog, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import QFile
from .Qt_designer import Ui_AjoutNouveauCours


class AjoutCoursFenetre(QWidget, Ui_AjoutNouveauCours):
    def __init__(self):
        super(AjoutCoursFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(500, 600)
        self.setWindowTitle("AJOUTER UN NOUVEAU COURS")
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
        # Qdialog à afficher lorsque le titre ou le chapitre est vide
        self.dialg = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(
            "Vous devez remplir le nom et entrer au moins un chapitre pour votre cours")
        layout.addWidget(label)
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.dialg.accept)
        layout.addWidget(ok_button)
        self.dialg.setLayout(layout)

        self.couche = QVBoxLayout()
        self.liste = QWidget()
        self.liste.setLayout(self.couche)
        self.scrollArea.setFixedSize(331, 351)
        self.scrollArea.setWidget(self.liste)
