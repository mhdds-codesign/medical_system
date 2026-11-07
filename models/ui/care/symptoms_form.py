# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'symptoms_form.ui'
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
        self.save_btn = QPushButton(Dialog)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(340, 390, 131, 41))
        self.save_btn.setFont(font)
        self.save_btn.setLayoutDirection(Qt.RightToLeft)
        self.save_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
        self.status_label = QLabel(Dialog)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(50, 100, 551, 31))
        font2 = QFont()
        font2.setFamily(u"Morabba")
        font2.setPointSize(10)
        self.status_label.setFont(font2)
        self.status_label.setLayoutDirection(Qt.RightToLeft)
        self.status_label.setStyleSheet(u"color: #FDF0D5")
        self.cancel_btn = QPushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(170, 390, 121, 41))
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
        self.symptoms_input = QTextEdit(Dialog)
        self.symptoms_input.setObjectName(u"symptoms_input")
        self.symptoms_input.setGeometry(QRect(50, 270, 551, 91))
        font3 = QFont()
        font3.setFamily(u"Ray")
        font3.setPointSize(12)
        self.symptoms_input.setFont(font3)
        self.symptoms_input.setStyleSheet(u"background-color: #FDF0D5; color:#003049; padding: 5px; border-radius: 5px")
        self.symptoms_label = QLabel(Dialog)
        self.symptoms_label.setObjectName(u"symptoms_label")
        self.symptoms_label.setGeometry(QRect(50, 230, 551, 31))
        font4 = QFont()
        font4.setFamily(u"Morabba")
        font4.setPointSize(12)
        self.symptoms_label.setFont(font4)
        self.symptoms_label.setLayoutDirection(Qt.RightToLeft)
        self.symptoms_label.setStyleSheet(u"color: #FDF0D5")
        self.status_input = QTextEdit(Dialog)
        self.status_input.setObjectName(u"status_input")
        self.status_input.setGeometry(QRect(50, 140, 551, 71))
        self.status_input.setFont(font3)
        self.status_input.setStyleSheet(u"background-color: #FDF0D5; color:#003049; padding: 5px; border-radius: 5px")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", u"\u062b\u0628\u062a \u0639\u0644\u0627\u0626\u0645", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u" \u0630\u062e\u06cc\u0631\u0647", None))
        self.status_label.setText(QCoreApplication.translate("Dialog", u"\u0686\u0646\u0627\u0646\u0686\u0647 \u062f\u0686\u0627\u0631 \u0628\u06cc\u0645\u0627\u0631\u06cc \u0632\u0645\u06cc\u0646\u0647 \u0627\u06cc \u0647\u0633\u062a\u06cc\u062f \u06cc\u0627 \u062f\u0627\u0631\u0648\u06cc\u06cc \u0645\u0635\u0631\u0641 \u0645\u06cc\u06a9\u0646\u06cc\u062f \u0648 \u062d\u062a\u06cc \u062f\u0631 24 \u0633\u0627\u0639\u062a \u06af\u0630\u0634\u062a\u0647 \u062f\u0627\u0631\u0648\u06cc \u0645\u0635\u0631\u0641 \u06a9\u0631\u062f\u0647 \u0627\u06cc\u062f \u0630\u06a9\u0631 \u06a9\u0646\u06cc\u062f:", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"\u0644\u063a\u0648", None))
        self.symptoms_input.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ray'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.symptoms_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0645\u062b\u0627\u0644: \u0633\u0631\u062f\u0631\u062f \u0628\u0627 \u0634\u062f\u062a 5, \u062a\u0628, \u062d\u0627\u0644\u062a \u062a\u0647\u0648\u0639", None))
        self.symptoms_label.setText(QCoreApplication.translate("Dialog", u"\u0639\u0644\u0627\u0626\u0645 (\u0628\u0627 \u0648\u06cc\u0631\u06af\u0648\u0644 \u062c\u062f\u0627 \u06a9\u0646\u06cc\u062f \u0648 \u0634\u062f\u062a \u062f\u0631\u062f \u0647\u0627\u0631\u0627 \u0627\u0632 10 \u0630\u06a9\u0631 \u06a9\u0646\u06cc\u062f):", None))
        self.status_input.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ray'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.status_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0645\u062b\u0627\u0644: \u0642\u0646\u062f \u062f\u0627\u0631\u0645\u060c \u0627\u0633\u062a\u0627\u0645\u06cc\u0646\u0648\u0641\u0646 \u0645\u0635\u0631\u0641 \u06a9\u0631\u062f\u0645", None))
    # retranslateUi

