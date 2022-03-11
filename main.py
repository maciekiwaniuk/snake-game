import json
import os
import requests

from login_panel.login_panel import show_login_panel
from env import VERSION, URL

from tendo import singleton
# prevent the possibility of opening two instances of game
me = singleton.SingleInstance()


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

