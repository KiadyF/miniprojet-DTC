# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetreprochaineseance.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QTimeEdit,
    QWidget)

class Ui_prochaineseancesFenetre(object):
    def setupUi(self, prochaineseancesFenetre):
        if not prochaineseancesFenetre.objectName():
            prochaineseancesFenetre.setObjectName(u"prochaineseancesFenetre")
        prochaineseancesFenetre.resize(500, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(prochaineseancesFenetre.sizePolicy().hasHeightForWidth())
        prochaineseancesFenetre.setSizePolicy(sizePolicy)
        self.sujet = QLineEdit(prochaineseancesFenetre)
        self.sujet.setObjectName(u"sujet")
        self.sujet.setGeometry(QRect(70, 160, 401, 25))
        self.sujet.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.sujet.setAlignment(Qt.AlignCenter)
        self.cancel = QPushButton(prochaineseancesFenetre)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(40, 400, 121, 40))
        self.cancel.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.submit = QPushButton(prochaineseancesFenetre)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(350, 400, 121, 40))
        self.submit.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 163, 72);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.details = QTextEdit(prochaineseancesFenetre)
        self.details.setObjectName(u"details")
        self.details.setGeometry(QRect(70, 210, 401, 151))
        self.details.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 160, 234, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.label = QLabel(prochaineseancesFenetre)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 291, 31))
        self.label.setStyleSheet(u"font: 75 26pt \"Ubuntu\";\n"
"color: rgb(53, 132, 228);")
        self.label_2 = QLabel(prochaineseancesFenetre)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 67, 17))
        self.label_2.setStyleSheet(u"color: rgb(53, 132, 228);\n"
"font: 75 16pt \"Ubuntu\";")
        self.duree = QTimeEdit(prochaineseancesFenetre)
        self.duree.setObjectName(u"duree")
        self.duree.setGeometry(QRect(360, 100, 118, 26))
        self.label_3 = QLabel(prochaineseancesFenetre)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 100, 67, 17))
        self.label_3.setStyleSheet(u"color: rgb(53, 132, 228);\n"
"font: 75 16pt \"Ubuntu\";")
        self.date = QDateTimeEdit(prochaineseancesFenetre)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(70, 100, 194, 26))

        self.retranslateUi(prochaineseancesFenetre)

        QMetaObject.connectSlotsByName(prochaineseancesFenetre)
    # setupUi

    def retranslateUi(self, prochaineseancesFenetre):
        prochaineseancesFenetre.setWindowTitle(QCoreApplication.translate("prochaineseancesFenetre", u"Form", None))
        self.sujet.setPlaceholderText(QCoreApplication.translate("prochaineseancesFenetre", u"Sujet", None))
        self.cancel.setText(QCoreApplication.translate("prochaineseancesFenetre", u"Cancel", None))
        self.submit.setText(QCoreApplication.translate("prochaineseancesFenetre", u"Submit", None))
        self.details.setPlaceholderText(QCoreApplication.translate("prochaineseancesFenetre", u"Details:", None))
        self.label.setText(QCoreApplication.translate("prochaineseancesFenetre", u"Prochaine seances", None))
        self.label_2.setText(QCoreApplication.translate("prochaineseancesFenetre", u"Date", None))
        self.label_3.setText(QCoreApplication.translate("prochaineseancesFenetre", u"Duree", None))
    # retranslateUi

