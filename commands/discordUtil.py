async def sendDm(interaction, message):
    await sendTurnOnDM(interaction)
    userObject = interaction.user
    dmChannel = await userObject.create_dm()
    await dmChannel.send(message)

async def sendTurnOnDM(interaction):
    await interaction.response.send_message(
        f'Please allow direct message for registering.\n'
        f'You can turn on direct message in `Settings` > `Privacy & Safety` > `Allow direct messages from server members.`'
        , ephemeral=True)