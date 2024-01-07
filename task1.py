import os
import shutil
import argparse

def copy_files(src, dest, root_dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_files(s, d, root_dest)  
        else:
            try:
                ext = os.path.splitext(item)[1][1:] 
                final_directory = os.path.join(root_dest, ext)  
                if not os.path.exists(final_directory):
                    os.makedirs(final_directory)
                shutil.copy(s, os.path.join(final_directory, item))
            except IOError as e:
                print(f"Unable to copy due to an IO error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Copy files into new directory sorted by file extension.")
    parser.add_argument('src', type=str, help="Source directory path")
    parser.add_argument('dest', type=str, nargs='?', default="dist", help="Destination directory path (default: dist)")
    
    args = parser.parse_args()

    if not os.path.exists(args.src):
        print("Error: Source directory does not exist.")
        return
    
    try:
        copy_files(args.src, args.dest, args.dest)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()