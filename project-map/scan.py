import os
import argparse


def scan_directory(directory, exclude_folders=None, indent=0, output_lines=None):
    if exclude_folders is None:
        exclude_folders = []
    if output_lines is None:
        output_lines = []

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if item in exclude_folders:
            continue
        line = ' ' * indent + '├── ' + item
        print(line)
        output_lines.append(line)
        if os.path.isdir(item_path):
            scan_directory(item_path, exclude_folders,
                           indent + 4, output_lines)

    return output_lines


def main():
    parser = argparse.ArgumentParser(
        description="Scan a project directory and output its hierarchy.")
    parser.add_argument('--path', '-p', type=str, required=True,
                        help="The path to the project directory.")
    parser.add_argument('--exclude', '-e', nargs='*', default=[],
                        help="List of folder names to exclude.")
    parser.add_argument('--output', '-o', type=str, default='output.txt',
                        help="The file to save the output (default: output.txt).")

    args = parser.parse_args()

    project_dir = args.path
    exclude_folders = args.exclude
    output_file = args.output

    if os.path.exists(project_dir) and os.path.isdir(project_dir):
        print(project_dir + '/')
        output_lines = [project_dir + '/']
        output_lines.extend(scan_directory(project_dir, exclude_folders))
        with open(output_file, 'w') as f:
            f.write('\n'.join(output_lines))
    else:
        print(
            f"The directory {project_dir} does not exist or is not a directory.")


if __name__ == "__main__":
    main()
