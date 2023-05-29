import configparser

CONFIG_FILE_NAME = "config.ini"
config = configparser.ConfigParser()

def generateDefaultConfig():
    sections = ['Settings']
    settings = [['discord_token', '{token}']]

    for section in sections:
        try:
            config.add_section(section)
        except configparser.DuplicateSectionError:
            pass

    for setting in settings:
        config['Settings'][setting[0]] = setting[1]

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def loadConfig():
    try:
        config.read(CONFIG_FILE_NAME)
        config['Settings']['discord_token']
    except KeyError:
        generateDefaultConfig()

    return config