# Form implementation generated from reading ui file 'play_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Ui_Play_Window(object):
    def setupUi(self, Play_Window):
        Play_Window.setObjectName("Play_Window")
        Play_Window.resize(976, 643)
        self.centralwidget = QtWidgets.QWidget(Play_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.countLabel = QtWidgets.QLabel(self.centralwidget)
        self.countLabel.setGeometry(QtCore.QRect(644, 30, 250, 150))
        self.countLabel.setMinimumSize(QtCore.QSize(250, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.countLabel.setFont(font)
        self.countLabel.setStyleSheet("background-color: rgba(34, 31, 31, 0.9);\n"
                                      "border-radius:20px;\n"
                                      "color: rgb(255, 255, 255);")
        self.countLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.countLabel.setObjectName("countLabel")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(30, 30, 250, 150))
        self.timeLabel.setMinimumSize(QtCore.QSize(250, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("background-color: rgba(34, 31, 31, 0.9);\n"
                                     "border-radius:20px;\n"
                                     "color: rgb(255, 255, 255);")
        self.timeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.camLabel = QtWidgets.QLabel(self.centralwidget)
        self.camLabel.setGeometry(QtCore.QRect(0, 0, 941, 611))
        self.camLabel.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.camLabel.setText("")
        self.camLabel.setObjectName("camLabel")
        self.camLabel.raise_()
        self.countLabel.raise_()
        self.timeLabel.raise_()
        Play_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Play_Window)
        QtCore.QMetaObject.connectSlotsByName(Play_Window)

    def retranslateUi(self, Play_Window):
        _translate = QtCore.QCoreApplication.translate
        Play_Window.setWindowTitle(_translate("Play_Window", "MainWindow"))
        self.countLabel.setText(_translate("Play_Window", "0"))
        self.timeLabel.setText(_translate("Play_Window", "0"))


class Ui_startWidget(QWidget):
    def __init__(self, parent):
        super(Ui_startWidget, self).__init__(parent)

    def setupUi(self, startWidget):
        startWidget.setObjectName("startWidget")
        startWidget.resize(532, 281)
        self.widget = QtWidgets.QWidget(startWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 532, 281))
        self.widget.setStyleSheet("background-color: rgba(34, 31, 31, 0.6);\n"
                                  "border-radius:40px;")
        self.widget.setObjectName("widget")
        self.startButton = QtWidgets.QPushButton(self.widget)
        self.startButton.setGeometry(QtCore.QRect(340, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(251, 95, 56);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius:20px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./window/icons/play.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QtCore.QSize(20, 20))
        self.startButton.setCheckable(False)
        self.startButton.setObjectName("startButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(376, 49, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: transparent;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(117, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: transparent;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.timeLabel = QtWidgets.QLabel(self.widget)
        self.timeLabel.setGeometry(QtCore.QRect(290, 100, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(255, 255, 255);")
        self.timeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.itemLabel = QtWidgets.QLabel(self.widget)
        self.itemLabel.setGeometry(QtCore.QRect(40, 100, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.itemLabel.setFont(font)
        self.itemLabel.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(255, 255, 255);")
        self.itemLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.itemLabel.setObjectName("itemLabel")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(268, 20, 2, 181))
        self.label_8.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.exitButton = QtWidgets.QPushButton(self.widget)
        self.exitButton.setGeometry(QtCore.QRect(80, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(49, 51, 55);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius:20px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./window/icons/exit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exitButton.setIcon(icon1)
        self.exitButton.setIconSize(QtCore.QSize(25, 25))
        self.exitButton.setObjectName("exitButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(349, 50, 30, 30))
        self.label_2.setStyleSheet("background-color: transparent;\n"
                                   "border-image: url(./window/icons/clock.svg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(87, 48, 35, 35))
        self.label_3.setStyleSheet("background-color: transparent;\n"
                                   "border-image: url(./window/icons/js.svg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(startWidget)
        QtCore.QMetaObject.connectSlotsByName(startWidget)

    def retranslateUi(self, startWidget):
        _translate = QtCore.QCoreApplication.translate
        startWidget.setWindowTitle(_translate("startWidget", "Form"))
        self.startButton.setText(_translate("startWidget", " 开始"))
        self.label.setText(_translate("startWidget", "时间"))
        self.label_4.setText(_translate("startWidget", "项目"))
        self.timeLabel.setText(_translate("startWidget", "60 s"))
        self.itemLabel.setText(_translate("startWidget", "引体向上"))
        self.exitButton.setText(_translate("startWidget", " 退出"))


class Ui_finishWidget(QWidget):
    def __init__(self, parent):
        super(Ui_finishWidget, self).__init__(parent)

    def setupUi(self, finishWidget):
        finishWidget.setObjectName("finishWidget")
        finishWidget.resize(538, 286)
        self.widget = QtWidgets.QWidget(finishWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 532, 281))
        self.widget.setStyleSheet("background-color: rgba(34, 31, 31, 0.6);\n"
                                  "border-radius:40px;")
        self.widget.setObjectName("widget")
        self.exitButton = QtWidgets.QPushButton(self.widget)
        self.exitButton.setGeometry(QtCore.QRect(400, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(251, 95, 56);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius:20px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./window/icons/exit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exitButton.setIcon(icon)
        self.exitButton.setIconSize(QtCore.QSize(20, 20))
        self.exitButton.setCheckable(False)
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(300, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: transparent;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(415, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: transparent;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 91, 61))
        self.label_3.setStyleSheet("background-color: transparent;\n"
                                   "image: url(./window/icons/star.svg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: transparent;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.timeLabel = QtWidgets.QLabel(self.widget)
        self.timeLabel.setGeometry(QtCore.QRect(280, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(255, 255, 255);")
        self.timeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.calorieLabel = QtWidgets.QLabel(self.widget)
        self.calorieLabel.setGeometry(QtCore.QRect(400, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.calorieLabel.setFont(font)
        self.calorieLabel.setStyleSheet("background-color: transparent;\n"
                                        "color: rgb(255, 255, 255);")
        self.calorieLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.calorieLabel.setObjectName("calorieLabel")
        self.countLabel = QtWidgets.QLabel(self.widget)
        self.countLabel.setGeometry(QtCore.QRect(40, 100, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.countLabel.setFont(font)
        self.countLabel.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(255, 255, 255);")
        self.countLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.countLabel.setObjectName("countLabel")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(250, 20, 2, 251))
        self.label_8.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(30, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: transparent;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.retryButton = QtWidgets.QPushButton(self.widget)
        self.retryButton.setGeometry(QtCore.QRect(270, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.retryButton.setFont(font)
        self.retryButton.setStyleSheet("background-color: rgb(49, 51, 55);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius:20px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./window/icons/retry.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.retryButton.setIcon(icon1)
        self.retryButton.setIconSize(QtCore.QSize(25, 25))
        self.retryButton.setObjectName("retryButton")

        self.retranslateUi(finishWidget)
        QtCore.QMetaObject.connectSlotsByName(finishWidget)

    def retranslateUi(self, finishWidget):
        _translate = QtCore.QCoreApplication.translate
        finishWidget.setWindowTitle(_translate("finishWidget", "Form"))
        self.exitButton.setText(_translate("finishWidget", " 退出"))
        self.label.setText(_translate("finishWidget", "时间"))
        self.label_2.setText(_translate("finishWidget", "卡路里"))
        self.label_4.setText(_translate("finishWidget", "成绩"))
        self.timeLabel.setText(_translate("finishWidget", "1:00"))
        self.calorieLabel.setText(_translate("finishWidget", "24"))
        self.countLabel.setText(_translate("finishWidget", "60"))
        self.label_9.setText(_translate("finishWidget", "超过宇宙99.9999%的生物"))
        self.retryButton.setText(_translate("finishWidget", " 重试"))


class Ui_pauseWidget(QWidget):
    def __init__(self, parent):
        super(Ui_pauseWidget, self).__init__(parent)

    def setupUi(self, pauseWidget):
        pauseWidget.setObjectName("pauseWidget")
        pauseWidget.resize(532, 281)
        self.widget = QtWidgets.QWidget(pauseWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 532, 281))
        self.widget.setStyleSheet("background-color: rgba(34, 31, 31, 0.6);\n"
                                  "border-radius:40px;")
        self.widget.setObjectName("widget")
        self.continueButton = QtWidgets.QPushButton(self.widget)
        self.continueButton.setGeometry(QtCore.QRect(300, 170, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.continueButton.setFont(font)
        self.continueButton.setStyleSheet("background-color: rgb(251, 95, 56);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius:30px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./window/icons/play.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.continueButton.setIcon(icon)
        self.continueButton.setIconSize(QtCore.QSize(30, 30))
        self.continueButton.setObjectName("continueButton")
        self.exitButton = QtWidgets.QPushButton(self.widget)
        self.exitButton.setGeometry(QtCore.QRect(90, 170, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(49, 51, 55);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius:30px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./window/icons/exit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exitButton.setIcon(icon1)
        self.exitButton.setIconSize(QtCore.QSize(25, 25))
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(220, 60, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent;\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(130, 50, 91, 81))
        self.widget_2.setStyleSheet("image: url(./window/icons/pause.svg);\n"
                                    "border-radius:0;\n"
                                    "background-color:transparent;")
        self.widget_2.setObjectName("widget_2")

        self.retranslateUi(pauseWidget)
        QtCore.QMetaObject.connectSlotsByName(pauseWidget)

    def retranslateUi(self, pauseWidget):
        _translate = QtCore.QCoreApplication.translate
        pauseWidget.setWindowTitle(_translate("pauseWidget", "Form"))
        self.continueButton.setText(_translate("pauseWidget", " 继续"))
        self.exitButton.setText(_translate("pauseWidget", " 退出"))
        self.label.setText(_translate("pauseWidget", "暂 停"))
