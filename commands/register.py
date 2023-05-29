from commands.apspace import verifyCredential
from credentialsHandler import addCredential

async def registerUser(interaction, username, password):
    username = username.upper()
    verifyResponse = verifyCredential(username, password)
    discordId = interaction.user.id

    if not verifyResponse:
        await interaction.response.send_message("Invalid username or password", ephemeral=True)
        return
    
    if addCredential(discordId, username, password):
        await interaction.response.send_message("User registered successfully", ephemeral=True)
        return

    await interaction.response.send_message("Error registering", ephemeral=True)