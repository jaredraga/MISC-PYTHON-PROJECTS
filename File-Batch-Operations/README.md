# File Batch Operations

> **Note**: This project is from 2018 and is preserved here as a showcase of early programming work. It demonstrates file system automation and batch processing capabilities.

A collection of Python scripts for performing batch operations on files and directories.

## Features
- **File Counting**: Quickly counts the number of files and directories in a specified location.
- **Batch File Creation**: Creates multiple files with specified names and types based on user input.
- **File Deletion**: Deletes files and directories based on user-defined keywords, ensuring confirmation before deletion.
- **File Moving**: Moves files that contain specified keywords to a designated directory.
- **File Renaming**: Renames files and directories based on user-defined rules, including random naming options.

## Functionality
1. **massCount.py**: Counts the number of files and directories in the current directory and prints the totals.
2. **massCreate.py**: Creates a specified number of files with a given title and file type, allowing for batch creation of files.
3. **massDelete.py**: Deletes all files and directories that contain a specified keyword in their names after user confirmation.
4. **massMove.py**: Moves files containing a specified keyword to a designated directory, which must already exist.
5. **massRename.py**: Renames files and directories that contain a specified keyword, adding a number to the new name based on user input.
6. **massRenameRandomName.py**: Renames files and directories containing a specified keyword to a random string of characters, ensuring unique names.
7. **massSimpleRename.py**: Allows for simple renaming of files and directories with a specified title, adding a number to the new name.

## Installation and Setup
1. Ensure you have Python 3 installed on your system.
2. Clone the repository or download the scripts.
3. Navigate to the directory containing the scripts.

## Usage Examples
- To count files and directories:
  ```bash
  python massCount.py
  ```
- To create files:
  ```bash
  python massCreate.py --title example --count 5 --type txt
  ```
- To delete files:
  ```bash
  python massDelete.py --keyword example
  ```
- To move files:
  ```bash
  python massMove.py --keyword example --destination /path/to/destination
  ```
- To rename files:
  ```bash
  python massRename.py --keyword example --newtitle newname
  ```

## Author

Jared I. Raga 2018
