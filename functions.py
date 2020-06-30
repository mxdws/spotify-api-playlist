import requests
import base64, json

def getAccessToken(clientID, clientSecret):
    # Initialise Requests Variables
    authUrl = "https://accounts.spotify.com/api/token"
    authHeader = {}
    authData = {}

    # Base64 Encode Client ID and Client Secret
    message = f"{clientID}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    # print(base64_message)

    authHeader['Authorization'] = "Basic " + base64_message
    authData['grant_type'] = "client_credentials"

    res = requests.post(authUrl, headers=authHeader, data=authData)

    responseObject = res.json()
    # print(json.dumps(responseObject, indent=2))

    accessToken = responseObject['access_token']

    return accessToken

def getPlaylistTracks(token, playlistID):
    playlistEndPoint = f"https://api.spotify.com/v1/playlists/{playlistID}"

    getHeader = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(playlistEndPoint, headers=getHeader)

    playlistObject = res.json()

    return playlistObject
