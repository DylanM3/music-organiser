# IMPORTS
import os
from tinytag import TinyTag

def get_music_location() -> str:
    # Ask the user for a path to the music and return it
    music_path: str = input("Please enter the location of your music library / playlist: ")
    return music_path

def check_music(music_path):
    for file in os.listdir(music_path):
        if file.lower().endswith(".mp3"):
            print(f"Reading {file}...")

def temp_main():
    music_path = get_music_location()
    check_music(music_path)

temp_main()