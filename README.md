# Project map
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

### Exclude File List
You can also specify an exclude file list by providing a file containing the names of files or folders to exclude. Each name should be on a new line.

1. Create an exclude file (e.g., `exclude.txt`) with the following content:

```sh
folder1
file1.txt
```
2. Run the script with the `--exclude`(`-e`) argument pointing to the exclude file:
```sh
python project-map/scan.py --path path_to_your_project_directory --exclude exclude.txt --output output_file.txt
```

### Print File Content
To include the content of all files, use the `--include-content` (`-c`) flag:

```sh
python project-map/scan.py --path path_to_your_project_directory --exclude folder_to_exclude1 file_to_exclude1 --output output_file.txt --include-content
```
Or using short arguments:
```sh
python project-map/scan.py -p path_to_your_project_directory -e folder_to_exclude1 file_to_exclude1 -o output_file.txt -i
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
with the argument `--include-content`
```
/path/to/your/project/
├── file1.txt
    file1 content
├── folder1
│   ├── file2.txt
        file2 content
├── folder2
│   ├── file3.txt
         file3 content
```