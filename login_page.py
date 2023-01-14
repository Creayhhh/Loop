from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui

import sys

import utils
from index_page import IndexWindow
from window.login_window import Ui_Login_window

from request import login, register
import messagebox


class LoginWindow(QMainWindow, Ui_Login_window):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.index_ui = None

        self.user_config = QtCore.QSettings('./user/user_config.ini', QtCore.QSettings.Format.IniFormat)

        self.move_flag = False
        self.move_Position = None
        self.setupUi(self)

        self.registerHeightLineEdit.setValidator(QtGui.QIntValidator())
        self.registerWeightLineEdit.setValidator(QtGui.QIntValidator())

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)

        self.closeButton.clicked.connect(sys.exit)
        self.LoginButton.clicked.connect(self.user_login)
        self.toRegister_Button.clicked.connect(self.to_register_page)
        self.toLogin_Button.clicked.connect(self.to_login_page)
        self.registerButton.clicked.connect(self.user_register)

        data = self.read_userconfig()
        self.UsernameLineEdit.setText(data["username"] if data["username"] is not None else "")
        self.PwdLineEdit.setText(data["password"] if data["password"] is not None else "")
        self.rememberPwd_checkBox.setChecked(True if data["remember_password"] == "1" else False)

    def user_login(self):
        username = self.UsernameLineEdit.text()
        password = self.PwdLineEdit.text()
        if username == "" or password == "":
            self.errorLabel.setText("用户名和密码不能为空")
            return
        success, msg = login(username, password)
        if success:
            data = {
                "username": username,
                "password": password if self.rememberPwd_checkBox.isChecked() else None,
                "remember_password": 1 if self.rememberPwd_checkBox.isChecked() else 0
            }
            self.write_userconfig(data)
            self.close()
            self.index_ui = IndexWindow(token=msg)
            self.index_ui.showFullScreen()
            self.index_ui.show()
        else:
            self.errorLabel.setText(msg)

    def user_register(self):
        if (self.registerUsernameLineEdit.text() == "") or (self.registerPasswordLineEdit.text() == "") or \
                (self.registerNicknameLineEdit.text() == "") or (self.registerHeightLineEdit.text() == "") \
                or (self.registerWeightLineEdit.text() == ""):
            self.registerErrorLabel.setText("请完善表单内容")
        else:
            self.registerErrorLabel.setText("")
            user = {
                "username": self.registerUsernameLineEdit.text(),
                "password": self.registerPasswordLineEdit.text(),
                "nickname": self.registerNicknameLineEdit.text(),
                "sex": "男" if self.registerManPushButton.isChecked() else "女",
                "height": int(self.registerHeightLineEdit.text()),
                "weight": int(self.registerWeightLineEdit.text())
            }

            state, msg = register(user)

            if state:
                messagebox.messagebox_success(self, "您的账号注册成功啦 :D")
                self.to_login_page()
            else:
                self.registerErrorLabel.setText(msg)

    def to_register_page(self):
        self.stackedWidget.setCurrentWidget(self.register_page)
        # 还原表单初始状态
        self.UsernameLineEdit.clear()
        self.PwdLineEdit.clear()
        self.errorLabel.setText("")

    def to_login_page(self):
        self.stackedWidget.setCurrentWidget(self.login_page)
        # 还原表单初始状态
        self.registerUsernameLineEdit.clear()
        self.registerPasswordLineEdit.clear()
        self.registerNicknameLineEdit.clear()
        self.registerHeightLineEdit.clear()
        self.registerWeightLineEdit.clear()
        self.registerManPushButton.setChecked(True)
        self.registerErrorLabel.setText("")

    def read_userconfig(self):
        user_data = {
            "username": self.user_config.value("username"),
            "password": utils.decrypt_3des(self.user_config.value("password")) if self.user_config.value(
                "password") is not None else None,
            "remember_password": self.user_config.value("remember_password")
        }
        return user_data

    def write_userconfig(self, data):
        self.user_config.setValue("username", data["username"])
        self.user_config.setValue("password",
                                  utils.encrypt_3des(data["password"]) if data["remember_password"] == 1 else None)
        self.user_config.setValue("remember_password", data["remember_password"])

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.move_flag = True
            self.move_Position = event.globalPosition().toPoint() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.MouseButton.LeftButton and self.move_flag:
            self.move(QMouseEvent.globalPosition().toPoint() - self.move_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.move_flag = False
