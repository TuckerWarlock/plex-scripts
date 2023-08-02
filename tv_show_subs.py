import os
import shutil

def process_season_folder(season_folder):
    subs_folder = os.path.join(season_folder, "Subs")

    for episode_folder in os.listdir(subs_folder):
        episode_folder_path = os.path.join(subs_folder, episode_folder)
        if os.path.isdir(episode_folder_path):
            eng_srt_files = [file for file in os.listdir(episode_folder_path) 
                             if file.endswith(".srt") and ("Eng" in file or "eng" in file)]
            if eng_srt_files:
                # Select the largest file
                largest_file = max(eng_srt_files, key=lambda file: os.path.getsize(os.path.join(episode_folder_path, file)))
                largest_file_path = os.path.join(episode_folder_path, largest_file)
                new_srt_name = f"{episode_folder}_{os.path.splitext(largest_file)[0]}.srt"
                new_srt_path = os.path.join(season_folder, new_srt_name)
                shutil.copy(largest_file_path, new_srt_path)
                print(f"Copied {largest_file_path} to {new_srt_path}")
            else:
                print(f"No English .srt files in {episode_folder_path}")

def scan_tv_shows_folder(folder_path):
    for show_folder in os.listdir(folder_path):
        full_show_path = os.path.join(folder_path, show_folder)
        if os.path.isdir(full_show_path):
            for season_folder in os.listdir(full_show_path):
                full_season_path = os.path.join(full_show_path, season_folder)
                subs_folder = os.path.join(full_season_path, "Subs")
                if os.path.isdir(subs_folder):
                    process_season_folder(full_season_path)

# Prompt the user to enter the TV shows folder path
folder_path = input("Enter path to TV shows folder: ")
scan_tv_shows_folder(folder_path)
