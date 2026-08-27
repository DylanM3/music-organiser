# IMPORTS
from music import get_music_location, check_music, get_music_info
import pandas as pd
import matplotlib.pyplot as plt

# TEMP CODE
music_path = get_music_location()
check_music(music_path)
songs = get_music_info(music_path)




df = pd.DataFrame({
    'title': [song.title for song in songs],
    'artist': [song.artist for song in songs],
    'album': [song.album for song in songs],
    'duration': [song.duration for song in songs]
})

# Group by artist and count the number of titles they have
artist_counts = df.groupby('artist')['title'].count()

# Plot the counts
artist_counts.plot.pie(autopct='%1.1f%%', title="Share of Tracks by Artist")
plt.ylabel("")
plt.show()