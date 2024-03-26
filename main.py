import logging
import config
import discord
from discord import app_commands
from requests import get

# Initial setup
log_handler = discord.utils.setup_logging()
intents = discord.Intents.default()

# Prepare client
application = discord.Client(intents=intents)
application_command_tree = app_commands.CommandTree(application)

# Commands:
@application_command_tree.command()
async def locate(interaction: discord.Interaction):
    logging.info("IP request received")
    public_ip = get('https://api.ipify.org').text
    await interaction.response.send_message(f'{config.HOSTNAME} is at {public_ip}')

if __name__ == '__main__':
    application.run(config.TOKEN, log_handler=log_handler)
