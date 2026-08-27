# IMPORTS
from music import get_music_location, check_music, get_music_info
from analysis import create_dataframe, show_chart

if __name__ == "__main__":

    music_path = get_music_location()
    check_music(music_path)
    songs = get_music_info(music_path)

    df = create_dataframe(songs)
    show_chart(df)

