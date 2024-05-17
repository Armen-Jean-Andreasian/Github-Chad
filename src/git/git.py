from src.packages.file_system import FileSystem
from src.packages.terminal import Terminal
import os


class Git:
    @staticmethod
    def send_to_github(repo_url: str) -> bool:
        """The method does what it has to do."""
        if Terminal.run_command(command='git init'):
            if Terminal.run_command(command=f"git remote add origin {repo_url}"):
                if Terminal.run_command(command=f"git config commit.gpgsign false"):
                    if Terminal.run_command(command='git add .'):
                        if Terminal.run_command(command='git commit -m "Dummy commit"'):
                            if Terminal.run_command(command='git push origin master --force'):
                                return True

    @staticmethod
    def remove_association() -> bool:
        FileSystem.remove_folder(folder_path=os.path.join(os.curdir, '.git'))
        return True
