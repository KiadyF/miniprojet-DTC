# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'fenetrelogin.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QWidget)
from . import icontest


class Ui_Fenetrelogin(object):
    def setupUi(self, Fenetrelogin):
        if not Fenetrelogin.objectName():
            Fenetrelogin.setObjectName(u"Fenetrelogin")
        Fenetrelogin.resize(404, 463)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            Fenetrelogin.sizePolicy().hasHeightForWidth())
        Fenetrelogin.setSizePolicy(sizePolicy)
        Fenetrelogin.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.username = QLineEdit(Fenetrelogin)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(100, 210, 201, 25))
        self.username.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border:0px")
        self.username.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit(Fenetrelogin)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 260, 201, 25))
        self.password.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border:0px")
        self.password.setAlignment(Qt.AlignCenter)
        self.login = QPushButton(Fenetrelogin)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(140, 310, 121, 41))
        self.login.setStyleSheet(u"border-radius:10px;\n"
                                 "background-color: rgb(255, 163, 72);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "\n"
                                 "\n"
                                 "")
        self.login.setAutoDefault(False)
        self.login.setFlat(True)
        self.signup = QPushButton(Fenetrelogin)
        self.signup.setObjectName(u"signup")
        self.signup.setGeometry(QRect(140, 370, 121, 41))
        self.signup.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(255, 163, 72);\n"
                                  "border-radius:10px")
        self.signup.setAutoDefault(False)
        self.signup.setFlat(True)
        self.label_2 = QLabel(Fenetrelogin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 10, 161, 121))
        self.label_2.setStyleSheet(u"border-radius:10px;\n"
                                   "background-image: url(:/newPrefix/Bureau/dtc.jpg);\n"
                                   "")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/Bureau/dtc.jpg"))
        self.label_2.setScaledContents(True)
        self.label = QLabel(Fenetrelogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 150, 221, 31))
        self.label.setStyleSheet(u"font: 75 26pt \"Ubuntu\";\n"
                                 "color: rgb(53, 132, 228);")
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Fenetrelogin)

        QMetaObject.connectSlotsByName(Fenetrelogin)
    # setupUi

    def retranslateUi(self, Fenetrelogin):
        Fenetrelogin.setWindowTitle(
            QCoreApplication.translate("Fenetrelogin", u"Form", None))
        self.username.setPlaceholderText(
            QCoreApplication.translate("Fenetrelogin", u"Username", None))
        self.password.setPlaceholderText(
            QCoreApplication.translate("Fenetrelogin", u"Password", None))
        self.login.setText(QCoreApplication.translate(
            "Fenetrelogin", u"L o g i n", None))
        self.signup.setText(QCoreApplication.translate(
            "Fenetrelogin", u"N e w U s e r", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate(
            "Fenetrelogin", u"LOGIN", None))
    # retranslateUi
