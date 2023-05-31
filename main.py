import discord

from discord import app_commands

from configHandler import loadConfig
from credentialsHandler import loadCredentials
from commandsImport import *


def onMessage(commandTree, discordServerId):
    @commandTree.command(name='take', description='Take attendance')
    @app_commands.describe(otp='OTP Code')
    async def take(interaction, otp: str):
        await takeAttendance(interaction, otp)

    @commandTree.command(name='register', description='Register Attendix credentials')
    @app_commands.describe(username="Username", password="Password")
    async def register(interaction, username: str, password: str):
        await registerUser(interaction, username, password)

def main():
    config = loadConfig()
    loadCredentials()

    discordToken = config['Settings']['discord_token']
    discordServersIdRaw = config['Settings']['discord_server_id'].split(',')
    discordServersId = []
    for discordServerIdRaw in discordServersIdRaw:
        discordServersId.append(discord.Object(id=discordServerIdRaw.strip()))
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = discord.Client(intents=intents)
    commandTree = app_commands.CommandTree(client)

    onMessage(commandTree, discordServersId)

    @client.event
    async def on_ready():
        await client.wait_until_ready()
        for discordServerId in discordServersId:
            await commandTree.sync(guild=discordServerId)
        # await commandTree.sync()
        await client.change_presence(activity=discord.Game(name="Powered by autoAttendix2"))
        print(f'{client.user} has connected to Discord!')

    client.run(token=discordToken)

if __name__ == '__main__':
    main()