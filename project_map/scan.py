import os
import argparse


def scan_directory(directory, exclude_items=None, indent=0, output_lines=None, print_content=False):
    if exclude_items is None:
        exclude_items = []
    if output_lines is None:
        output_lines = []

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if item_path in exclude_items or item in exclude_items:
            continue
        line = ' ' * indent + '├── ' + item
        print(line)
        output_lines.append(line)
        if os.path.isdir(item_path):
            scan_directory(item_path, exclude_items, indent +
                           4, output_lines, print_content)
        elif print_content and os.path.isfile(item_path):
            try:
                with open(item_path, 'r') as file:
                    content = file.read()
                    content_lines = content.splitlines()
                    for content_line in content_lines:
                        content_line_indented = ' ' * \
                            (indent + 4) + content_line
                        print(content_line_indented)
                        output_lines.append(content_line_indented)
            except Exception as e:
                error_line = ' ' * (indent + 4) + f"[Error reading file: {e}]"
                print(error_line)
                output_lines.append(error_line)

    return output_lines


def read_exclude_file(exclude_file):
    exclude_items = []
    if os.path.exists(exclude_file):
        with open(exclude_file, 'r') as file:
            exclude_items = [line.strip() for line in file if line.strip()]
    return exclude_items


def main():
    parser = argparse.ArgumentParser(
        description="Scan a project directory and output its hierarchy.")
    parser.add_argument('--path', '-p', type=str, required=True,
                        help="The path to the project directory.")
    parser.add_argument('--exclude', '-e', nargs='*', default=[],
                        help="List of files or folders to exclude, or a file containing a list of files/folders to exclude.")
    parser.add_argument('--output', '-o', type=str, default='output.txt',
                        help="The file to save the output (default: output.txt).")
    parser.add_argument('--include-content', '-i', action='store_true',
                        help="Print the content of all files.")

    args = parser.parse_args()

    project_dir = args.path
    exclude_items = []

    # Check if the exclude argument is a file with an extension
    if args.exclude:
        if len(args.exclude) == 1 and os.path.isfile(args.exclude[0]) and '.' in args.exclude[0]:
            exclude_items = read_exclude_file(args.exclude[0])
        else:
            exclude_items = args.exclude

    output_file = args.output
    include_content = args.include_content

    if os.path.exists(project_dir) and os.path.isdir(project_dir):
        print(project_dir + '/')
        output_lines = [project_dir + '/']
        output_lines.extend(scan_directory(
            project_dir, exclude_items, print_content=include_content))
        with open(output_file, 'w') as f:
            f.write('\n'.join(output_lines))
    else:
        print(
            f"The directory {project_dir} does not exist or is not a directory.")


if __name__ == "__main__":
    main()
