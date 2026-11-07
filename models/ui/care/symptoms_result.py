# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'symptoms_result.ui'
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
        Dialog.resize(400, 450)
        font = QFont()
        font.setFamily(u"Morabba")
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setLayoutDirection(Qt.RightToLeft)
        Dialog.setStyleSheet(u"background-color: #003049; color: #FDF0D5")
        Dialog.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.title_label = QLabel(Dialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(230, 20, 151, 31))
        font1 = QFont()
        font1.setFamily(u"Morabba")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.title_label.setFont(font1)
        self.title_label.setMouseTracking(False)
        self.title_label.setLayoutDirection(Qt.RightToLeft)
        self.title_label.setAutoFillBackground(False)
        self.title_label.setStyleSheet(u"color: #FDF0D5")
        self.title_label.setTextFormat(Qt.PlainText)
        self.title_label.setWordWrap(False)
        self.prompt_label = QLabel(Dialog)
        self.prompt_label.setObjectName(u"prompt_label")
        self.prompt_label.setGeometry(QRect(180, 70, 191, 31))
        font2 = QFont()
        font2.setFamily(u"Morabba")
        font2.setPointSize(12)
        self.prompt_label.setFont(font2)
        self.prompt_label.setLayoutDirection(Qt.RightToLeft)
        self.prompt_label.setStyleSheet(u"color: #FDF0D5")
        self.prompt_text = QTextEdit(Dialog)
        self.prompt_text.setObjectName(u"prompt_text")
        self.prompt_text.setGeometry(QRect(30, 110, 341, 51))
        font3 = QFont()
        font3.setFamily(u"Ray")
        font3.setPointSize(10)
        self.prompt_text.setFont(font3)
        self.prompt_text.setStyleSheet(u"background-color: #FDF0D5; color:#003049; padding: 5px; border-radius: 5px")
        self.prompt_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.prompt_text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.warning_label = QLabel(Dialog)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setGeometry(QRect(60, 320, 279, 21))
        self.warning_label.setFont(font2)
        self.warning_label.setStyleSheet(u"color: #FDF0D5")
        self.warning_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.date_label = QLabel(Dialog)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(60, 360, 279, 21))
        self.date_label.setFont(font2)
        self.date_label.setStyleSheet(u"color: #7F908F")
        self.date_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.back_btn = QPushButton(Dialog)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(120, 400, 161, 31))
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
        self.result_label_2 = QLabel(Dialog)
        self.result_label_2.setObjectName(u"result_label_2")
        self.result_label_2.setGeometry(QRect(220, 170, 151, 31))
        self.result_label_2.setFont(font2)
        self.result_label_2.setLayoutDirection(Qt.RightToLeft)
        self.result_label_2.setStyleSheet(u"color: #FDF0D5")
        self.diagnosis_text = QTextEdit(Dialog)
        self.diagnosis_text.setObjectName(u"diagnosis_text")
        self.diagnosis_text.setGeometry(QRect(30, 210, 341, 91))
        self.diagnosis_text.setFont(font3)
        self.diagnosis_text.setStyleSheet(u"background-color: #FDF0D5; color:#003049; padding: 5px; border-radius: 5px")
        self.diagnosis_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.diagnosis_text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", u"\u0646\u062a\u06cc\u062c\u0647 \u062a\u062d\u0644\u06cc\u0644 \u0639\u0644\u0627\u0626\u0645", None))
        self.prompt_label.setText(QCoreApplication.translate("Dialog", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0627\u0631\u0633\u0627\u0644\u06cc \u0628\u0647 \u0645\u062f\u0644 (\u067e\u0631\u0627\u0645\u067e\u062a):", None))
        self.prompt_text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ray'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.prompt_text.setPlaceholderText(QCoreApplication.translate("Dialog", u"...\u067e\u0631\u0627\u0645\u067e\u062a \u0627\u0631\u0633\u0627\u0644\u06cc \u0628\u0647 \u0645\u062f\u0644", None))
        self.warning_label.setText(QCoreApplication.translate("Dialog", u"\u26a0\ufe0f \u0627\u06cc\u0646 \u0641\u0642\u0637 \u062a\u062e\u0645\u06cc\u0646 \u0627\u0633\u062a\u060c \u0628\u0627 \u067e\u0632\u0634\u06a9 \u0645\u0634\u0648\u0631\u062a \u06a9\u0646\u06cc\u062f!", None))
        self.date_label.setText(QCoreApplication.translate("Dialog", u"\u062a\u0627\u0631\u06cc\u062e \u062b\u0628\u062a: [\u062a\u0627\u0631\u06cc\u062e]", None))
        self.back_btn.setText(QCoreApplication.translate("Dialog", u"\u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0647 \u0644\u06cc\u0633\u062a \u0639\u0644\u0627\u0626\u0645", None))
        self.result_label_2.setText(QCoreApplication.translate("Dialog", u"\u062a\u0634\u062e\u06cc\u0635 \u0648 \u062a\u0648\u0635\u06cc\u0647\u200c\u0647\u0627 \u0627\u0632 AI:", None))
        self.diagnosis_text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ray'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.diagnosis_text.setPlaceholderText(QCoreApplication.translate("Dialog", u"...\u062a\u0634\u062e\u06cc\u0635 \u0648 \u062a\u0648\u0635\u06cc\u0647\u200c\u0647\u0627", None))
    # retranslateUi

