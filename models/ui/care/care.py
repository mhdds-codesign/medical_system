# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'care.ui'
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
        self.title_label.setGeometry(QRect(360, 40, 241, 41))
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
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(200, 120, 241, 291))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bmi_btn = QPushButton(self.layoutWidget)
        self.bmi_btn.setObjectName(u"bmi_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bmi_btn.sizePolicy().hasHeightForWidth())
        self.bmi_btn.setSizePolicy(sizePolicy)
        self.bmi_btn.setFont(font)
        self.bmi_btn.setLayoutDirection(Qt.RightToLeft)
        self.bmi_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.verticalLayout.addWidget(self.bmi_btn)

        self.symptoms_btn = QPushButton(self.layoutWidget)
        self.symptoms_btn.setObjectName(u"symptoms_btn")
        sizePolicy.setHeightForWidth(self.symptoms_btn.sizePolicy().hasHeightForWidth())
        self.symptoms_btn.setSizePolicy(sizePolicy)
        self.symptoms_btn.setFont(font)
        self.symptoms_btn.setLayoutDirection(Qt.RightToLeft)
        self.symptoms_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.verticalLayout.addWidget(self.symptoms_btn)

        self.back_btn = QPushButton(self.layoutWidget)
        self.back_btn.setObjectName(u"back_btn")
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")

        self.verticalLayout.addWidget(self.back_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u0633\u0644\u0627\u0645\u062a \u0628\u06cc\u0645\u0627\u0631", None))
        self.bmi_btn.setText(QCoreApplication.translate("Form", u"BMI\u0645\u062f\u06cc\u0631\u06cc\u062a ", None))
        self.symptoms_btn.setText(QCoreApplication.translate("Form", u"\u062b\u0628\u062a \u0639\u0644\u0627\u0626\u0645 \u0628\u06cc\u0645\u0627\u0631", None))
        self.back_btn.setText(QCoreApplication.translate("Form", u"\u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0647 \u062f\u0627\u0634\u0628\u0648\u0631\u062f", None))
    # retranslateUi

