from PyQt5.QtWidgets import QApplication
from login_panel.login_panel import LoginPanel

import sys
import json
import os
import requests

from env import VERSION, URL

from tendo import singleton
# will sys.exit(-1) if other instance is running
me = singleton.SingleInstance()


# Main function
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


def main():
    path = f"{os.getenv('APPDATA')}/SnakeGame/api_token.ini"
    # checking if path exists and if token exists and is valid
    if os.path.exists(path):
        with open(path, "r") as api_token_file:
            api_token = api_token_file.readline()
            request = {
                "api_token": api_token,
                "version": VERSION
            }

            response = requests.post(f'{URL}/api/v1/wczytanie-danych-tokenem', data=request)
            data = json.loads(response.text)

            token_is_valid = False
            reason_to_close_game = False

            # if there is a reason to not open a game
            # example: game is out-of-date
            try:
                if data["reason_to_close_game"]:
                    reason_to_close_game = True
                    show_login_panel()
            except:
                pass

            # if there is NO reason to NOT open a game
            # trying to check if api token is valid
            if reason_to_close_game is False:
                try:
                    print(data["result"]["id"])
                    token_is_valid = True
                except:
                    show_login_panel()

            if token_is_valid:
                import main_game_application.game_application
                main_game_application.game_application.run_game_application()
    else:
        # if path doesnt exist --> user is first time logging in
        show_login_panel()


if __name__ == "__main__":
    main()

