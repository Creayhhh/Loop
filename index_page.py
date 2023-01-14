import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem

import messagebox
import request
from play_page import PlayWindow
from request import get_userinfo, refresh_token
from window.index_history_item import Ui_HistoryItem
from window.index_window import Ui_Index_Window


class IndexWindow(QMainWindow, Ui_Index_Window):
    def __init__(self, token, parent=None):
        super(IndexWindow, self).__init__(parent)
        self.token = token
        self.userinfo = None
        self.setupUi(self)

        self.play_window = None

        self.sport_name_dict = {"chinning": "引体向上", "jumpingJacks": "开合跳", "push": "俯卧撑",
                                "squat": "深蹲", "dumbbell": "哑铃"}
        self.sport_name = "squat"
        self.time = 10

        self.history_query_date = None

        self.slot_init()
        self.init_widget()
        self.get_user()

    def init_widget(self):
        self.pageListWidget.setCurrentRow(0)
        # item.setIcon(QtGui.QIcon("./window/icons/home_blue.svg"))
        self.pageStackedWidget.setCurrentWidget(self.indexPage)

    def slot_init(self):
        self.pageListWidget.currentItemChanged.connect(self.pageListWidget_change)
        self.exitButton.clicked.connect(self.exit)
        self.startButton.clicked.connect(self.start_sport)

        self.sportTime_Slider.valueChanged.connect(self.change_sport_time)

        self.pushChoice_Button.clicked.connect(lambda: self.change_select_sports("push"))
        self.chinningChoiceButton.clicked.connect(lambda: self.change_select_sports("chinning"))
        self.squatChoice_Button.clicked.connect(lambda: self.change_select_sports("squat"))
        self.jumpingJacksChoice_Button.clicked.connect(lambda: self.change_select_sports("jumpingJacks"))
        self.dumbbellChoiceButton.clicked.connect(lambda: self.change_select_sports("dumbbell"))

        self.history_sift_pushButton.clicked.connect(self.history_sift)
        self.history_reset_pushButton.clicked.connect(self.history_reset)
        self.history_calendarWidget.selectionChanged.connect(self.history_calendar_change)

    def get_user(self):
        self.userinfo = get_userinfo(self.token)
        if self.userinfo is None:
            access_token = refresh_token(self.token)
            if access_token is None:
                print("登录已过期")
                sys.exit(0)
            self.token["access_token"] = access_token
            self.userinfo = get_userinfo(self.token)

        self.nickname_Label.setText(self.userinfo["nickname"])

    def change_sport_time(self):
        self.time = self.sportTime_Slider.value()
        min = 0
        sec = self.time

        while sec >= 60:
            min += 1
            sec -= 60

        self.leftTime_Label.setText(str(min) + " 分 " + str(sec) + " 秒")
        self.rightTime_Label.setText(str(min) + " 分 " + str(sec) + " 秒")

    def change_select_sports(self, sport_name):
        self.sport_name = sport_name
        self.item_Label.setText(self.sport_name_dict[sport_name])

    def pageListWidget_change(self, current, previous):
        if current.text() == '首页':
            self.pageStackedWidget.setCurrentWidget(self.indexPage)
            current.setIcon(QtGui.QIcon("./window/icons/home_blue.svg"))
        elif current.text() == '开始运动':
            self.pageStackedWidget.setCurrentWidget(self.sportPage)
            current.setIcon(QtGui.QIcon("./window/icons/yl_blue.svg"))
        elif current.text() == '运动记录':
            self.history_reset()
            self.pageStackedWidget.setCurrentWidget(self.historyPage)
            current.setIcon(QtGui.QIcon("./window/icons/history_blue.svg"))
        elif current.text() == '设置':
            self.pageStackedWidget.setCurrentWidget(self.settingsPage)
            current.setIcon(QtGui.QIcon("./window/icons/settings_blue.svg"))

        if previous is not None:
            if previous.text() == '首页':
                previous.setIcon(QtGui.QIcon("./window/icons/home.svg"))
            elif previous.text() == '开始运动':
                previous.setIcon(QtGui.QIcon("./window/icons/yl.svg"))
            elif previous.text() == '运动记录':
                previous.setIcon(QtGui.QIcon("./window/icons/history.svg"))
            elif previous.text() == '设置':
                previous.setIcon(QtGui.QIcon("./window/icons/settings.svg"))

    def start_sport(self):
        self.token["access_token"] = refresh_token(self.token)
        if self.token["access_token"]:
            self.hide()
            self.play_window = PlayWindow(self, sport=self.sport_name, time=self.time)
            self.play_window.showFullScreen()
            self.play_window.show()
        else:
            messagebox.messagebox_error(self, "登录过期了 o(￣┰￣*)ゞ")

    def history_query(self, data):
        success, history_list = request.query_sport_history(self.token, data)
        if success:
            return history_list
        else:
            # 刷新access_token再试一次，不行就是登录过期或服务器炸了
            self.token["access_token"] = request.refresh_token(self.token)
            if self.token["access_token"]:
                success, history_list = request.query_sport_history(self.token, data)
                if success:
                    return history_list
                else:
                    messagebox.messagebox_error(self, "服务器炸了 (╯°Д°)╯︵ ┻━┻")
            else:
                messagebox.messagebox_error(self, "登录过期了 o(￣┰￣*)ゞ")

    def history_sift(self):
        select_sport = None
        for button in self.history_sport_groupBox.findChildren(QtWidgets.QPushButton):
            if button.isChecked():
                select_sport = button.text()

        if select_sport == "全部":
            select_sport = None

        if select_sport is None and self.history_query_date is None:
            data = {
                "username": self.userinfo["username"]
            }
        else:
            if select_sport is None:
                data = {
                    "username": self.userinfo["username"],
                    "start_time": self.history_query_date
                }
            elif self.history_query_date is None:
                data = {
                    "username": self.userinfo["username"],
                    "sport_name": select_sport
                }
            else:
                data = {
                    "username": self.userinfo["username"],
                    "sport_name": select_sport,
                    "start_time": self.history_query_date
                }
        history_list = self.history_query(data)
        self.history_show(history_list)

    def history_reset(self):
        self.history_query_date = None
        self.history_query_all_pushButton.setChecked(True)
        self.history_calendarWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.history_calendarWidget.setSelectedDate(QtCore.QDate.currentDate())
        history_list = self.history_query({"username": self.userinfo["username"]})
        self.history_show(history_list)

    def history_show(self, history_list):
        self.historyListWidget.clear()
        if history_list:
            for record in history_list[::-1]:
                item = QListWidgetItem()
                widget = Ui_HistoryItem()
                widget.sport_name_label.setText(record["sport_name"])
                widget.count_label.setText(str(record["count"]))
                widget.sport_time_label.setText(str(record["sport_time"]) + " s")
                widget.start_time_label.setText(record["start_time"])
                item.setSizeHint(QtCore.QSize(self.historyListWidget.width() - 4, widget.height()))
                self.historyListWidget.addItem(item)
                self.historyListWidget.setItemWidget(item, widget)
        else:
            messagebox.messagebox_error(self, "登录过期了 o(￣┰￣*)ゞ")

    def history_calendar_change(self):
        self.history_query_date = self.history_calendarWidget.selectedDate().toString("yyyy-MM-dd")

    def exit(self):
        self.close()
