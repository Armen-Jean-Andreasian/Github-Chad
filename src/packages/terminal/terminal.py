import subprocess


class Terminal:
    """Terminal with run command method"""
    @staticmethod
    def run_command(command: str):
        """Returns True if the command is executed."""
        subprocess.run(command)
        return True
