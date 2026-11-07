# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'medicines.ui'
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
        Form.setStyleSheet(u"background-color: #003049; color: #fdf0d5;")
        Form.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(440, 20, 161, 41))
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
        self.search_label = QLabel(Form)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setGeometry(QRect(500, 90, 101, 31))
        self.search_label.setFont(font)
        self.search_label.setLayoutDirection(Qt.RightToLeft)
        self.search_label.setStyleSheet(u"color: #FDF0D5")
        self.search_label.setAlignment(Qt.AlignCenter)
        self.search_input = QLineEdit(Form)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setGeometry(QRect(340, 90, 151, 31))
        font2 = QFont()
        font2.setFamily(u"Ray")
        font2.setPointSize(12)
        self.search_input.setFont(font2)
        self.search_input.setLayoutDirection(Qt.RightToLeft)
        self.search_input.setStyleSheet(u"background-color: #7F908F; border: 1px solid #FDF0D5; padding: 5 px; border-radius: 5px;")
        self.search_btn = QPushButton(Form)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(270, 90, 61, 31))
        font3 = QFont()
        font3.setFamily(u"Morabba")
        font3.setPointSize(8)
        self.search_btn.setFont(font3)
        self.search_btn.setLayoutDirection(Qt.RightToLeft)
        self.search_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
        self.clear_btn = QPushButton(Form)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(210, 90, 51, 31))
        self.clear_btn.setFont(font3)
        self.clear_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
        self.medicine_table = QTableWidget(Form)
        if (self.medicine_table.columnCount() < 3):
            self.medicine_table.setColumnCount(3)
        brush = QBrush(QColor(0, 48, 73, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.medicine_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush1 = QBrush(QColor(0, 48, 73, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem1.setForeground(brush1);
        self.medicine_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        brush2 = QBrush(QColor(0, 48, 73, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font);
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem2.setForeground(brush2);
        self.medicine_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.medicine_table.setObjectName(u"medicine_table")
        self.medicine_table.setGeometry(QRect(30, 140, 571, 251))
        palette = QPalette()
        brush3 = QBrush(QColor(0, 48, 73, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(253, 240, 213, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush5 = QBrush(QColor(0, 48, 73, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        brush6 = QBrush(QColor(0, 48, 73, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        brush7 = QBrush(QColor(0, 48, 73, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.medicine_table.setPalette(palette)
        self.medicine_table.setFont(font2)
        self.medicine_table.setAutoFillBackground(False)
        self.medicine_table.setStyleSheet(u"border-radius: 5px; background-color: #FDF0D5; color:#003049;")
        self.medicine_table.setFrameShape(QFrame.NoFrame)
        self.medicine_table.setFrameShadow(QFrame.Sunken)
        self.medicine_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.medicine_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.medicine_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.medicine_table.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.medicine_table.setAlternatingRowColors(False)
        self.medicine_table.setShowGrid(True)
        self.medicine_table.setGridStyle(Qt.DashLine)
        self.medicine_table.setColumnCount(3)
        self.medicine_table.horizontalHeader().setVisible(True)
        self.medicine_table.horizontalHeader().setCascadingSectionResizes(False)
        self.medicine_table.horizontalHeader().setDefaultSectionSize(150)
        self.medicine_table.horizontalHeader().setHighlightSections(True)
        self.medicine_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.medicine_table.horizontalHeader().setStretchLastSection(True)
        self.medicine_table.verticalHeader().setVisible(True)
        self.medicine_table.verticalHeader().setMinimumSectionSize(40)
        self.medicine_table.verticalHeader().setDefaultSectionSize(45)
        self.medicine_table.verticalHeader().setStretchLastSection(False)
        self.back_btn = QPushButton(Form)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(140, 410, 161, 41))
        self.back_btn.setFont(font)
        self.back_btn.setLayoutDirection(Qt.RightToLeft)
        self.back_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(340, 410, 131, 41))
        self.add_btn.setFont(font)
        self.add_btn.setLayoutDirection(Qt.RightToLeft)
        self.add_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"\u0644\u06cc\u0633\u062a \u062f\u0627\u0631\u0648\u0647\u0627", None))
        self.search_label.setText(QCoreApplication.translate("Form", u"\u062c\u0633\u062a\u062c\u0648\u06cc \u062f\u0627\u0631\u0648:", None))
        self.search_input.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("Form", u"\u0646\u0627\u0645 \u062f\u0627\u0631\u0648 \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f...", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"\u062c\u0633\u062a \u0648 \u062c\u0648 ", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"\u067e\u0627\u06a9 \u06a9\u0631\u062f\u0646", None))
        ___qtablewidgetitem = self.medicine_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u0634\u0646\u0627\u0633\u0647", None));
        ___qtablewidgetitem1 = self.medicine_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0646\u0627\u0645 \u062f\u0627\u0631\u0648", None));
        ___qtablewidgetitem2 = self.medicine_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0639\u0645\u0644\u06cc\u0627\u062a", None));
        self.back_btn.setText(QCoreApplication.translate("Form", u"\u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0647 \u062f\u0627\u0634\u0628\u0648\u0631\u062f", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"\u0627\u0636\u0627\u0641\u0647 \u06a9\u0631\u062f\u0646 \u062f\u0627\u0631\u0648", None))
    # retranslateUi

