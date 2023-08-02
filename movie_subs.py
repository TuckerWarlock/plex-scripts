import os
import glob
import shutil

def process_movie_folder(movie_folder):
    movie_name = os.path.basename(movie_folder)
    subs_folder = os.path.join(movie_folder, "Subs")
    subtitle_files = glob.glob(os.path.join(subs_folder, "*.srt"))

    english_subtitle_files = [subtitle for subtitle in subtitle_files if 'english' in subtitle.lower()]
    if len(english_subtitle_files) > 0:
        subtitle_file = english_subtitle_files[0]
        new_subtitle_name = f"{movie_name}.en.srt"
        new_subtitle_path = os.path.join(movie_folder, new_subtitle_name)

        if not os.path.exists(new_subtitle_path):
            shutil.copy(subtitle_file, new_subtitle_path)
            print(f"Copied {subtitle_file} to {new_subtitle_path}")
        else:
            print(f"Skipping {movie_folder}: .en.srt file already exists")
    else:
        print(f"Skipping {movie_folder}: No English .srt files found in Subs folder")

def scan_movie_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for movie_folder in dirs:
            full_path = os.path.join(root, movie_folder)
            subs_folder = os.path.join(full_path, "Subs")

            if os.path.isdir(subs_folder):
                process_movie_folder(full_path)

# Prompt the user to enter the parent movie folder path
folder_path = input("Enter path to parent movie folder: ")
scan_movie_folder(folder_path)
