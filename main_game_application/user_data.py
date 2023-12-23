import pygame
import json
import sys
import requests
import hashlib
from datetime import datetime

from constants import *
from env import VERSION, SECRET_GAME_KEY, URL

pygame.init()
pygame.font.init()


# class for saved user data from file
class UserData:
    def __init__(self):
        self.load_user_data()

    @staticmethod
    def clear_api_file():
        path = f"{os.getenv('APPDATA')}/SnakeGame/api_token.ini"
        with open(path, "w") as api_token_file:
            api_token_file.write("")

    def load_user_data(self):
        path = f"{os.getenv('APPDATA')}/SnakeGame/api_token.ini"
        with open(path, "r") as api_token_file:
            self.api_token = api_token_file.readline()

        secret_hash = '{}.{}.{}'.format(SECRET_GAME_KEY, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), VERSION)
        request = {
            "api_token": self.api_token,
            "secret_hash": hashlib.sha256(secret_hash.encode('utf-8')).hexdigest(),
        }
        response = requests.post(f'{URL}/api/v1/wczytanie-danych-tokenem', data=request)
        data = json.loads(response.text)

        self.name = data["result"]["name"]
        self.user_id = data["result"]["id"]
        self.ip = data["ip"]

        self.coins = data["result"]["user_game_data"]["coins"]
        self.total_coins_earned = data["result"]["user_game_data"]["total_coins_earned"]
        self.points = data["result"]["user_game_data"]["points"]
        self.play_time_seconds = data["result"]["user_game_data"]["play_time_seconds"]

        self.games_amount = data["result"]["user_game_data"]["games_amount"]
        self.hit_wall = data["result"]["user_game_data"]["hit_wall"]
        self.hit_snake = data["result"]["user_game_data"]["hit_snake"]
        self.clicks = data["result"]["user_game_data"]["clicks"]
        self.selected_lvl = data["result"]["user_game_data"]["selected_level"]

        self.ate_fruits_amount = data["result"]["user_game_data"]["ate_fruits_amount"]
        self.ate_fruits_on_easy = data["result"]["user_game_data"]["ate_fruits_on_easy"]
        self.ate_fruits_on_medium = data["result"]["user_game_data"]["ate_fruits_on_medium"]
        self.ate_fruits_on_hard = data["result"]["user_game_data"]["ate_fruits_on_hard"]
        self.ate_fruits_on_speed = data["result"]["user_game_data"]["ate_fruits_on_speed"]

        self.coins_upgrade_lvl = data["result"]["user_game_data"]["coins_upgrade_lvl"]
        self.points_upgrade_lvl = data["result"]["user_game_data"]["points_upgrade_lvl"]
        self.fruits_upgrade_lvl = data["result"]["user_game_data"]["fruits_upgrade_lvl"]

        self.selected_fruits_upgrade_lvl = data["result"]["user_game_data"]["selected_fruits_upgrade_lvl"]

        self.head_skin = data["result"]["user_game_data"]["selected_head_skin"]
        self.body_skin = data["result"]["user_game_data"]["selected_body_skin"]
        self.fruit_skin = data["result"]["user_game_data"]["selected_fruit_skin"]
        self.board_skin = data["result"]["user_game_data"]["selected_board_skin"]

        self.medium_diff = data["result"]["user_game_data"]["unlocked_medium"]
        self.hard_diff = data["result"]["user_game_data"]["unlocked_hard"]
        self.speed_diff = data["result"]["user_game_data"]["unlocked_speed"]

        self.easy_record = data["result"]["user_game_data"]["easy_record"]
        self.medium_record = data["result"]["user_game_data"]["medium_record"]
        self.hard_record = data["result"]["user_game_data"]["hard_record"]
        self.speed_record = data["result"]["user_game_data"]["speed_record"]

        self.head_skins = data["result"]["user_game_data"]["head_skins"]
        self.body_skins = data["result"]["user_game_data"]["body_skins"]
        self.fruit_skins = data["result"]["user_game_data"]["fruit_skins"]
        self.board_skins = data["result"]["user_game_data"]["board_skins"]

        self.fps = data["result"]["user_game_data"]["fps"]
        self.music = data["result"]["user_game_data"]["music"]
        self.effects = data["result"]["user_game_data"]["effects"]
        self.volume = data["result"]["user_game_data"]["volume"]

    def save_user_data(self):
        path = f"{os.getenv('APPDATA')}/SnakeGame/api_token.ini"
        with open(path, "r") as api_token_file:
            api_token = api_token_file.readline()
        # checking if token wasn't changed while playing or
        # logged out from all pc using website
        if api_token != self.api_token:
            pygame.quit()
            sys.exit()

        if self.total_coins_earned >= self.coins:
            request = {}
            request["api_token"] = self.api_token
            request["selected_level"] = self.selected_lvl

            request["coins"] = self.coins
            request["total_coins_earned"] = self.total_coins_earned
            request["points"] = self.points
            request["play_time_seconds"] = self.play_time_seconds

            request["games_amount"] = self.games_amount
            request["hit_wall"] = self.hit_wall
            request["hit_snake"] = self.hit_snake
            request["clicks"] = self.clicks

            request["ate_fruits_amount"] = self.ate_fruits_amount
            request["ate_fruits_on_easy"] = self.ate_fruits_on_easy
            request["ate_fruits_on_medium"] = self.ate_fruits_on_medium
            request["ate_fruits_on_hard"] = self.ate_fruits_on_hard
            request["ate_fruits_on_speed"] = self.ate_fruits_on_speed

            request["coins_upgrade_lvl"] = self.coins_upgrade_lvl
            request["points_upgrade_lvl"] = self.points_upgrade_lvl
            request["fruits_upgrade_lvl"] = self.fruits_upgrade_lvl

            request["selected_fruits_upgrade_lvl"] = self.selected_fruits_upgrade_lvl

            request["selected_head_skin"] = self.head_skin
            request["selected_body_skin"] = self.body_skin
            request["selected_fruit_skin"] = self.fruit_skin
            request["selected_board_skin"] = self.board_skin

            request["unlocked_medium"] = self.medium_diff
            request["unlocked_hard"] = self.hard_diff
            request["unlocked_speed"] = self.speed_diff

            request["easy_record"] = self.easy_record
            request["medium_record"] = self.medium_record
            request["hard_record"] = self.hard_record
            request["speed_record"] = self.speed_record

            request["head_skins"] = self.head_skins
            request["body_skins"] = self.body_skins
            request["fruit_skins"] = self.fruit_skins
            request["board_skins"] = self.board_skins

            request["fps"] = self.fps
            request["music"] = self.music
            request["effects"] = self.effects
            request["volume"] = self.volume

            secret_hash = '{}.{}.{}'.format(SECRET_GAME_KEY, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), VERSION)
            request["secret_hash"] = hashlib.sha256(secret_hash.encode('utf-8')).hexdigest()

            response = requests.post(f'{URL}/api/v1/zapisanie-danych-tokenem', data=request)

            try: # check if user has out-of-date game version
                 # check if user got ban
                 # check if user changed token while playing
                data = json.loads(response.text)
                if data["reason_to_close_game"]:
                    self.clear_api_file()
                    pygame.quit()
                    sys.exit()
            except: pass

    def create_open_game_log(self):
        secret_hash = '{}.{}.{}'.format(SECRET_GAME_KEY, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), VERSION)
        request = {
            "api_token": self.api_token,
            "secret_hash": hashlib.sha256(secret_hash.encode('utf-8')).hexdigest(),
            "user_id": self.user_id,
            "ip": self.ip
        }
        requests.post(f'{URL}/api/v1/zapisanie-logu-wejsciowego', data=request)

    def create_exit_game_log(self):
        secret_hash = '{}.{}.{}'.format(SECRET_GAME_KEY, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), VERSION)
        request = {
            "api_token": self.api_token,
            "secret_hash": hashlib.sha256(secret_hash.encode('utf-8')).hexdigest(),
            "user_id": self.user_id,
            "ip": self.ip
        }
        requests.post(f'{URL}/api/v1/zapisanie-logu-wyjsciowego', data=request)

    def create_logout_game_log(self):
        secret_hash = '{}.{}.{}'.format(SECRET_GAME_KEY, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), VERSION)
        request = {
            "api_token": self.api_token,
            "secret_hash": hashlib.sha256(secret_hash.encode('utf-8')).hexdigest(),
            "user_id": self.user_id,
            "ip": self.ip
        }
        requests.post(f'{URL}/api/v1/zapisanie-logu-wylogowania', data=request)
