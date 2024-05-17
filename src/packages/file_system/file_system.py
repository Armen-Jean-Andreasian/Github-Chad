import os
import random
import shutil
import datetime
from typing import Optional


class FileSystem:
    """Implementation of file system with create_file, remove file and create_random_file methods"""
    @staticmethod
    def create_file(file_path: str, file_content: Optional[str] = ""):
        """Creates a blank file"""
        with open(file_path, "w") as file:
            file.write(file_content)

    @staticmethod
    def remove_folder(folder_path: str):
        """Recursively delete a directory tree by force."""
        shutil.rmtree(path=os.path.join(folder_path), ignore_errors=True)
        return True

    @classmethod
    def create_random_file(cls, filepath: str):
        """Creates a file with unique content"""
        unique_content = str(random.randint(1, 10000)) + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        return cls.create_file(file_path=filepath, file_content=unique_content)
