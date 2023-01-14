import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Ui_Messagebox_success(QWidget):
    def __init__(self, parent):
        super(Ui_Messagebox_success, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)

        self.closePushButton.clicked.connect(self.exit)
        self.okPushButton.clicked.connect(self.exit)

    def setupUi(self, Messagebox_success):
        Messagebox_success.setObjectName("Messagebox_success")
        Messagebox_success.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Messagebox_success.resize(400, 200)
        self.widget = QtWidgets.QWidget(Messagebox_success)
        self.widget.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.widget.setStyleSheet("#widget{\n"
                                  "    background-color: #F3F5FD;\n"
                                  "    border-radius:10px;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 25))
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(325, -4, 71, 31))
        self.widget_4.setStyleSheet("QPushButton{\n"
                                    "    border:none;\n"
                                    "    border-radius:8px;\n"
                                    "}")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton.setStyleSheet("background-color: rgb(40, 194, 50);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_2.setStyleSheet("background-color: rgb(255,199,124);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.closePushButton = QtWidgets.QPushButton(self.widget_4)
        self.closePushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.closePushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.closePushButton.setStyleSheet("background-color: rgb(252, 70, 70);")
        self.closePushButton.setText("")
        self.closePushButton.setObjectName("closePushButton")
        self.gridLayout.addWidget(self.closePushButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 25))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 19, 80, 80))
        self.label.setStyleSheet("border-image: url(./window/icons/msg_success.svg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textLabel = QtWidgets.QLabel(self.widget_2)
        self.textLabel.setGeometry(QtCore.QRect(126, 29, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        self.textLabel.setFont(font)
        self.textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textLabel.setObjectName("textLabel")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_5.setStyleSheet("#widget_5{\n"
                                    "    border-top:1px solid rgb(239, 239, 240)\n"
                                    "}")
        self.widget_5.setObjectName("widget_5")
        self.okPushButton = QtWidgets.QPushButton(self.widget_5)
        self.okPushButton.setGeometry(QtCore.QRect(292, 11, 91, 27))
        self.okPushButton.setObjectName("okPushButton")
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(Messagebox_success)
        QtCore.QMetaObject.connectSlotsByName(Messagebox_success)

    def retranslateUi(self, Messagebox_success):
        _translate = QtCore.QCoreApplication.translate
        Messagebox_success.setWindowTitle(_translate("Messagebox_success", "Form"))
        self.textLabel.setText(_translate("Messagebox_success", "您的账号注册成功啦 :D"))
        self.okPushButton.setText(_translate("Messagebox_success", "好"))

    def move_position(self):
        parent_width = self.parent.width()
        parent_height = self.parent.height()
        msg_box_width = self.width()
        msg_box_height = self.height()
        self.move(int((parent_width/2) - (msg_box_width/2)), int((parent_height/2) - (msg_box_height/2)))

    def exit(self):
        self.close()


class Ui_Messagebox_error(QWidget):
    def __init__(self, parent):
        super(Ui_Messagebox_error, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)

        self.closePushButton.clicked.connect(self.exit)
        self.okPushButton.clicked.connect(self.exit)

    def setupUi(self, Messagebox_error):
        Messagebox_error.setObjectName("Messagebox_error")
        Messagebox_error.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Messagebox_error.resize(400, 200)
        self.widget = QtWidgets.QWidget(Messagebox_error)
        self.widget.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.widget.setStyleSheet("#widget{\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "    border-radius:10px;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 25))
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(325, -4, 71, 31))
        self.widget_4.setStyleSheet("QPushButton{\n"
                                    "    border:none;\n"
                                    "    border-radius:8px;\n"
                                    "}")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton.setStyleSheet("background-color: rgb(40, 194, 50);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_2.setStyleSheet("background-color: rgb(255,199,124);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.closePushButton = QtWidgets.QPushButton(self.widget_4)
        self.closePushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.closePushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.closePushButton.setStyleSheet("background-color: rgb(252, 70, 70);")
        self.closePushButton.setText("")
        self.closePushButton.setObjectName("closePushButton")
        self.gridLayout.addWidget(self.closePushButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 25))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 19, 80, 80))
        self.label.setStyleSheet("border-image: url(./window/icons/msg_error.svg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textLabel = QtWidgets.QLabel(self.widget_2)
        self.textLabel.setGeometry(QtCore.QRect(126, 29, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        self.textLabel.setFont(font)
        self.textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textLabel.setObjectName("textLabel")
        self.textLabel.raise_()
        self.label.raise_()
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_5.setStyleSheet("#widget_5{\n"
                                    "    border-top:1px solid rgb(239, 239, 240)\n"
                                    "}")
        self.widget_5.setObjectName("widget_5")
        self.okPushButton = QtWidgets.QPushButton(self.widget_5)
        self.okPushButton.setGeometry(QtCore.QRect(292, 11, 91, 27))
        self.okPushButton.setObjectName("okPushButton")
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 2)
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.widget_5.raise_()

        self.retranslateUi(Messagebox_error)
        QtCore.QMetaObject.connectSlotsByName(Messagebox_error)

    def retranslateUi(self, Messagebox_error):
        _translate = QtCore.QCoreApplication.translate
        Messagebox_error.setWindowTitle(_translate("Messagebox_error", "Form"))
        self.textLabel.setText(_translate("Messagebox_error", ""))
        self.okPushButton.setText(_translate("Messagebox_error", "好"))

    def move_position(self):
        parent_width = self.parent.width()
        parent_height = self.parent.height()
        msg_box_width = self.width()
        msg_box_height = self.height()
        self.move(int((parent_width/2) - (msg_box_width/2)), int((parent_height/2) - (msg_box_height/2)))

    def exit(self):
        self.close()
        sys.exit(-2)
