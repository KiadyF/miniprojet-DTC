# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetrecours.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_FenetreCours(object):
    def setupUi(self, FenetreCours):
        if not FenetreCours.objectName():
            FenetreCours.setObjectName(u"FenetreCours")
        FenetreCours.resize(800, 600)
        FenetreCours.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 113, 216, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Ajouter = QPushButton(FenetreCours)
        self.Ajouter.setObjectName(u"Ajouter")
        self.Ajouter.setGeometry(QRect(80, 80, 101, 81))
        self.Ajouter.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"font-size:16px\n"
"")
        self.scrollArea = QScrollArea(FenetreCours)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(320, 80, 461, 501))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 459, 499))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ListedesCours = QGroupBox(self.scrollAreaWidgetContents)
        self.ListedesCours.setObjectName(u"ListedesCours")
        self.ListedesCours.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Ubuntu\";")
        self.ListedesCours.setAlignment(Qt.AlignCenter)
        self.ListedesCours.setFlat(True)

        self.verticalLayout.addWidget(self.ListedesCours)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(FenetreCours)

        QMetaObject.connectSlotsByName(FenetreCours)
    # setupUi

    def retranslateUi(self, FenetreCours):
        FenetreCours.setWindowTitle(QCoreApplication.translate("FenetreCours", u"Form", None))
        self.Ajouter.setText(QCoreApplication.translate("FenetreCours", u"Ajouter", None))
        self.ListedesCours.setTitle(QCoreApplication.translate("FenetreCours", u"LISTE DE VOS COURS", None))
    # retranslateUi

