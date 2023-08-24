# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetreinsciptionetudiant.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_insciptionEtudiants(object):
    def setupUi(self, insciptionEtudiants):
        if not insciptionEtudiants.objectName():
            insciptionEtudiants.setObjectName(u"insciptionEtudiants")
        insciptionEtudiants.resize(450, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(insciptionEtudiants.sizePolicy().hasHeightForWidth())
        insciptionEtudiants.setSizePolicy(sizePolicy)
        self.cancel = QPushButton(insciptionEtudiants)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(20, 300, 121, 40))
        self.cancel.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.submit = QPushButton(insciptionEtudiants)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(310, 300, 121, 40))
        self.submit.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.nom = QLineEdit(insciptionEtudiants)
        self.nom.setObjectName(u"nom")
        self.nom.setGeometry(QRect(20, 90, 411, 25))
        self.nom.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.nom.setAlignment(Qt.AlignCenter)
        self.prenom = QLineEdit(insciptionEtudiants)
        self.prenom.setObjectName(u"prenom")
        self.prenom.setGeometry(QRect(20, 150, 411, 25))
        self.prenom.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.prenom.setAlignment(Qt.AlignCenter)
        self.dateDeNaissance = QDateEdit(insciptionEtudiants)
        self.dateDeNaissance.setObjectName(u"dateDeNaissance")
        self.dateDeNaissance.setGeometry(QRect(270, 200, 161, 40))
        self.dateDeNaissance.setStyleSheet(u"color: rgb(255, 120, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 193, 241, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;\n"
"border:0px\n"
"")
        self.label = QLabel(insciptionEtudiants)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 200, 191, 41))
        self.label.setStyleSheet(u"font: 75 16pt \"Ubuntu\";\n"
"color: rgb(98, 160, 234);")
        self.label_2 = QLabel(insciptionEtudiants)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 40, 281, 31))
        self.label_2.setStyleSheet(u"font: 75 26pt \"Ubuntu\";\n"
"color: rgb(53, 132, 228);")

        self.retranslateUi(insciptionEtudiants)

        QMetaObject.connectSlotsByName(insciptionEtudiants)
    # setupUi

    def retranslateUi(self, insciptionEtudiants):
        insciptionEtudiants.setWindowTitle(QCoreApplication.translate("insciptionEtudiants", u"Form", None))
        self.cancel.setText(QCoreApplication.translate("insciptionEtudiants", u"Cancel", None))
        self.submit.setText(QCoreApplication.translate("insciptionEtudiants", u"Submit", None))
        self.nom.setPlaceholderText(QCoreApplication.translate("insciptionEtudiants", u"Entrer son nom", None))
        self.prenom.setPlaceholderText(QCoreApplication.translate("insciptionEtudiants", u"Entrer ici son prenom", None))
        self.label.setText(QCoreApplication.translate("insciptionEtudiants", u"Date de naissance", None))
        self.label_2.setText(QCoreApplication.translate("insciptionEtudiants", u"New Student", None))
    # retranslateUi

