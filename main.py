import requests

try:
    from secret_info import *
    from artist import *

except ModuleNotFoundError:
    print("Error import file, check secret_info.py, artist.py")
    exit(-1)

AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"

AUTH_PARAMS = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}

try:
    auth_response = requests.post(AUTH_URL, AUTH_PARAMS)
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']

    headers = {"Authorization": f"Bearer {access_token}"}
    artist = requests.get(f"{BASE_URL}artists/{ARTIST_ID}",
                          headers=headers).json()["name"]

    r_albums = requests.get(f"{BASE_URL}artists/{ARTIST_ID}/albums",
                            headers=headers,
                            params={'include_groups': "album,single,compilation"}).json()

    albums = []
    tracks = []

    for count, album in enumerate(r_albums["items"]):
        print(f"loading album {count+1}/{len(r_albums['items'])}")

        albums.append({"name": album["name"],
                       "album_type": album["album_type"],
                       "release_date": album["release_date"],
                       "total_tracks": album["total_tracks"],
                       "id": album["id"]})

        tracks_in_albums = requests.get(f"{BASE_URL}albums/{album['id']}/tracks",
                                        headers=headers).json()["items"]

        for track in tracks_in_albums:
            tracks.append({"track_name": track["name"],
                           "album_name": album["name"],
                           "track_number": track["track_number"],
                           "release_date": album["release_date"],
                           "id": track["id"]})
    print("loading is complete!\n\n")

    print(f"artist: {artist}\n\n")

    print("albums:", end=" ")
    for album in albums:
        print(album, end="\n\t\t")

    print("\ntracks:", end=" ")
    for track in tracks:
        print(track, end="\n\t\t")

except KeyError:
    print("Error key, check ARTIST_TOKEN, CLIENT_ID, CLIENT_SECRET")
    exit(-1)




