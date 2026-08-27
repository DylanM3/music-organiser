# IMPORTS
import os
from tinytag import TinyTag

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

def get_music_info(music_path):
    # Loop through songs, combining paths for TinyTag
    for file in os.listdir(music_path):
        full_path = os.path.join(music_path, file)

        # List the Artists of each track in the music_path
        tag: TinyTag = TinyTag.get(full_path)
        print(f"{tag.artist}")

def temp_main():
    music_path = get_music_location()
    check_music(music_path)
    get_music_info(music_path)

temp_main()
