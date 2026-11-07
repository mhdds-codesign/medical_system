# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bmi_result.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        font = QFont()
        font.setFamily(u"Morabba")
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setLayoutDirection(Qt.RightToLeft)
        Dialog.setStyleSheet(u"background-color: #003049; color: #FDF0D5")
        Dialog.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.title_label = QLabel(Dialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(210, 20, 161, 36))
        font1 = QFont()
        font1.setFamily(u"Morabba")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: #FDF0D5")
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.back_btn = QPushButton(Dialog)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(120, 240, 161, 31))
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 80, 281, 141))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.result_label = QLabel(self.layoutWidget)
        self.result_label.setObjectName(u"result_label")
        font2 = QFont()
        font2.setFamily(u"Morabba")
        font2.setPointSize(12)
        self.result_label.setFont(font2)
        self.result_label.setStyleSheet(u"color: #FDF0D5")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result_label)

        self.date_label = QLabel(self.layoutWidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setFont(font2)
        self.date_label.setStyleSheet(u"color: #7F908F")
        self.date_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.date_label)

        self.status_label = QLabel(self.layoutWidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font2)
        self.status_label.setStyleSheet(u"color: #FDF0D5")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status_label)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", u"\u0646\u062a\u06cc\u062c\u0647 \u0645\u062d\u0627\u0633\u0628\u0647 BMI", None))
        self.back_btn.setText(QCoreApplication.translate("Dialog", u" BMI \u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0647 \u0644\u06cc\u0633\u062a", None))
        self.result_label.setText(QCoreApplication.translate("Dialog", u" \u0634\u0645\u0627 BMI: [\u0645\u0642\u062f\u0627\u0631] ", None))
        self.date_label.setText(QCoreApplication.translate("Dialog", u"\u062a\u0627\u0631\u06cc\u062e \u062b\u0628\u062a: [\u062a\u0627\u0631\u06cc\u062e]", None))
        self.status_label.setText(QCoreApplication.translate("Dialog", u"\u0648\u0636\u0639\u06cc\u062a: [\u0648\u0636\u0639\u06cc\u062a]", None))
    # retranslateUi

