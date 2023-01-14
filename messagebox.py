from window.message_ui import Ui_Messagebox_success, Ui_Messagebox_error


def messagebox_success(parent_object, text):
    messagebox = Ui_Messagebox_success(parent_object)
    messagebox.textLabel.setText(text)
    messagebox.move_position()
    messagebox.show()


def messagebox_error(parent_object, text):
    messagebox = Ui_Messagebox_error(parent_object)
    messagebox.textLabel.setText(text)
    messagebox.move_position()
    messagebox.show()
