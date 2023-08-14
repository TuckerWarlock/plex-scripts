# plex-scripts
Collection of scripts for managing your Plex library.

## mp4 to mkv
This script allows you to convert all .mp4 files in a specified directory (and its subdirectories) to .mkv format, and optionally deletes the original .mp4 files, using the `mkvmerge` utility from MKVToolNix.

### Prerequisites
- [MKVToolNix](https://mkvtoolnix.download/)
- Python 3.6 or later

### Setup
- Download and install MKVToolNix.
- Clone this repository to your local machine.
- Open `mp4_to_mkv.py` in a text editor and set `mkvmergePath` to the path of your `mkvmerge` executable. The default location is set for Windows 10. For macOS and Linux, you will need to adjust the path accordingly.

### Usage
This script can be run in two modes: dry-run mode and normal mode.

#### Dry-run Mode
In dry-run mode, the script will traverse the directory structure, starting from a parent directory that you specify, and write the full paths of all .mp4 files to the `mp4_files_to_convert.txt` file. No files are actually converted in this mode.

To run the script in dry-run mode, use the following command:

```
python mp4_to_mkv.py --dry-run
```

When prompted, enter the parent directory to search for .mp4 files.

#### Normal Mode
In normal mode, the script will read the paths from the `mp4_files_to_convert.txt` file (generated in the dry-run mode), convert those .mp4 files to .mkv format using `mkvmerge`, delete the original .mp4 files, and record the paths of the successfully converted and deleted files in `converted_files.txt` and `deleted_files.txt`, respectively.

To run the script in normal mode, use the following command:

```
python mp4_to_mkv.py
```

At the end of the execution, the script will print the number of files to be converted, the number of files actually converted and deleted, and the difference between the number of files converted and deleted. The paths written in `converted_files.txt` and `deleted_files.txt` are just the base names of the files, not the full paths.

### Notes
- Be sure to run the script in dry-run mode first to generate the `mp4_files_to_convert.txt` file.
- Be aware that this script will delete the original .mp4 files after converting them to .mkv. If you want to keep the original files, make a backup before running the script.
- The paths in the output .txt files are located in the `results` subdirectory.
- The file paths may need to be updated to accommodate for escaping \ / characters.



## TV Show Subtitle Organizer

This Python script is designed to organize subtitle files for TV shows stored in a specific directory structure. The script looks for English subtitle files (identified by "Eng" or "eng" in the filename) in each episode's folder, selects the largest one if there are multiple, and copies it to the corresponding season folder while preserving the language information in the filename.

### Directory Structure

The script is designed to work with a specific directory structure:

```
TV Shows Folder
│
└───Show A
│   └───Season 1
│   │   │   Episode 1
│   │   │   Episode 2
│   │   │   Episode 3
│   │   └───Subs
│   │       └───Episode1
│   │           Episode1_subtitle_eng.srt
│   │           Episode1_subtitle_fre.srt
│   │       └───Episode2
│   │           Episode2_subtitle_eng.srt
│   │           Episode2_subtitle_fre.srt
│   │       └───Episode3
│   │           Episode3_subtitle_eng.srt
│   │           Episode3_subtitle_fre.srt
│   └───Season 2
│       │   ...
│   
└───Show B
    │   ...
```

Each show has its own folder, which contains one folder per season. Each season folder contains an 'Episode' folder and a 'Subs' folder. The 'Subs' folder contains one folder per episode, which in turn contain subtitle files. The script is designed to work with .srt files.

### Usage

1. Save the script into a Python file, for example `move_subs.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `move_subs.py` using the `cd` command.
4. Run the script using Python. You'll need to have Python installed on your computer. You can run the script like this:
    ```bash
    python move_subs.py
    ```
5. The script will prompt you to enter the path to the TV Shows folder. Input the path and press Enter.

The script will then process each show and season, copying the English .srt files from the episode folders in the 'Subs' folders to their parent Season folders. It will print out a message each time it copies a file, so you can see what it's doing.

### Warning

Remember to back up your data before running this script. This script will modify your filesystem, and mistakes can lead to data loss.


## Movie Subtitle Organizer Script

### Description

This Python script assists in organizing subtitle files for movies. It scans a directory containing movies, searches for English subtitle files (.srt) in a "Subs" folder under each movie's folder, and then copies the first found English subtitle file to the corresponding movie's folder. The copied subtitle file is renamed to match the movie's name with a '.en.srt' extension. This script will streamline your movie subtitle organization process.

### Usage

1. Ensure Python 3 is installed on your machine.

2. Run the script from the command line as follows:
   ```
   python movie_subtitle_organizer.py
   ```

3. When prompted, input the full path to the directory containing your movies. The expected folder structure is as follows:

   ```
   Movies Folder
   ├── Movie 1
   │   └── Subs
   │       ├── English.srt
   │       ├── Spanish.srt
   │       └── ...
   ├── Movie 2
   │   └── Subs
   │       ├── English.srt
   │       ├── Spanish.srt
   │       └── ...
   └── ...
   ```

### Important Notes

- Each movie should have its own folder within the root Movies folder.
- The script expects each movie folder to contain a "Subs" folder.
- The "Subs" folder should contain your .srt subtitle files.
- The script is designed to copy only English .srt files. If you have subtitles in different languages, you may need to modify the script to suit your needs.

### Warning

This script copies subtitle files, leaving the original files untouched. However, it's always a good practice to have a backup of your files before running any script that modifies files, due to the risk of data loss.

### Troubleshooting

If you encounter issues, please check the following:

- Make sure your folder structure matches the structure described above.
- Ensure your subtitle files end with the ".srt" extension and that English subtitle files include the word "English" in their name.
- Check you have sufficient permissions to read and write in the specified directory.


## Parts-to-SRT Folder Mapper

## Description:
This was the closest I could get to pulling the name of folder(s) that was seeding when the client lost connection to the source/destination folder(s). So far the only issues with this method are if the subtitle file isn't included in the directory or if it took longer to initialize the download, the created date for the `.parts` file won't match anything and won't come back with a folder name.

This script maps `.parts` files to corresponding folders that contain `.srt` files with the same creation timestamp. The primary use-case is to identify which movie or series a `.parts` file corresponds to by locating its matching subtitle `.srt` file. 

### Key Features:
1. Gathers all `.parts` files and their creation timestamps from a given root directory.
2. Searches for `.srt` files throughout the directory structure.
3. Maps each `.parts` file to a folder containing an `.srt` file with a matching creation timestamp.
4. If the `.srt` file resides in a folder named "Subs", the script will use the parent directory of "Subs" for mapping.
5. Outputs the mapping results to a file named `results.txt`.

### How to Use:
1. Set the `root_folder` variable in the script to the desired root path of your movie/series directory.
2. Execute the script.
3. Review the generated `results.txt` file for the mapping results.

### Output Format:
The `results.txt` file will contain lines in the following format:

```
<parts_file_name> -> <folder_name>
```

Where:
- `<parts_file_name>` is the name of the `.parts` file.
- `<folder_name>` is the name of the folder containing a matching `.srt` file. If the `.srt` file is inside a "Subs" folder, the parent directory of "Subs" is used.

### Notes:
- Timestamp matching uses a threshold of 1 second, meaning `.srt` and `.parts` files with creation timestamps within 1 second of each other are considered a match.
- The script recursively searches all sub-directories under the provided `root_folder`.
- Ensure you have necessary read permissions on the `root_folder` and write permissions where the script resides (for the `results.txt` file).
