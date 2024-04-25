import os
import shutil
import argparse


def copy_files_recursively(source, target):
    # Ensure the target directory exists
    os.makedirs(target, exist_ok=True)

    # Recursively walk through the source directory
    for root, dirs, files in os.walk(source):
        for file in files:
            # Full path of the source file
            source_file_path = os.path.join(root, file)
            # Determine file extension or use 'no_extension' if none
            extension = os.path.splitext(file)[1][1:] or 'no_extension'
            # Define the target subdirectory based on the file extension
            target_subdir = os.path.join(target, extension)
            # Ensure the target subdirectory exists
            os.makedirs(target_subdir, exist_ok=True)
            # Target file path
            target_file_path = os.path.join(target_subdir, file)

            # Copy the file to the target directory
            shutil.copy2(source_file_path, target_file_path)
            print(f"File {file} copied to {target_subdir}")


def main():
    parser = argparse.ArgumentParser(
        description="Copy files recursively and sort them by extension into subdirectories.")
    parser.add_argument("source_directory", type=str, help="Path to the source directory")
    parser.add_argument("target_directory", type=str, nargs='?', default="dist",
                        help="Path to the target directory (default: 'dist')")

    args = parser.parse_args()

    # Copy files recursively from source to target
    copy_files_recursively(args.source_directory, args.target_directory)


if __name__ == "__main__":
    main()