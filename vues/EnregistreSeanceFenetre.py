import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from .Qt_designer import Ui_enregistrerseancefenetre


class EnregistrationSeanceFenetre(QWidget, Ui_enregistrerseancefenetre):
    def __init__(self):
        super(EnregistrationSeanceFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(500, 500)
        self.setWindowTitle("ENREGISTRER UNE SEANCE")
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
