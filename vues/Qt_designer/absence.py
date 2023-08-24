# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetrerecapabsent.ui'
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

class Ui_recapabsentFenetre(object):
    def setupUi(self, recapabsentFenetre):
        if not recapabsentFenetre.objectName():
            recapabsentFenetre.setObjectName(u"recapabsentFenetre")
        recapabsentFenetre.resize(800, 800)
        self.label = QLabel(recapabsentFenetre)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 551, 31))
        self.label.setStyleSheet(u"font: 75 26pt \"Ubuntu\";\n"
"color: rgb(53, 132, 228);")
        self.label.setAlignment(Qt.AlignCenter)
        self.recapAbsents = QScrollArea(recapabsentFenetre)
        self.recapAbsents.setObjectName(u"recapAbsents")
        self.recapAbsents.setGeometry(QRect(80, 70, 651, 641))
        self.recapAbsents.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 649, 639))
        self.recapAbsents.setWidget(self.scrollAreaWidgetContents)
        self.revenir = QPushButton(recapabsentFenetre)
        self.revenir.setObjectName(u"revenir")
        self.revenir.setGeometry(QRect(320, 730, 121, 41))
        self.revenir.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 163, 72);\n"
"border-radius:10px")
        self.revenir.setAutoDefault(False)
        self.revenir.setFlat(True)

        self.retranslateUi(recapabsentFenetre)

        QMetaObject.connectSlotsByName(recapabsentFenetre)
    # setupUi

    def retranslateUi(self, recapabsentFenetre):
        recapabsentFenetre.setWindowTitle(QCoreApplication.translate("recapabsentFenetre", u"Form", None))
        self.label.setText(QCoreApplication.translate("recapabsentFenetre", u"RECAPITULATION DES ABSENCES", None))
        self.revenir.setText(QCoreApplication.translate("recapabsentFenetre", u"Revenir", None))
    # retranslateUi

