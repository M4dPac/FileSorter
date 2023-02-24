import os
import shutil

# Set up inner and outer paths
FOLDER_PATH = 'C:/files'  # Our folder with files to sort
OUTER_PATH = 'C:/sort_files'  # The folder in which our categories will be created
OTHER = 'Other'  # For unknown extensions

# Dict of extensions and corresponding folders
EXTENSIONS = {
    'Documents': ('.txt', '.doc', '.docx', '.xls', '.xlsx', '.pdf'),
    'Photos': ('.jpg', '.jpeg', '.png', '.gif'),
    'Videos': ('.avi', '.mp4', '.mkv'),
    'Music': ('.mp3', '.wav'),
    'Archives': ('.rar', '.zip', '.7zip'),
    'Programs': ('.exe', '.msi'),
    '3D_print': ('.stl',),
    'Torrent_files': ('.torrent',)
}


# Create directories
def make_directory() -> None:
    '''Create folders if they don't exist'''
    for folder in EXTENSIONS.keys():
        folder_path = os.path.join(OUTER_PATH, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


# Check directories
def check_directory(extension: str) -> str:
    '''Find extension in EXTENSIONS and return folder'''
    for k, v in EXTENSIONS.items():
        if extension in v:
            return k
    return OTHER


if __name__ == '__main__':
    make_directory()

    # Get list of files in the monitored folder
    files = os.listdir(FOLDER_PATH)
    for file_name in files:
        # Full path to file
        file_path = os.path.join(FOLDER_PATH, file_name)

        # Get file extension
        extension = os.path.splitext(file_name)[1]

        if extension:  # If it's a folder or there is no extension, do nothing
            # Get folder name by extension
            folder_name = check_directory(extension)
            folder_path = os.path.join(OUTER_PATH, folder_name)
            # Move file to folder
            shutil.move(file_path, folder_path)
