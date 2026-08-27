# IMPORTS
import os
from tinytag import TinyTag

class Song:
    def __init__(self, tag: TinyTag):
        self.title = tag.title
        self.artist = tag.artist
        self.album = tag.album
        self.duration = tag.duration

def get_music_location() -> str:
    # Ask the user for a path to the music and return it
    music_path: str = input("Please enter the location of your music library / playlist: ")
    return music_path

def check_music(music_path):
    # Loop over each file, checking its a supported file type
    for file in os.listdir(music_path):
        if file.lower().endswith(".mp3"):
            continue
        else:
            # If its an unsupported type, log it and throw an error
            print(f"{file} is not a supported file type.")
            print("Please ensure this directory only contains supported file types")
            exit("musicTypeError")

def get_music_info(music_path) -> list[Song]:
    # Prepare array to be populated with songs
    songs = []

    # Loop through songs, combining paths for TinyTag
    for file in os.listdir(music_path):
        full_path = os.path.join(music_path, file)

        # Convert to Song class, and append to songs array
        tag: TinyTag = TinyTag.get(full_path)
        song = Song(tag)
        songs.append(song)

    return songs