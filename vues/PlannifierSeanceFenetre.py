import sys
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QFile
from .Qt_designer import Ui_prochaineseancesFenetre


class PlannificationSeanceFenetre(QWidget, Ui_prochaineseancesFenetre):
    def __init__(self):
        super(PlannificationSeanceFenetre, self).__init__()
        self.setupUi(self)
        self.setFixedSize(500, 500)
        self.setWindowTitle("PLANIFIER UNE SEANCE")
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
        self.dialg = QDialog(self)
        layout = QVBoxLayout()
        self.label5 = QLabel(
            "Merci de bien remplir tous les champs.")
        layout.addWidget(self.label5)
        ok_button = QPushButton("OK")
        # Closes the dialog when OK is clicked
        ok_button.clicked.connect(self.dialg.accept)
        layout.addWidget(ok_button)
        self.dialg.setLayout(layout)
