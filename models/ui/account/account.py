# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
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
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(200, 130, 241, 291))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.personal_btn = QPushButton(self.layoutWidget)
        self.personal_btn.setObjectName(u"personal_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personal_btn.sizePolicy().hasHeightForWidth())
        self.personal_btn.setSizePolicy(sizePolicy)
        self.personal_btn.setFont(font)
        self.personal_btn.setLayoutDirection(Qt.RightToLeft)
        self.personal_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.verticalLayout.addWidget(self.personal_btn)

        self.account_btn = QPushButton(self.layoutWidget)
        self.account_btn.setObjectName(u"account_btn")
        sizePolicy.setHeightForWidth(self.account_btn.sizePolicy().hasHeightForWidth())
        self.account_btn.setSizePolicy(sizePolicy)
        self.account_btn.setFont(font)
        self.account_btn.setLayoutDirection(Qt.RightToLeft)
        self.account_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.verticalLayout.addWidget(self.account_btn)

        self.delete_btn = QPushButton(self.layoutWidget)
        self.delete_btn.setObjectName(u"delete_btn")
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        self.delete_btn.setFont(font)
        self.delete_btn.setLayoutDirection(Qt.RightToLeft)
        self.delete_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.verticalLayout.addWidget(self.delete_btn)

        self.back_btn = QPushButton(self.layoutWidget)
        self.back_btn.setObjectName(u"back_btn")
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")

        self.verticalLayout.addWidget(self.back_btn)

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
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.title_label.setWordWrap(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.personal_btn.setText(QCoreApplication.translate("Form", u"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0634\u062e\u0635\u06cc", None))
        self.account_btn.setText(QCoreApplication.translate("Form", u"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"\u062d\u0630\u0641 \u062d\u0633\u0627\u0628 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.back_btn.setText(QCoreApplication.translate("Form", u"\u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0647 \u062f\u0627\u0634\u0628\u0648\u0631\u062f", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u067e\u0631\u0648\u0641\u0627\u06cc\u0644", None))
    # retranslateUi

