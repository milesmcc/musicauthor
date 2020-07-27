Here are {{track_count}} songs across {{genre_count}} genres that I've been listening to lately.

To listen to this playlist on Spotify, [click here]({{playlist_link}}). Note that song metadata --- the genres, duration, release date, etc. --- is provided by the Spotify API. I don't input this information myself, so it might be wrong!

{% for genre, songs in genre_groups.items() %}
### {{genre | capitalize | replace("r&b", "R&B") | replace("idm", "IDM") }}
{% for song in songs %}
{% raw %}{{<{% endraw %} song title="{{song.name}}" artists="{{ song.artists_display }}" album="{{song.album.name}}" date="{{song.album.release_date}}" preview="{{song.preview_url}}" duration="{{ song.data.duration_ms / 60}}" genres="{{song.genres_display}}" url="{{ song.external_urls.spotify}}" image="{{song.album.images.0.url}}" {% raw %}>}}{% endraw %}
{% endfor %}
{% endfor %}