import shutil
import argparse
from pathlib import Path
import os

def copy_directory_contents(src, dest):
    create_destination_dir(dest)
    process_directory_contents(src, dest)


def create_destination_dir(destination):
    if not destination.exists():
        print("Destination folder was created in the current directory")
        destination.mkdir()


def process_directory_contents(source, destination):
    for item in source.iterdir():
        if item.is_dir():
            copy_directory_contents(item, destination)
        else:
            process_file_item(item, destination)


def process_file_item(file_path, destination):
    if can_access_file(file_path):
        folder_for_extension = get_or_create_extension_folder(file_path, destination)
        if folder_for_extension:
            destination_path = get_unique_destination_path(file_path, folder_for_extension)
            shutil.copy(file_path, destination_path)


def get_or_create_extension_folder(file_path, destination):
    extension = file_path.suffix.lower().lstrip('.')
    if extension:
        folder_path = destination.joinpath(extension)
        folder_path.mkdir(exist_ok=True)
        return folder_path
    return None


def can_access_file(file_path):
    try:
        return os.access(file_path, os.R_OK | os.W_OK | os.X_OK)
    except Exception as e:
        print(f"No access rights: {e}")
        return False


def get_unique_destination_path(file_path, destination_folder):
    base_name = file_path.stem
    extension = file_path.suffix
    unique_path = destination_folder.joinpath(f"{base_name}{extension}")

    counter = 1
    while unique_path.exists():
        unique_path = destination_folder.joinpath(f"{base_name}_copy_{counter}{extension}")
        counter += 1

    return unique_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Copy Utility")
    parser.add_argument("--source", type=Path, default=Path.cwd(), help="Source directory path")
    parser.add_argument("--destination", type=Path, default=Path("./dist"), help="Destination directory path")

    args = parser.parse_args()

    copy_directory_contents(args.source, args.destination)
    print("File copying process completed")