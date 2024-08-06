import configparser

from logger import log

CONFIG_FILE_NAME = "./data/config.ini"
config = configparser.ConfigParser()

def generateDefaultConfig():
    sections = ['Settings']
    settings = [['discord_token', '{token}'],['discord_server_id', '{id}, {id}']]

    for section in sections:
        try:
            config.add_section(section)
        except configparser.DuplicateSectionError:
            pass

    for setting in settings:
        config['Settings'][setting[0]] = setting[1]

    with open(CONFIG_FILE_NAME, 'w') as configfile:
        config.write(configfile)

def loadConfig():
    try:
        config.read(CONFIG_FILE_NAME)
        config['Settings']['discord_token']
        config['Settings']['discord_server_id']
    except KeyError:
        generateDefaultConfig()
        log("Config file not found or incomplete, generating default config file.")
        exit()

    return config