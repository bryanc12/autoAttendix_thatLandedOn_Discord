import requests

def signAttendance(otpCode, username, password):

    refreshTokenRequestUrl = 'https://cas.apiit.edu.my/cas/v1/tickets'
    signApiUrl = 'https://attendix.apu.edu.my/graphql'

    # Common header for questing refresh token and api request ticket
    commonHeader = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain',
    }

    refreshTokenRequestParameter = {
        'username': username,
        'password': password
    }

    refreshTokenResponse = requests.post(url=refreshTokenRequestUrl, headers=commonHeader, params=refreshTokenRequestParameter)
    refreshToken = refreshTokenResponse.text

    ticketRequestUrl = 'https://cas.apiit.edu.my/cas/v1/tickets/' + refreshToken + '?service=https://api.apiit.edu.my/attendix'
    ticketRequestParameter = {
        'service':'https://api.appit.edu.my/attendix'
    }

    ticketRequestResponse = requests.post(url=ticketRequestUrl, headers=commonHeader, params=ticketRequestParameter)
    ticket = ticketRequestResponse.text

    signHeader = {
        'accept':'application/json',
        'content-type':'application/json',
        'ticket':ticket,
        'x-amz-user-agent':'aws-amplify/2.0.7',
        'x-api-key':'da2-u4ksf3gspnhyjcokxzugo3mqr4'
    }

    signVariables = {
        'otp':otpCode
    }

    signQuery = 'mutation updateAttendance($otp: String!) {\n  updateAttendance(otp: $otp) {\n    id\n    attendance\n    classcode\n    date\n    startTime\n    endTime\n    classType\n    __typename\n  }\n}\n'

    signJson = {
        'operationName':'updateAttendance',
        'variables':signVariables,
        'query':signQuery
    }

    signResponse = requests.post(url=signApiUrl, headers=signHeader, json=signJson)
    signResponseJson = signResponse.json()

    if signResponseJson['data'] is not None:
        return(signResponseJson['data']['updateAttendance']['classcode'])
    else:
        return(signResponse.json()['errors'][0]['message'])
    
def verifyCredential(username, password):
    refreshTokenRequestUrl = 'https://cas.apiit.edu.my/cas/v1/tickets'

    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain',
    }

    parameter = {
        'username': username,
        'password': password
    }

    response = requests.post(url=refreshTokenRequestUrl, headers=header, params=parameter)
    refreshToken = response.text

    if refreshToken.startswith('TGT'):
        return True
    
    return False