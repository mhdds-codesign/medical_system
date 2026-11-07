# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'symptoms.ui'
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
        self.search_label = QLabel(Form)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setGeometry(QRect(490, 90, 111, 31))
        self.search_label.setFont(font)
        self.search_label.setLayoutDirection(Qt.RightToLeft)
        self.search_label.setStyleSheet(u"color: #FDF0D5")
        self.search_label.setAlignment(Qt.AlignCenter)
        self.search_date = QDateEdit(Form)
        self.search_date.setObjectName(u"search_date")
        self.search_date.setGeometry(QRect(330, 90, 151, 31))
        font1 = QFont()
        font1.setFamily(u"Ray")
        font1.setPointSize(12)
        self.search_date.setFont(font1)
        self.search_date.setLayoutDirection(Qt.RightToLeft)
        self.search_date.setStyleSheet(u"background-color: #7F908F; border: 1px solid #FDF0D5; padding: 5 px; border-radius: 5px;")
        self.search_date.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.search_date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search_date.setCalendarPopup(True)
        self.search_btn = QPushButton(Form)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(260, 90, 61, 31))
        font2 = QFont()
        font2.setFamily(u"Morabba")
        font2.setPointSize(8)
        self.search_btn.setFont(font2)
        self.search_btn.setLayoutDirection(Qt.RightToLeft)
        self.search_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(370, 410, 131, 41))
        self.add_btn.setFont(font)
        self.add_btn.setLayoutDirection(Qt.RightToLeft)
        self.add_btn.setStyleSheet(u"QPushButton {background-color: #FDF0D5; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
        self.symptoms_table = QTableWidget(Form)
        if (self.symptoms_table.columnCount() < 3):
            self.symptoms_table.setColumnCount(3)
        brush = QBrush(QColor(0, 48, 73, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.symptoms_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush1 = QBrush(QColor(0, 48, 73, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setForeground(brush1);
        self.symptoms_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        brush2 = QBrush(QColor(0, 48, 73, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font);
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem2.setForeground(brush2);
        self.symptoms_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.symptoms_table.setObjectName(u"symptoms_table")
        self.symptoms_table.setGeometry(QRect(30, 140, 571, 251))
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
        self.symptoms_table.setPalette(palette)
        self.symptoms_table.setFont(font1)
        self.symptoms_table.setAutoFillBackground(False)
        self.symptoms_table.setStyleSheet(u"border-radius: 5px; background-color: #FDF0D5; color:#003049;")
        self.symptoms_table.setFrameShape(QFrame.NoFrame)
        self.symptoms_table.setFrameShadow(QFrame.Sunken)
        self.symptoms_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.symptoms_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.symptoms_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.symptoms_table.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.symptoms_table.setAlternatingRowColors(False)
        self.symptoms_table.setShowGrid(True)
        self.symptoms_table.setGridStyle(Qt.DashLine)
        self.symptoms_table.setColumnCount(3)
        self.symptoms_table.horizontalHeader().setVisible(True)
        self.symptoms_table.horizontalHeader().setCascadingSectionResizes(False)
        self.symptoms_table.horizontalHeader().setDefaultSectionSize(150)
        self.symptoms_table.horizontalHeader().setHighlightSections(True)
        self.symptoms_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.symptoms_table.horizontalHeader().setStretchLastSection(True)
        self.symptoms_table.verticalHeader().setVisible(True)
        self.symptoms_table.verticalHeader().setMinimumSectionSize(40)
        self.symptoms_table.verticalHeader().setDefaultSectionSize(45)
        self.symptoms_table.verticalHeader().setStretchLastSection(False)
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(440, 20, 161, 41))
        font3 = QFont()
        font3.setFamily(u"Morabba")
        font3.setPointSize(22)
        font3.setBold(True)
        font3.setWeight(75)
        self.title_label.setFont(font3)
        self.title_label.setMouseTracking(False)
        self.title_label.setLayoutDirection(Qt.RightToLeft)
        self.title_label.setAutoFillBackground(False)
        self.title_label.setStyleSheet(u"color: #FDF0D5")
        self.title_label.setTextFormat(Qt.PlainText)
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.title_label.setWordWrap(False)
        self.clear_btn = QPushButton(Form)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(200, 90, 51, 31))
        self.clear_btn.setFont(font2)
        self.clear_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
        self.back_btn = QPushButton(Form)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(120, 410, 211, 41))
        self.back_btn.setFont(font)
        self.back_btn.setLayoutDirection(Qt.RightToLeft)
        self.back_btn.setStyleSheet(u"QPushButton {background-color: #EEB9A8; color: #003049; border: none; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
        self.back_btn.setFlat(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_label.setText(QCoreApplication.translate("Form", u"\u062c\u0633\u062a\u062c\u0648\u06cc \u0639\u0644\u0627\u0626\u0645:", None))
        self.search_date.setDisplayFormat(QCoreApplication.translate("Form", u"dd-MM-yyyy", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"\u062c\u0633\u062a \u0648 \u062c\u0648 ", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"\u062b\u0628\u062a \u0639\u0644\u0627\u0626\u0645  \u062c\u062f\u06cc\u062f", None))
        ___qtablewidgetitem = self.symptoms_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u0634\u0646\u0627\u0633\u0647", None));
        ___qtablewidgetitem1 = self.symptoms_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u062a\u0627\u0631\u06cc\u062e \u062b\u0628\u062a", None));
        ___qtablewidgetitem2 = self.symptoms_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0639\u0645\u0644\u06cc\u0627\u062a", None));
        self.title_label.setText(QCoreApplication.translate("Form", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u0639\u0644\u0627\u0626\u0645", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"\u067e\u0627\u06a9 \u06a9\u0631\u062f\u0646", None))
        self.back_btn.setText(QCoreApplication.translate("Form", u"\u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0647 \u0645\u062f\u06cc\u0631\u06cc\u062a \u0633\u0644\u0627\u0645\u062a", None))
    # retranslateUi

