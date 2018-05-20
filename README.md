# Doob Bot

A simple Raider.io bot for discord

### To use:


* cd into the project directory and create a virtual environment:
`python3 -m venv env`


* activate the virtual environment:
`source env/bin/activate`


* install requirements:
`python3 -m pip install -r requirements.pip`


* create a secrets file and write your bot token to it:
`echo 'BOT_TOKEN='<your_secret_token>' > secrets.py`


* add the bot to your discord server by going to your unique client ID link:

https://discordapp.com/oauth2/authorize?client_id=<your_client_id>&scope=bot


* run the app:
`python3 doob.py`


### Bot Commands
*replace all spaces in realm names with underscore*

*All commands require a character name and realm name. If no region is given the Bot will default to US*

|Command                                          |Description                                                 |
|-------------------------------------------------|------------------------------------------------------------|
|#info <character> <realm_name> <region>          | Basic info about character.                                | 
|#ioscore <character> <realm_name> <region>       | The Raider.io score of a character.                        |
|#highest <character> <realm_name> <region>       | Three highest mythic dungeons completed by character.      |
|#best <character> <realm_name> <region>          | Three best scoring mythic dungeons completed by character. |
