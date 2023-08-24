# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'fenetrenewuser.ui'
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


class Ui_UserinscriptionFenetre(object):
    def setupUi(self, UserinscriptionFenetre):
        if not UserinscriptionFenetre.objectName():
            UserinscriptionFenetre.setObjectName(u"UserinscriptionFenetre")
        UserinscriptionFenetre.resize(400, 463)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            UserinscriptionFenetre.sizePolicy().hasHeightForWidth())
        UserinscriptionFenetre.setSizePolicy(sizePolicy)
        self.label_2 = QLabel(UserinscriptionFenetre)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 10, 161, 121))
        self.label_2.setStyleSheet(u"border-radius:10px;\n"
                                   "background-image: url(:/newPrefix/Bureau/dtc.jpg);\n"
                                   "")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/Bureau/dtc.jpg"))
        self.label_2.setScaledContents(True)
        self.nom = QLineEdit(UserinscriptionFenetre)
        self.nom.setObjectName(u"nom")
        self.nom.setGeometry(QRect(60, 220, 271, 25))
        self.nom.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
                               "color: rgb(255, 255, 255);\n"
                               "border:0px")
        self.nom.setAlignment(Qt.AlignCenter)
        self.mdp = QLineEdit(UserinscriptionFenetre)
        self.mdp.setObjectName(u"mdp")
        self.mdp.setGeometry(QRect(60, 260, 271, 25))
        self.mdp.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
                               "color: rgb(255, 255, 255);\n"
                               "border:0px")
        self.mdp.setAlignment(Qt.AlignCenter)
        self.confirm_mdp = QLineEdit(UserinscriptionFenetre)
        self.confirm_mdp.setObjectName(u"confirm_mdp")
        self.confirm_mdp.setGeometry(QRect(60, 300, 271, 25))
        self.confirm_mdp.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border:0px")
        self.confirm_mdp.setAlignment(Qt.AlignCenter)
        self.cancel = QPushButton(UserinscriptionFenetre)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(10, 360, 121, 41))
        self.cancel.setStyleSheet(u"border-radius:10px;\n"
                                  "background-color: rgb(255, 163, 72);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "\n"
                                  "\n"
                                  "")
        self.cancel.setAutoDefault(False)
        self.cancel.setFlat(True)
        self.submit = QPushButton(UserinscriptionFenetre)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(260, 360, 121, 41))
        self.submit.setStyleSheet(u"border-radius:10px;\n"
                                  "background-color: rgb(255, 163, 72);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "\n"
                                  "\n"
                                  "")
        self.submit.setAutoDefault(False)
        self.submit.setFlat(True)
        self.label = QLabel(UserinscriptionFenetre)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 160, 301, 31))
        self.label.setStyleSheet(u"font: 75 26pt \"Ubuntu\";\n"
                                 "color: rgb(53, 132, 228);")
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(UserinscriptionFenetre)

        QMetaObject.connectSlotsByName(UserinscriptionFenetre)
    # setupUi

    def retranslateUi(self, UserinscriptionFenetre):
        UserinscriptionFenetre.setWindowTitle(
            QCoreApplication.translate("UserinscriptionFenetre", u"Form", None))
        self.label_2.setText("")
        self.nom.setText("")
        self.nom.setPlaceholderText(QCoreApplication.translate(
            "UserinscriptionFenetre", u"Username", None))
        self.mdp.setPlaceholderText(QCoreApplication.translate(
            "UserinscriptionFenetre", u"Your password", None))
        self.confirm_mdp.setPlaceholderText(QCoreApplication.translate(
            "UserinscriptionFenetre", u"Confirm your password", None))
        self.cancel.setText(QCoreApplication.translate(
            "UserinscriptionFenetre", u"Cancel", None))
        self.submit.setText(QCoreApplication.translate(
            "UserinscriptionFenetre", u"Submit", None))
        self.label.setText(QCoreApplication.translate(
            "UserinscriptionFenetre", u"CREATE ACCOUNT", None))
    # retranslateUi
