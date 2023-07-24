# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(825, 546)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ciphertext = QTextEdit(Form)
        self.ciphertext.setObjectName(u"ciphertext")

        self.verticalLayout.addWidget(self.ciphertext)

        self.mapping_table = QLineEdit(Form)
        self.mapping_table.setObjectName(u"mapping_table")

        self.verticalLayout.addWidget(self.mapping_table)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pre_image = QLineEdit(Form)
        self.pre_image.setObjectName(u"pre_image")

        self.horizontalLayout_2.addWidget(self.pre_image)

        self.image = QLineEdit(Form)
        self.image.setObjectName(u"image")

        self.horizontalLayout_2.addWidget(self.image)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.submit_key_button = QPushButton(Form)
        self.submit_key_button.setObjectName(u"submit_key_button")

        self.horizontalLayout.addWidget(self.submit_key_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.plaintext = QTextEdit(Form)
        self.plaintext.setObjectName(u"plaintext")

        self.verticalLayout.addWidget(self.plaintext)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.suggestions = QTextEdit(Form)
        self.suggestions.setObjectName(u"suggestions")

        self.verticalLayout_2.addWidget(self.suggestions)

        self.decode_button = QPushButton(Form)
        self.decode_button.setObjectName(u"decode_button")

        self.verticalLayout_2.addWidget(self.decode_button)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.submit_key_button.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4\u5bc6\u94a5\u5b57", None))
        self.decode_button.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
    # retranslateUi

