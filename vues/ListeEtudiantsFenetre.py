import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import QFile
from .Qt_designer import Ui_listedesetudiants


class ListeEtudiantFenetre(QWidget, Ui_listedesetudiants):
    def __init__(self):
        super(ListeEtudiantFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("LISTE DES ETUDIANTS")

        self.ajoutNewEtudiant.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)

        self.liste = QWidget()
        self.couche = QVBoxLayout()
        self.scrollArea.setWidget(self.liste)
        self.liste.setLayout(self.couche)

        self.retour = QPushButton("Retour", self)
        self.retour.setGeometry(370, 10, 95, 30)
        self.retour.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)
