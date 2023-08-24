import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import QFile
from .Qt_designer import Ui_seanceFenetre


class GestionSeancesFenetre(QWidget, Ui_seanceFenetre):
    def __init__(self):
        super(GestionSeancesFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("SEANCES")
        self.plannifier.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)
        self.enregistrer.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)
        self.retour.setStyleSheet("""
            QPushButton{
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));
                border:0px;
                color: rgb(255, 255, 255);
                border-radius:5px
                }
                QPushButton:pressed{
                background-color: rgb(26, 95, 180);
                }
        """)
        self.deconnecter.setStyleSheet("""
            QPushButton{
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));
                border:0px;
                color: rgb(255, 255, 255);
                border-radius:5px
                }
                QPushButton:pressed{
                background-color: rgb(26, 95, 180);
                }
        """)

        self.layout_prochaine_seance = QVBoxLayout()
        prochaineseance = QWidget()
        prochaineseance.setLayout(self.layout_prochaine_seance)
        self.scrollAreaprochaineseance.setWidget(prochaineseance)
