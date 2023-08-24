# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetreajoutcours.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_AjoutNouveauCours(object):
    def setupUi(self, AjoutNouveauCours):
        if not AjoutNouveauCours.objectName():
            AjoutNouveauCours.setObjectName(u"AjoutNouveauCours")
        AjoutNouveauCours.resize(500, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AjoutNouveauCours.sizePolicy().hasHeightForWidth())
        AjoutNouveauCours.setSizePolicy(sizePolicy)
        self.nom = QLineEdit(AjoutNouveauCours)
        self.nom.setObjectName(u"nom")
        self.nom.setGeometry(QRect(80, 30, 330, 30))
        self.nom.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.nom.setAlignment(Qt.AlignCenter)
        self.chapitres = QGroupBox(AjoutNouveauCours)
        self.chapitres.setObjectName(u"chapitres")
        self.chapitres.setGeometry(QRect(80, 60, 331, 401))
        self.chapitres.setStyleSheet(u"font: 75 16pt \"Ubuntu\";\n"
"color: rgb(53, 132, 228);")
        self.scrollArea = QScrollArea(self.chapitres)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(9, 39, 311, 351))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 309, 349))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.newchpitre = QLineEdit(AjoutNouveauCours)
        self.newchpitre.setObjectName(u"newchpitre")
        self.newchpitre.setGeometry(QRect(80, 470, 330, 30))
        self.newchpitre.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.newchpitre.setAlignment(Qt.AlignCenter)
        self.cancel = QPushButton(AjoutNouveauCours)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(80, 530, 121, 41))
        self.cancel.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.submit = QPushButton(AjoutNouveauCours)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(290, 530, 121, 41))
        self.submit.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.retranslateUi(AjoutNouveauCours)

        QMetaObject.connectSlotsByName(AjoutNouveauCours)
    # setupUi

    def retranslateUi(self, AjoutNouveauCours):
        AjoutNouveauCours.setWindowTitle(QCoreApplication.translate("AjoutNouveauCours", u"Form", None))
        self.nom.setText("")
        self.nom.setPlaceholderText(QCoreApplication.translate("AjoutNouveauCours", u"Nom du cours", None))
        self.chapitres.setTitle(QCoreApplication.translate("AjoutNouveauCours", u"Chapitres", None))
        self.newchpitre.setPlaceholderText(QCoreApplication.translate("AjoutNouveauCours", u"Ajouter un chapitre", None))
        self.cancel.setText(QCoreApplication.translate("AjoutNouveauCours", u"Cancel", None))
        self.submit.setText(QCoreApplication.translate("AjoutNouveauCours", u"Submit", None))
    # retranslateUi

