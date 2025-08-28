# 代码生成时间: 2025-08-28 13:41:27
import os
import re
from pathlib import Path

"""
A batch file rename tool using Python and the pathlib module.
"""

class BatchRenameTool:
    def __init__(self, directory):
        """
        Initialize the BatchRenameTool with a directory path.
        :param directory: Path to the directory containing files to rename.
        """
        self.directory = Path(directory)

    def rename_files(self, prefix):
        """
        Rename files in the directory with a specified prefix.
        :param prefix: Prefix to append to the file name.
        """
        if not self.directory.exists() or not self.directory.is_dir():
            raise ValueError(f"The directory {self.directory} does not exist.")

        for file in self.directory.iterdir():
            if file.is_file():
                original_name = file.name
                # Append the prefix to the original file name and keep the extension
                new_name = f"{prefix}{original_name}"
                # Construct full path for the new file name
                new_file_path = self.directory / new_name
                # Rename the file
                file.rename(new_file_path)
                print(f"Renamed {original_name} to {new_name}")

def main():
    """
    Main function to perform batch renaming of files.
    """
    # Define the directory containing files to rename and the prefix
    directory_path = "/path/to/directory"
    prefix_to_add = "new_"

    try:
        # Create an instance of BatchRenameTool
        rename_tool = BatchRenameTool(directory_path)
        # Rename files with the specified prefix
        rename_tool.rename_files(prefix_to_add)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()