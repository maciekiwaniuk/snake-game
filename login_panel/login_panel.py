import sys
import json
import os
import webbrowser
import requests

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence, QCursor
from PyQt5.QtWidgets import QMainWindow, QShortcut, QApplication

from env import VERSION, SECRET_GAME_KEY, URL


def show_login_panel():
    # Creating instance of QApplication class
    # QApplication takes a list of string as input
    # So QApplication is also able to work with [] argument
    # app = QApplication([])

    app = QApplication(sys.argv)

    # Creating object of the main application class
    window = LoginPanel()

    # Shows the application window
    window.show()

    # exec_() call starts the event-loop
    # and will block until the application quits
    sys.exit(app.exec_())


class LoginPanel(QMainWindow):
    # Initializing constructor
    def __init__(self):
        # Initializing constructor of inherited class
        # which is passed in the argument of the class
        super(LoginPanel, self).__init__()
        # super().__init__() is the same

        # object name, size of the window, background and window title
        self.setObjectName("LoginPanel")
        self.setWindowIcon(QtGui.QIcon(os.path.join("assets", "images", "icon.png")))
        self.setFixedSize(784, 600)
        self.setStyleSheet("background-color: #8BCA67;")

        # Method that shows user interface
        self.show_ui()

    # Overriding the closeEvent method to prevent auto closing app
    # when user clicked exit or login
    def close_event(self, event):
        event.accept()
        self.hide()

    @staticmethod
    def check_internet_connection():
        url = "https://www.google.pl/"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            return True
        except:
            return False

    def try_to_login(self):
        if self.check_internet_connection() is False:
            self.error_label.setHidden(False)
            self.error_label.setText("Brak połączenia z internetem")
            return

        request = {
            "email": self.email.text(),
            "password": self.password.text(),
            "version": VERSION
        }

        if len(request["email"]) >= 1 and len(request["password"]) >= 1:
            response = requests.post(f'{URL}/api/v1/logowanie-do-gry', data=request)
            data = json.loads(response.text)
            if data["result"]["success"] is False:
                self.error_label.setHidden(False)
                self.error_label.setText(data["result"]["error_message"])

            if data["result"]["success"]:
                path = f"{os.getenv('APPDATA')}/SnakeGame"
                # checking if directory doesnt exist
                if os.path.exists(path) is False:
                    folder = "SnakeGame"
                    create_path = os.path.join(os.getenv('APPDATA'), folder)
                    os.mkdir(create_path)

                filename = "api_token.ini"
                with open(os.path.join(path, filename), "w") as api_file:
                    api_file.write(data["result"]["api_token"])
                # closing login panel
                self.close()
                # starting main game application
                import main_game_application.game_application
                main_game_application.game_application.run_game_application()

    # Method which is showing UI
    def show_ui(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(0, 0, 781, 121))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(230, 160, 101, 41))
        self.email_label.setStyleSheet("font-size: 25px;")
        self.email_label.setObjectName("email_label")
        self.login_submit = QtWidgets.QPushButton(self.centralwidget)
        self.login_submit.setGeometry(QtCore.QRect(260, 400, 261, 61))
        self.login_submit.setStyleSheet(
            "QPushButton{background-color: #EBE99E; color: black; font-size: 35px; border-radius: 28px; border:2px solid black;}\n"
            "QPushButton:hover{background-color: rgb(217, 216, 176);}")
        self.login_submit.setObjectName("login_submit")
        self.login_submit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(230, 200, 331, 41))
        self.email.setStyleSheet("font-size: 20px; border: 2px solid black;")
        self.email.setText("")
        self.email.setObjectName("email")

        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(230, 245, 451, 25))
        self.error_label.setStyleSheet("font-size: 14px; color: #cc0000; font-weight: 700;")
        self.error_label.setObjectName("connection_error_label")
        self.error_label.setHidden(True)

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(230, 280, 101, 41))
        self.password_label.setStyleSheet("font-size: 25px;")
        self.password_label.setObjectName("password_label")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(230, 320, 331, 41))
        self.password.setStyleSheet("font-size: 20px; border: 2px solid black;")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.visit_site_label = QtWidgets.QLabel(self.centralwidget)
        self.visit_site_label.setGeometry(QtCore.QRect(170, 510, 231, 41))
        self.visit_site_label.setStyleSheet("font-size: 21px")
        self.visit_site_label.setObjectName("visit_site_label")
        self.visit_site_button = QtWidgets.QPushButton(self.centralwidget)
        self.visit_site_button.setGeometry(QtCore.QRect(410, 510, 171, 41))
        self.visit_site_button.setStyleSheet(
            "QPushButton{background-color: #EBE99E; color: black; font-size: 21px; border-radius: 12px; border:2px solid black;}\n"
            "QPushButton:hover{background-color: rgb(217, 216, 176);}")
        self.visit_site_button.setObjectName("visit_site_button")
        self.visit_site_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

        # app mechanism - clicks etc
        self.mechanism()

    # Method which is changing name of buttons
    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LoginPanel", "Panel logowania"))
        self.title_label.setText(_translate("LoginPanel", "Panel logowania do gry"))
        self.email_label.setText(_translate("LoginPanel", "Email"))
        self.login_submit.setText(_translate("LoginPanel", "Zaloguj"))
        self.email.setPlaceholderText(_translate("LoginPanel", "Podaj email"))
        self.password_label.setText(_translate("LoginPanel", "Hasło"))
        self.password.setPlaceholderText(_translate("LoginPanel", "Podaj hasło"))
        self.visit_site_label.setText(_translate("LoginPanel", "Nie masz jeszcze konta?"))
        self.visit_site_button.setText(_translate("LoginPanel", "Odwiedź stronę"))
        self.error_label.setText(_translate("LoginPanel", ""))

    def mechanism(self):
        self.visit_site_button.clicked.connect(lambda: webbrowser.open(f'{URL}/rejestracja', new=2))
        self.login_submit.clicked.connect(lambda: self.try_to_login())

        self.enter = QShortcut(QKeySequence('Return'), self)
        self.enter.activated.connect(lambda: self.try_to_login())