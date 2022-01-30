# Snake game ![](https://github.com/maciekiwaniuk/snake-game/blob/main/assets/images/icon.png?raw=true) 

> ### Project of the game which interacts via API with the web application that handles necessary stuff related with storing data.

- The whole application is made in [python](https://www.python.org/downloads/).
- To create login panel is used [PyQt5 Framework](https://pypi.org/project/PyQt5/).
- Game application is made with [pygame library](https://getbootstrap.com/docs/5.1/getting-started/introduction/).
- Properly configured [web application](https://github.com/maciekiwaniuk/snake-web-app) is necessary to update data.

# Installation

To successfully install application you need to have installed [python](https://www.python.org/downloads/), [pip](https://pypi.org/project/pip/) and properly configured web application which is available to get from [here](https://github.com/maciekiwaniuk/snake-web-app).

Open folder where you want to have project files, open console and then clone the repository

    git clone https://github.com/maciekiwaniuk/snake-game
	
Change folder in console to created folder with project files

	cd snake-game

Install all the required modules using pip

    pip install -r requirements.txt

Copy the env_example.py file and make the required configuration changes in the env.py file

    copy env_example.py env.py
    
Configuration variables should be the same as in the .env in web application.

    SECRET_GAME_KEY = "example_secret_game_key"
    VERSION = "example_game_version_1.0"
    URL = "http://127.0.0.1:8000"

Run application

    py main.py

# Application usage

To log into game you need to use account from configured web application. Example data from seeded database

    email: admin1234@wp.pl

    password: admin1234

    