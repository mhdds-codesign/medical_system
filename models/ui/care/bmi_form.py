# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bmi_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets,QFont,Qt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        font = QFont()
        font.setFamily(u"Morabba")
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setLayoutDirection(Qt.RightToLeft)
        Dialog.setStyleSheet(u"background-color: #003049; color: #FDF0D5")
        Dialog.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.title_label = QLabel(Dialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(390, 40, 211, 41))
        font1 = QFont()
        font1.setFamily(u"Morabba")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.title_label.setFont(font1)
        self.title_label.setMouseTracking(False)
        self.title_label.setLayoutDirection(Qt.RightToLeft)
        self.title_label.setAutoFillBackground(False)
        self.title_label.setStyleSheet(u"color: #FDF0D5")
        self.title_label.setTextFormat(Qt.PlainText)
        self.title_label.setWordWrap(False)
        self.weight_label = QLabel(Dialog)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setGeometry(QRect(380, 220, 41, 31))
        font2 = QFont()
        font2.setFamily(u"Morabba")
        font2.setPointSize(18)
        self.weight_label.setFont(font2)
        self.weight_label.setLayoutDirection(Qt.RightToLeft)
        self.weight_label.setStyleSheet(u"color: #FDF0D5")
        self.height_label = QLabel(Dialog)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setGeometry(QRect(380, 160, 31, 31))
        self.height_label.setFont(font2)
        self.height_label.setLayoutDirection(Qt.RightToLeft)
        self.height_label.setStyleSheet(u"color: #FDF0D5")
        self.weight_input = QLineEdit(Dialog)
        self.weight_input.setObjectName(u"weight_input")
        self.weight_input.setGeometry(QRect(230, 220, 131, 31))
        font3 = QFont()
        font3.setFamily(u"Ray")
        font3.setPointSize(14)
        self.weight_input.setFont(font3)
        self.weight_input.setLayoutDirection(Qt.RightToLeft)
        self.weight_input.setStyleSheet(u"background-color: #7F908F; border: 1px solid #FDF0D5; padding: 5 px; border-radius: 5px;")
        self.weight_input.setEchoMode(QLineEdit.Normal)
        self.height_input = QLineEdit(Dialog)
        self.height_input.setObjectName(u"height_input")
        self.height_input.setGeometry(QRect(230, 160, 131, 31))
        self.height_input.setFont(font3)
        self.height_input.setLayoutDirection(Qt.RightToLeft)
        self.height_input.setStyleSheet(u"background-color: #7F908F; border: 1px solid #FDF0D5; padding: 5 px; border-radius: 4px;")
        self.calculate_btn = QPushButton(Dialog)
        self.calculate_btn.setObjectName(u"calculate_btn")
        self.calculate_btn.setGeometry(QRect(330, 320, 131, 41))
        self.calculate_btn.setFont(font)
        self.calculate_btn.setLayoutDirection(Qt.RightToLeft)
        self.calculate_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
        self.cancel_btn = QPushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(160, 320, 121, 41))
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", u"\u062b\u0628\u062a BMI", None))
        self.weight_label.setText(QCoreApplication.translate("Dialog", u"\u0648\u0632\u0646:", None))
        self.height_label.setText(QCoreApplication.translate("Dialog", u"\u0642\u062f:", None))
        self.weight_input.setPlaceholderText(QCoreApplication.translate("Dialog", u" \u0648\u0632\u0646 \u0628\u0647 \u06a9\u06cc\u0644\u0648\u06af\u0631\u0645", None))
        self.height_input.setPlaceholderText(QCoreApplication.translate("Dialog", u" \u0642\u062f \u0628\u0647 \u0633\u0627\u0646\u062a\u06cc\u200c\u0645\u062a\u0631", None))
        self.calculate_btn.setText(QCoreApplication.translate("Dialog", u"\u0645\u062d\u0627\u0633\u0628\u0647 \u0648 \u0630\u062e\u06cc\u0631\u0647", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"\u0644\u063a\u0648", None))
    # retranslateUi

