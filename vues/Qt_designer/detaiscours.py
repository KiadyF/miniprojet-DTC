# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'fenetredetailscours.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
                               QProgressBar, QPushButton, QSizePolicy, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gestionetudiant = QPushButton(Form)
        self.gestionetudiant.setObjectName(u"gestionetudiant")
        self.gestionetudiant.setGeometry(QRect(530, 360, 220, 40))
        self.gestionetudiant.setStyleSheet(u"border-radius:10px;\n"
                                           "background-color: rgb(255, 163, 72);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "\n"
                                           "\n"
                                           "")
        self.seances = QPushButton(Form)
        self.seances.setObjectName(u"seances")
        self.seances.setGeometry(QRect(530, 460, 220, 40))
        self.seances.setStyleSheet(u"border-radius:10px;\n"
                                   "background-color: rgb(255, 163, 72);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "\n"
                                   "")
        self.retour = QPushButton(Form)
        self.retour.setObjectName(u"retour")
        self.retour.setGeometry(QRect(20, 20, 89, 25))
        self.retour.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "border:0px;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border-radius:5px\n"
                                  "")
        self.deconnecter = QPushButton(Form)
        self.deconnecter.setObjectName(u"deconnecter")
        self.deconnecter.setGeometry(QRect(680, 20, 89, 25))
        self.deconnecter.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "border:0px;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius:5px")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 60, 301, 31))
        self.label.setStyleSheet(u"font: 75 20pt \"Ubuntu\";\n"
                                 "color: rgb(98, 160, 234);")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(270, 100, 231, 23))
        self.progressBar.setStyleSheet(u"border-radius:5px;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(255, 190, 111);")
        self.progressBar.setValue(24)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 180, 81, 21))
        self.label_2.setStyleSheet(u"font: 75 20pt \"Ubuntu\";\n"
                                   "color: rgb(98, 160, 234);")
        self.plan = QListWidget(Form)
        self.plan.setObjectName(u"plan")
        self.plan.setGeometry(QRect(70, 210, 351, 391))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.plan.sizePolicy().hasHeightForWidth())
        self.plan.setSizePolicy(sizePolicy1)
        self.plan.setStyleSheet(u"border-radius: 20px;\n"
                                "border:0px;\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 193, 241, 255), stop:1 rgba(255, 255, 255, 255));")
        self.gestionabsence = QPushButton(Form)
        self.gestionabsence.setObjectName(u"gestionabsence")
        self.gestionabsence.setGeometry(QRect(530, 410, 220, 40))
        self.gestionabsence.setStyleSheet(u"border-radius:10px;\n"
                                          "background-color: rgb(255, 163, 72);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "\n"
                                          "\n"
                                          "")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gestionetudiant.setText(QCoreApplication.translate(
            "Form", u"GESTION DES ETUDIANTS", None))
        self.seances.setText(
            QCoreApplication.translate("Form", u"SEANCES", None))
        self.retour.setText(
            QCoreApplication.translate("Form", u"Retour", None))
        self.deconnecter.setText(
            QCoreApplication.translate("Form", u"Deconnecter", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"Progression du cours", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"PLAN", None))
        self.gestionabsence.setText(QCoreApplication.translate(
            "Form", u"GESTION DES ABSENCES", None))
    # retranslateUi
