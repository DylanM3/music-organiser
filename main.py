# IMPORTS
from music import get_music_location, check_music, get_music_info

if __name__ == "__main__":
    music_path = get_music_location()
    check_music(music_path)
    songs = get_music_info(music_path)


# for song in songs:
#     print(f"{song.title}")
#     print(f"{song.artist}")