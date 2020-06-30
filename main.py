import requests
import base64, json
from secrets import *
from functions import *

# To run this, you need to 
# 1. Create an App on Spotify Developers
# 2. Create a files called secrets.py in the root of this project
# 3. Copy your ClientID and ClientSecret to to the secrets.py file
# 4. Find a playlist that you want to return the json for

# Get Access Token
token = getAccessToken(clientID, clientSecret)

# Use Token to get Playlist data
playlistID = "1InbX5R7TCQ7IMa5JJOxXp?si=9XClVgQ0SSyX79-ysEWruA"
tracklist = getPlaylistTracks(token, playlistID)

# Print out Playlist name and songs

playlistName = tracklist['name']
print('-' * len(playlistName))
print(playlistName)
print('-' * len(playlistName))
for t in tracklist['tracks']['items']:
    artists=[]
    separator=', '
    for a in t['track']['artists']:
        artists.append(a['name'])
    artistsString = separator.join(artists)
    songName = t['track']['name']

    print(f"{songName} by {artistsString}")














