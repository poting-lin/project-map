import os
import argparse


def scan_directory(directory, exclude_folders=None, indent=0):
    if exclude_folders is None:
        exclude_folders = []

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if item in exclude_folders:
            continue
        print(' ' * indent + '├── ' + item)
        if os.path.isdir(item_path):
            scan_directory(item_path, exclude_folders, indent + 4)


def main():
    parser = argparse.ArgumentParser(
        description="Scan a project directory and output its hierarchy.")
    parser.add_argument('--path', type=str, required=True,
                        help="The path to the project directory.")
    parser.add_argument('--exclude', nargs='*', default=[],
                        help="List of folder names to exclude.")

    args = parser.parse_args()

    project_dir = args.path
    exclude_folders = args.exclude

    if os.path.exists(project_dir) and os.path.isdir(project_dir):
        print(project_dir + '/')
        scan_directory(project_dir, exclude_folders)
    else:
        print(
            f"The directory {project_dir} does not exist or is not a directory.")


if __name__ == "__main__":
    main()
