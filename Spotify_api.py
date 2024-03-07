import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

print("")
artists_name = input("Enter artist's Name: ")
#num_album = int(input("Enter how many album: "))

client_id = "ffe78d14f08f4b1ab902d7026223175a"
client_secret = "9ce4c0556d9f4a848a1af037dae228f0"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

results = spotify.search(q=artists_name, type='artist')
items = results['artists']['items']



if len(items) == 0:
    print(f"Artist '{artists_name}' not found.")
else:
    artists_uri = items[0]['uri']
    results = spotify.artist_albums(artists_uri, album_type='album')
    albums = results['items']
    print("")

    print(f"Albums by {artists_name}:")
    print("")
    for album in albums:
        #for num in range(1, num_album + 1):
            #print((num), (album['name']))
        print(album['name'])