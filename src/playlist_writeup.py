import api
import sys
import jinja2
import random

# Basic setup

if len(sys.argv) != 4:
    print("Usage: <playlist id> <template location> <output location>")

playlist = sys.argv[1]
template_loc = sys.argv[2]
output_loc = sys.argv[3]

with open(template_loc, "r") as infile:
    data = infile.read()
    template = jinja2.Template(data)

# Get songs from the API

playlist = api.read_playlist(playlist)

genres = []
tracks = []

for song in playlist["tracks"]:
    song_data = api.song_data(song["id"])[0]
    artist_data = api.artist_data(song["artists"][0]["id"])
    song.update(data=song_data, artist=artist_data,
                genres=artist_data["genres"] or [],
                genres_display=", ".join(artist_data["genres"] or []), artists_display=', '.join(
                    [artist["name"] for artist in song["artists"]]))
    genres.extend(artist_data["genres"])
    tracks.append(song)

genres = sorted(
    set(genres), key=lambda k: len(list(filter(lambda v: v == k, genres))), reverse=True)


def main_genre(track_genres):
    for genre in genres:
        if genre in track_genres:
            return genre
    return "genreless"


genre_groups = {}

for song in tracks:
    genre = main_genre(song["genres"])
    if not genre in genre_groups:
        genre_groups[genre] = []
    genre_groups[genre].append(song)

random.shuffle(genres)

with open(output_loc, "w") as outfile:
    outfile.write(template.render(genre_groups=genre_groups,
                                  track_count=len(playlist["tracks"]),
                                  genre_count=len(genres),
                                  playlist_link=playlist["uri"],
                                  genres_display=", ".join(genres)))
