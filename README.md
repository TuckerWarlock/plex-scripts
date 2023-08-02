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