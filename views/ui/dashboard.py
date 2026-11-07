# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
        self.title_label.setGeometry(QRect(430, 40, 171, 41))
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
        self.welcome_label = QLabel(Form)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(90, 100, 461, 31))
        font2 = QFont()
        font2.setFamily(u"Morabba")
        font2.setPointSize(18)
        self.welcome_label.setFont(font2)
        self.welcome_label.setLayoutDirection(Qt.RightToLeft)
        self.welcome_label.setStyleSheet(u"color: #FDF0D5")
        self.welcome_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(230, 160, 180, 261))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.profile_btn = QPushButton(self.layoutWidget)
        self.profile_btn.setObjectName(u"profile_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_btn.sizePolicy().hasHeightForWidth())
        self.profile_btn.setSizePolicy(sizePolicy)
        self.profile_btn.setFont(font)
        self.profile_btn.setLayoutDirection(Qt.RightToLeft)
        self.profile_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.verticalLayout.addWidget(self.profile_btn)

        self.symptoms_btn = QPushButton(self.layoutWidget)
        self.symptoms_btn.setObjectName(u"symptoms_btn")
        sizePolicy.setHeightForWidth(self.symptoms_btn.sizePolicy().hasHeightForWidth())
        self.symptoms_btn.setSizePolicy(sizePolicy)
        self.symptoms_btn.setFont(font)
        self.symptoms_btn.setLayoutDirection(Qt.RightToLeft)
        self.symptoms_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.verticalLayout.addWidget(self.symptoms_btn)

        self.medicines_btn = QPushButton(self.layoutWidget)
        self.medicines_btn.setObjectName(u"medicines_btn")
        sizePolicy.setHeightForWidth(self.medicines_btn.sizePolicy().hasHeightForWidth())
        self.medicines_btn.setSizePolicy(sizePolicy)
        self.medicines_btn.setFont(font)
        self.medicines_btn.setLayoutDirection(Qt.RightToLeft)
        self.medicines_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.verticalLayout.addWidget(self.medicines_btn)

        self.logout_btn = QPushButton(self.layoutWidget)
        self.logout_btn.setObjectName(u"logout_btn")
        sizePolicy.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy)
        self.logout_btn.setFont(font)
        self.logout_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")

        self.verticalLayout.addWidget(self.logout_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"\u062f\u0627\u0634\u0628\u0648\u0631\u062f \u06a9\u0627\u0631\u0628\u0631", None))
        self.welcome_label.setText(QCoreApplication.translate("Form", u"\u062e\u0648\u0634 \u0622\u0645\u062f\u06cc\u062f!", None))
        self.profile_btn.setText(QCoreApplication.translate("Form", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0627\u0631\u0628\u0631", None))
        self.symptoms_btn.setText(QCoreApplication.translate("Form", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u0633\u0644\u0627\u0645\u062a", None))
        self.medicines_btn.setText(QCoreApplication.translate("Form", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u062f\u0627\u0631\u0648\u0647\u0627", None))
        self.logout_btn.setText(QCoreApplication.translate("Form", u"\u062e\u0631\u0648\u062c", None))
    # retranslateUi

