import datetime


def log(rawMsg):
    dateTime = datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
    msg = (dateTime + ' ' + rawMsg)
    print(msg)

    with open('latest.log', 'a') as logFile:
        logFile.write(msg +'\n')
