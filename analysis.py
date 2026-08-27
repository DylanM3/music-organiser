# IMPORTS
from music import get_music_location, check_music, get_music_info
import pandas as pd
import matplotlib.pyplot as plt

def create_dataframe(songs):
    df = pd.DataFrame({
        'title': [song.title for song in songs],
        'artist': [song.artist for song in songs],
        'album': [song.album for song in songs],
        'duration': [song.duration for song in songs]
    })
    return df

def show_chart(df):
    # Group by artist and count the number of titles they have
    artist_counts = df.groupby('artist')['title'].count()

    labels = [f"{artist} — {count}" for artist, count in artist_counts.items()]

    artist_counts.plot.pie(autopct='%1.1f%%')

    plt.ylabel("")
    plt.legend(labels, title="Artist — Tracks", loc="center left", bbox_to_anchor=(-0.5, 0.5))
    plt.show()