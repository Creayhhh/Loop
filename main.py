from PyQt6.QtWidgets import QApplication
import sys

from login_page import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_ui = LoginWindow()
    login_ui.show()
    sys.exit(app.exec())
