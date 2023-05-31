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
        try:
            signResponse = signAttendance(otp, credentials[credential]["username"], credential[credential]["password"])

            if signResponse == 'Class not found':
                errorSign += f"{credential.username} -> Class not found\n"
                continue

            if signResponse == 'Unauthorized':
                errorSign += f"{credential.username} -> Invalid credentials\n"
                continue

            successSign += f"{credential.username} -> {signResponse}\n"
        except:
            errorSign += f"{credential.username} -> Unhandled Error\n"
            continue

    if len(successSign) == 0:
        await interaction.response.send_message("Invalid code", ephemeral=True)
        return

    if len(successSign) > 0:
        finalResponse = "Successfully signed for:\n" + successSign

    if len(errorSign) > 0:
        finalResponse += "\nError signing for:\n" + errorSign

    finalResponse = finalResponse.strip()
    await interaction.response.send_message(finalResponse)

def verifyCode(otp) -> bool:
    if (otp.isdecimal()) == False:
        return False

    if (len(otp) != 3):
        return False

    return True