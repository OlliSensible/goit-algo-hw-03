import os
import shutil
import argparse

def copy_files(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_files(s, d)
        else:
            ext = os.path.splitext(item)[1][1:] 
            final_directory = os.path.join(dest, ext)
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)
            shutil.copy(s, os.path.join(final_directory, item))

def main():
    parser = argparse.ArgumentParser(description="Copy files into new directory sorted by file extension.")
    parser.add_argument('src', type=str, help="Source directory path")
    parser.add_argument('dest', type=str, nargs='?', default="dist", help="Destination directory path (default: dist)")
    
    args = parser.parse_args()

    if not os.path.exists(args.src):
        print("Error: Source directory does not exist.")
        return

    copy_files(args.src, args.dest)

if __name__ == "__main__":
    main()
