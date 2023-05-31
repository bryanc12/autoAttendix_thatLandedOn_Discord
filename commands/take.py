from commands.apspace import signAttendance
from credentialsHandler import loadCredentials

async def takeAttendance(interaction, otp):
    credentials = loadCredentials()
    successSign = ""
    errorSign = ""
    finalResponse = ""

    if not verifyCode(otp):
        await interaction.response.send_message("Invalid code", ephemeral=True)
        return

    if len(credentials) == 0:
        await interaction.response.send_message("No credentials registered", ephemeral=True)
        return

    for credential in credentials.keys():
        username = credentials[credential]['username']
        password = credentials[credential]['password']

        try:
            signResponse = signAttendance(otp, username, password)

            if signResponse == 'Unauthorized':
                errorSign += f"{username} -> {signResponse}\n"
                continue

            if '-' in signResponse:
                errorSign += f"{username} -> {signResponse}\n"
                continue

            successSign += f"{username} -> {signResponse}\n"
        except:
            errorSign += f"{username} -> Unhandled Error\n"
            continue

    if len(successSign) == 0:
        await interaction.response.send_message("Invalid code", ephemeral=True)
        return

    if len(successSign) > 0:
        finalResponse = "Successfully taken for:\n" + successSign

    if len(errorSign) > 0:
        finalResponse += "\nError signing otp for:\n" + errorSign

    finalResponse = finalResponse.strip()
    await interaction.response.send_message(finalResponse)

def verifyCode(otp) -> bool:
    if (otp.isdecimal()) == False:
        return False

    if (len(otp) != 3):
        return False

    return True