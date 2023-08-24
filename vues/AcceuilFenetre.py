import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QFile
from .Qt_designer import Ui_FenetreCours


class AcceuilFenetre(QWidget, Ui_FenetreCours):
    def __init__(self):
        super(AcceuilFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.setWindowTitle("ACCEUIL")

        self.Ajouter.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)
        self.couche = QVBoxLayout()
        self.ListedesCours.setLayout(self.couche)
        self.deconnecter = QPushButton("Deconnecter", self)
        self.deconnecter.setGeometry(650, 20, 95, 30)
        self.deconnecter.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)
