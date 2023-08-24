# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetreseance.ui'
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
    QSizePolicy, QWidget)

class Ui_seanceFenetre(object):
    def setupUi(self, seanceFenetre):
        if not seanceFenetre.objectName():
            seanceFenetre.setObjectName(u"seanceFenetre")
        seanceFenetre.resize(800, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(seanceFenetre.sizePolicy().hasHeightForWidth())
        seanceFenetre.setSizePolicy(sizePolicy)
        self.retour = QPushButton(seanceFenetre)
        self.retour.setObjectName(u"retour")
        self.retour.setGeometry(QRect(50, 20, 89, 25))
        self.retour.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:0px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px\n"
"")
        self.deconnecter = QPushButton(seanceFenetre)
        self.deconnecter.setObjectName(u"deconnecter")
        self.deconnecter.setGeometry(QRect(688, 20, 91, 25))
        self.deconnecter.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:0px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px\n"
"")
        self.enregistrer = QPushButton(seanceFenetre)
        self.enregistrer.setObjectName(u"enregistrer")
        self.enregistrer.setGeometry(QRect(560, 690, 221, 40))
        self.enregistrer.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);")
        self.plannifier = QPushButton(seanceFenetre)
        self.plannifier.setObjectName(u"plannifier")
        self.plannifier.setGeometry(QRect(20, 690, 221, 40))
        self.plannifier.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);")
        self.prochaineseances = QGroupBox(seanceFenetre)
        self.prochaineseances.setObjectName(u"prochaineseances")
        self.prochaineseances.setGeometry(QRect(10, 120, 371, 531))
        self.prochaineseances.setStyleSheet(u"font: 75 18pt \"Ubuntu\";\n"
"color: rgb(53, 132, 228);")
        self.scrollAreaprochaineseance = QScrollArea(self.prochaineseances)
        self.scrollAreaprochaineseance.setObjectName(u"scrollAreaprochaineseance")
        self.scrollAreaprochaineseance.setGeometry(QRect(10, 40, 351, 481))
        self.scrollAreaprochaineseance.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 349, 479))
        self.scrollAreaprochaineseance.setWidget(self.scrollAreaWidgetContents)
        self.seancepasses = QGroupBox(seanceFenetre)
        self.seancepasses.setObjectName(u"seancepasses")
        self.seancepasses.setGeometry(QRect(400, 120, 381, 531))
        self.seancepasses.setStyleSheet(u"font: 75 18pt \"Ubuntu\";\n"
"color: rgb(53, 132, 228);")
        self.scrollAreaseancepasses = QScrollArea(self.seancepasses)
        self.scrollAreaseancepasses.setObjectName(u"scrollAreaseancepasses")
        self.scrollAreaseancepasses.setGeometry(QRect(10, 40, 361, 481))
        self.scrollAreaseancepasses.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 359, 479))
        self.scrollAreaseancepasses.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(seanceFenetre)

        QMetaObject.connectSlotsByName(seanceFenetre)
    # setupUi

    def retranslateUi(self, seanceFenetre):
        seanceFenetre.setWindowTitle(QCoreApplication.translate("seanceFenetre", u"Form", None))
        self.retour.setText(QCoreApplication.translate("seanceFenetre", u"Retour", None))
        self.deconnecter.setText(QCoreApplication.translate("seanceFenetre", u"Deconnecter", None))
        self.enregistrer.setText(QCoreApplication.translate("seanceFenetre", u"Enregistrer une seance", None))
        self.plannifier.setText(QCoreApplication.translate("seanceFenetre", u"Plannifier une seance", None))
        self.prochaineseances.setTitle(QCoreApplication.translate("seanceFenetre", u"Les prochaines Seances", None))
        self.seancepasses.setTitle(QCoreApplication.translate("seanceFenetre", u"Les seances pass\u00e9s", None))
    # retranslateUi

