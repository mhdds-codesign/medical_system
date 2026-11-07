# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        font = QFont()
        font.setFamily(u"Morabba")
        font.setPointSize(14)
        Form.setFont(font)
        Form.setLayoutDirection(Qt.RightToLeft)
        Form.setStyleSheet(u"background-color: #003049; color: #FDF0D5")
        Form.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(420, 40, 181, 41))
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
        self.password_input = QLineEdit(Form)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(200, 220, 131, 31))
        font2 = QFont()
        font2.setFamily(u"Ray")
        font2.setPointSize(14)
        self.password_input.setFont(font2)
        self.password_input.setLayoutDirection(Qt.RightToLeft)
        self.password_input.setStyleSheet(u"background-color: #7F908F; border: 1px solid #FDF0D5; padding: 5 px; border-radius: 5px;")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password = QLabel(Form)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(350, 220, 71, 31))
        font3 = QFont()
        font3.setFamily(u"Morabba")
        font3.setPointSize(18)
        self.password.setFont(font3)
        self.password.setLayoutDirection(Qt.RightToLeft)
        self.password.setStyleSheet(u"color: #FDF0D5")
        self.username = QLabel(Form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(350, 160, 101, 31))
        self.username.setFont(font3)
        self.username.setLayoutDirection(Qt.RightToLeft)
        self.username.setStyleSheet(u"color: #FDF0D5")
        self.username_input = QLineEdit(Form)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(200, 160, 131, 31))
        self.username_input.setFont(font2)
        self.username_input.setLayoutDirection(Qt.RightToLeft)
        self.username_input.setStyleSheet(u"background-color: #7F908F; border: 1px solid #FDF0D5; padding: 5 px; border-radius: 5px;")
        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(170, 320, 121, 41))
        self.login_btn.setFont(font)
        self.login_btn.setLayoutDirection(Qt.RightToLeft)
        self.login_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
        self.signup_btn = QPushButton(Form)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setGeometry(QRect(340, 320, 121, 41))
        self.signup_btn.setFont(font)
        self.signup_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"\u0648\u0631\u0648\u062f \u0628\u0647 \u0633\u06cc\u0633\u062a\u0645", None))
        self.password.setText(QCoreApplication.translate("Form", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631:", None))
        self.username.setText(QCoreApplication.translate("Form", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc:", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\u0648\u0631\u0648\u062f", None))
        self.signup_btn.setText(QCoreApplication.translate("Form", u"\u062b\u0628\u062a\u200c\u0646\u0627\u0645", None))
    # retranslateUi

