import os
import subprocess
import argparse

# Parse the arguments
parser = argparse.ArgumentParser(description='Convert mp4 files to mkv and delete the original files.')
parser.add_argument('--dry-run', action='store_true', help='If given, only print the paths of mp4 files and do not perform actual conversion.')
args = parser.parse_args()

# Set up the initial variables
mkvmergePath = r"C:\\Program Files\\MKVToolNix\\mkvmerge.exe" 
if args.dry_run:
    parent_dir = input("Enter parent folder to search for mp4's: ")

# Counters
total_files_to_convert = 0
files_converted = 0
files_deleted = 0

# Output directory
output_dir = "results"
os.makedirs(output_dir, exist_ok=True)  # Creates the directory if it doesn't exist

# Output files
dry_run_output_file_path = os.path.join(output_dir, "mp4_files_to_convert.txt")
converted_output_file_path = os.path.join(output_dir, "converted_files.txt")
deleted_output_file_path = os.path.join(output_dir, "deleted_files.txt")

# Clear the contents of output files before writing
if args.dry_run:
    open(dry_run_output_file_path, 'w').close()
else:
    open(converted_output_file_path, 'w').close()
    open(deleted_output_file_path, 'w').close()

if args.dry_run:
    # Traverse directory recursively
    for dirpath, dirs, files in os.walk(parent_dir):
        for filename in files:
            if filename.endswith(".mp4"):
                total_files_to_convert += 1

                # Get the full file path
                inputFileFullPath = os.path.join(dirpath, filename)

                # Write the path to the dry run output file
                with open(dry_run_output_file_path, 'a') as f:
                    f.write(inputFileFullPath + '\n')
else:
    with open(dry_run_output_file_path, 'r') as f:
        file_paths = f.readlines()

    for inputFileFullPath in file_paths:
        inputFileFullPath = inputFileFullPath.strip()  # Remove newline character

        # Get the directory and file path
        dirpath, filename = os.path.split(inputFileFullPath)
        outputFileFullPath = os.path.join(dirpath, os.path.splitext(filename)[0] + ".mkv")

        # Create the command
        cmd = f'"{mkvmergePath}" --output "{outputFileFullPath}" --video-tracks 0 --no-audio --no-subtitles --language "0:und" --track-name "0:" --default-track "0:yes" --forced-track "0:no" "{inputFileFullPath}" --track-order 0:0'

        # Execute the command and get the result
        result = subprocess.run(cmd, shell=True)

        # Check the return code to determine success or failure
        if result.returncode == 0:
            files_converted += 1
            with open(converted_output_file_path, 'a') as f:
                f.write(os.path.basename(outputFileFullPath) + '\n')

            try:
                os.remove(inputFileFullPath)
                files_deleted += 1
                with open(deleted_output_file_path, 'a') as f:
                    f.write(os.path.basename(inputFileFullPath) + '\n')
            except PermissionError:
                print(f'Could not delete file: {os.path.basename(inputFileFullPath)}. It is being used by another process.')
        else:
            print(f'Failure: {cmd}')

# Print the final counts
print(f'Total number of files to convert: {total_files_to_convert}')
if not args.dry_run:
    print(f'Number of files converted: {files_converted}')
    print(f'Number of files deleted: {files_deleted}')
    print(f'Difference between converted and deleted: {files_converted - files_deleted}')
