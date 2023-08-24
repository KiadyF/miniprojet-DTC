# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetrelisteetudiants.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QWidget)

class Ui_listedesetudiants(object):
    def setupUi(self, listedesetudiants):
        if not listedesetudiants.objectName():
            listedesetudiants.setObjectName(u"listedesetudiants")
        listedesetudiants.resize(800, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(listedesetudiants.sizePolicy().hasHeightForWidth())
        listedesetudiants.setSizePolicy(sizePolicy)
        self.titre = QLabel(listedesetudiants)
        self.titre.setObjectName(u"titre")
        self.titre.setGeometry(QRect(40, 30, 711, 81))
        self.titre.setStyleSheet(u"font: 75 18pt \"Ubuntu\";\n"
"color: rgb(53, 132, 228);")
        self.scrollArea = QScrollArea(listedesetudiants)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(29, 99, 741, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 739, 549))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.ajoutNewEtudiant = QPushButton(listedesetudiants)
        self.ajoutNewEtudiant.setObjectName(u"ajoutNewEtudiant")
        self.ajoutNewEtudiant.setGeometry(QRect(250, 670, 250, 40))
        self.ajoutNewEtudiant.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.retranslateUi(listedesetudiants)

        QMetaObject.connectSlotsByName(listedesetudiants)
    # setupUi

    def retranslateUi(self, listedesetudiants):
        listedesetudiants.setWindowTitle(QCoreApplication.translate("listedesetudiants", u"Form", None))
        self.titre.setText(QCoreApplication.translate("listedesetudiants", u"Liste des etudiants incrits sur le cours: ", None))
        self.ajoutNewEtudiant.setText(QCoreApplication.translate("listedesetudiants", u"Ajouter un nouveau etudiant", None))
    # retranslateUi

