# Discord Bot - Get IP bot

Basically the idea is to have a way to get the bot's server's current IP. Useful for getting a dynamic IP, just use the command `/locate`.

## Before you start

Create a Discord bot and fill the variables in the `config.py` file. Make sure you register this application command!
```python
import requests


url = "https://discord.com/api/v10/applications/<my_application_id>/commands"

json = {
    "name": "locate",
    "type": 1,
    "description": "Returns the public IP address where the bot is located",
}

# For authorization use your bot token
headers = {
    "Authorization": "Bot <my_bot_token>"
}

r = requests.post(url, headers=headers, json=json)
```

Make sure the bot has permission to send messages to your server.

## Standalone usage

```
git clone https://github.com/anthares101/get-ip-bot-dc.git
cd get-ip-bot-dc
pip install -r requirements.txt
```

Start the bot script with `python main.py`.

## Docker usage

### Recommended way

This repository takes care of building a docker image when necessary and uploads it to [DockerHub](https://hub.docker.com/r/anthares101/get-ip-bot-dc). You don't need to build anything!

```
docker run -v </PATH/TO/YOUR/config.py>:/app/config.py anthares101/get-ip-bot-dc:latest
```

### Build it yourself

To build the image, simply run:

```
docker build -t get-ip-bot-dc .
```

After that is done, you can start your container:

```
docker run -v </PATH/TO/YOUR/config.py>:/app/config.py get-ip-bot-dc
```
