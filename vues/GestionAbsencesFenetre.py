import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from .Qt_designer import Ui_recapabsentFenetre


class AbsenceFenetre(QWidget, Ui_recapabsentFenetre):
    def __init__(self):
        super(AbsenceFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("RECAP ABSENCES")
        self.revenir.setStyleSheet("""
            QPushButton{
                border-radius:10px;
                background-color: rgb(255, 163, 72);
                color: rgb(255, 255, 255);
                }
                QPushButton:pressed{
                background-color: rgb(230, 97, 0);
                }
        """)
