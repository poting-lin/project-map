# Project-map
A Python script to scan and visualize the directory structure of a project, with options to exclude specific folders.


## Features
- Scans and prints the directory hierarchy of a specified project.
- Allows exclusion of specific folders from the output.
- Simple command-line interface.
- Saves the output to a text file.

## Installation
Clone the repository:
```sh
git clone https://github.com/poting-lin/project-map.git
cd project-map
```

## Usage
Run the script using the following command:

```sh
python project-map/scan.py --path path_to_your_project_directory --exclude folder_to_exclude1 folder_to_exclude2 --output output_file.txt
```

Or using short arguments:
```sh
python project-map/scan.py -p path_to_your_project_directory -e folder_to_exclude1 folder_to_exclude2 -o output_file.txt
```

### Output
The script will print the directory hierarchy in a tree-like format. For example:

```
/path/to/your/project/
├── file1.txt
├── folder1
│   ├── file2.txt
├── folder2
│   ├── file3.txt
```