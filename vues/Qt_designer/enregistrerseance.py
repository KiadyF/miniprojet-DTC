# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetrerenregisterseance.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_enregistrerseancefenetre(object):
    def setupUi(self, enregistrerseancefenetre):
        if not enregistrerseancefenetre.objectName():
            enregistrerseancefenetre.setObjectName(u"enregistrerseancefenetre")
        enregistrerseancefenetre.resize(500, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(enregistrerseancefenetre.sizePolicy().hasHeightForWidth())
        enregistrerseancefenetre.setSizePolicy(sizePolicy)
        self.cancel = QPushButton(enregistrerseancefenetre)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(30, 420, 121, 40))
        self.cancel.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.submit = QPushButton(enregistrerseancefenetre)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(330, 420, 121, 40))
        self.submit.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.activites = QTextEdit(enregistrerseancefenetre)
        self.activites.setObjectName(u"activites")
        self.activites.setGeometry(QRect(40, 130, 401, 151))
        self.activites.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.label = QLabel(enregistrerseancefenetre)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 90, 141, 17))
        self.label.setStyleSheet(u"color: rgb(53, 132, 228);\n"
"font: 75 16pt \"Ubuntu\";")
        self.label_2 = QLabel(enregistrerseancefenetre)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 20, 371, 41))
        self.label_2.setStyleSheet(u"font: 75 26pt \"Ubuntu\";\n"
"color: rgb(53, 132, 228);")
        self.label_3 = QLabel(enregistrerseancefenetre)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 310, 141, 17))
        self.label_3.setStyleSheet(u"color: rgb(53, 132, 228);\n"
"font: 75 16pt \"Ubuntu\";")

        self.retranslateUi(enregistrerseancefenetre)

        QMetaObject.connectSlotsByName(enregistrerseancefenetre)
    # setupUi

    def retranslateUi(self, enregistrerseancefenetre):
        enregistrerseancefenetre.setWindowTitle(QCoreApplication.translate("enregistrerseancefenetre", u"Form", None))
        self.cancel.setText(QCoreApplication.translate("enregistrerseancefenetre", u"Cancel", None))
        self.submit.setText(QCoreApplication.translate("enregistrerseancefenetre", u"Submit", None))
        self.activites.setPlaceholderText(QCoreApplication.translate("enregistrerseancefenetre", u"Activit\u00e9s faites:", None))
        self.label.setText(QCoreApplication.translate("enregistrerseancefenetre", u"Choix seances", None))
        self.label_2.setText(QCoreApplication.translate("enregistrerseancefenetre", u"Enregistrer une seances", None))
        self.label_3.setText(QCoreApplication.translate("enregistrerseancefenetre", u"Les absences", None))
    # retranslateUi

