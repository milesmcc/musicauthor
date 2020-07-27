import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import webbrowser

def no_browser(x):
    raise webbrowser.Error()
webbrowser.open = no_browser

scope = "user-library-modify user-library-read user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path=".spotipy"))

def song_data(song_id: str) -> dict:
    return sp.audio_features(song_id)

def artist_data(artist_id: str) -> dict:
    return sp.artist(artist_id)

def read_playlist(playlist_id: str) -> list:
    playlist = sp.playlist(playlist_id)
    return {
        "tracks": [track["track"] for track in playlist["tracks"]["items"]],
        "uri": playlist["external_urls"]["spotify"],
        "name": playlist["name"],
        "description": playlist["description"],
    }