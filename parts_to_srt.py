import os

def map_parts_to_srt_folders(root_path):
    mapping = {}
    parts_files_data = {}  # Store .parts files with their timestamps

    # Gather all .parts files and their creation timestamps
    for dirpath, _, filenames in os.walk(root_path):
        for parts_file in [f for f in filenames if f.endswith('.parts')]:
            parts_file_path = os.path.join(dirpath, parts_file)
            parts_timestamp = os.path.getctime(parts_file_path)  # Creation timestamp
            parts_files_data[parts_file_path] = parts_timestamp

    # Search for matching .srt files
    for dirpath, _, filenames in os.walk(root_path):
        for srt_file in [f for f in filenames if f.endswith('.srt')]:
            srt_file_path = os.path.join(dirpath, srt_file)
            srt_timestamp = os.path.getctime(srt_file_path)  # Creation timestamp
            
            # Check against all .parts files timestamps
            for parts_file_path, parts_timestamp in parts_files_data.items():
                if abs(parts_timestamp - srt_timestamp) < 1:  # Using a threshold of 1 second
                    parts_file_name = os.path.basename(parts_file_path)
                    
                    # If .srt is inside "Subs", use the parent directory
                    if os.path.basename(dirpath) == "Subs":
                        matching_folder = os.path.basename(os.path.dirname(dirpath))
                    else:
                        matching_folder = os.path.basename(dirpath)
                    
                    mapping[parts_file_name] = matching_folder

    return mapping

root_folder = r"\\TNT\\Shared Z Drive\\Movies"  # Your network path
file_folder_map = map_parts_to_srt_folders(root_folder)

with open('results.txt', 'w') as f:
    for parts_file, folder in file_folder_map.items():
        f.write(f"{parts_file} -> {folder}\n")
