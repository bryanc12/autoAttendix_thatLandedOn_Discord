import json
import os
import time

from logger import log

CRED_FILE_NAME = "user_credentials.json"

def generateDefaultFile():
    try:
        with open(CRED_FILE_NAME, 'w') as outfile:
            json.dump({}, outfile)
    except:
        return("Error while creating user_credentials.json")
    
    return True

def generateNewFile(newFileName):
    os.rename(CRED_FILE_NAME, newFileName)

    try:
        with open(CRED_FILE_NAME, 'w') as outfile:
            json.dump({}, outfile)
    except:
        return("Error while creating user_credentials.json")

    return True

def loadCredentials():
    credentials = {}

    try:
        with open(CRED_FILE_NAME) as json_file:
            credentials = json.load(json_file)

    except FileNotFoundError:
        success =  generateDefaultFile()
        if success == True:
            return ("File user_credentials.json not found, creating file user_credentials.json.")
        log(success)
        exit()
    
    except json.JSONDecodeError:
        newFileName = "user_credentials " + time.strftime("%Y-%m-%d-%H-%M-%S") + ".json.corrupted"
        success =  generateNewFile(newFileName)
        if success == True:
            return ("Corrupted user_credentials.json file, renamed to " + newFileName + ", creating new user_credentials.json.")
        log(success)
        exit()
    
    return credentials

def addCredential(discordId, username, password):
    credentials = {}

    try:
        with open(CRED_FILE_NAME) as json_file:
            credentials = json.load(json_file)
            credentials[discordId] = {"username": username, "password": password}

        with open(CRED_FILE_NAME, 'w') as json_file:
            json.dump(credentials, json_file)

    except FileNotFoundError:
        log(f"File not found while registering user \"{discordId}\" with \"{username}\" and \"{password}\"")
        return False
    
    except Exception:
        log(f"Unhandled error while registering user \"{discordId}\" with \"{username}\" and \"{password}\"")
        return False
        
    log(f"User \"{discordId}\" registered successfully with \"{username}\"")
    return True