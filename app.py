from src.git import Git
from src.packages.file_system import FileSystem
from src.packages.counter import Count
from src.packages.input_taker import Input
from src.packages.scheduler import Scheduler
from src.user_config import UserConfig


class CommitsApp:
    def __init__(self, repo_url: str, file_name: str, commits_count: int):
        self.repo_url = repo_url
        self.file_name = file_name
        self.commits_count = commits_count

    def _execute_script(self):
        """
        Cleans leftovers
        Creates a new file with random content
        Forcefully commits the file to repo.

        The logic of the loop:
            While True, try to commit to git
                If it fails remove git folder and try to commit again. Ignore all errors.
                Else, break the loop.
        """
        Git.remove_association()
        FileSystem.create_random_file(filepath=self.file_name)

        while True:
            try:
                while Git.send_to_github(repo_url=self.repo_url) is not True:
                    Git.remove_association()
            except Exception:
                Git.remove_association()
                continue
            else:
                break

    def run(self):
        count = Count()

        while count.__lt__(other=self.commits_count):
            self._execute_script()
            count.increase_by_one()

        count.reset()


if __name__ == '__main__':
    try:
        repo_url, file_name = UserConfig.get("repo_url", "file_name")

        if not repo_url:
            repo_url = Input.take_str(msg="Enter the Github repository URL: ", starts_with="https://github.com/",
                                      ends_with='.git')
            UserConfig.save_data(repo_url=repo_url)

        if not file_name:
            file_name = Input.take_str(msg="Enter the preferred file name: ")
            UserConfig.save_data(file_name=file_name)

        commits_count: int = Input.take_int(msg="How many commits you want to perform?: ")
        repeat_daily: bool = Input.take_str(msg="Do you want to autocommit every day? Y/N: ", to_lower=True) == 'y'

        app = CommitsApp(repo_url=repo_url, file_name=file_name, commits_count=commits_count)

        if repeat_daily:
            time: str = Input.take_str(msg="What time do you want to schedule? (Example: 04:05): ")
            Scheduler.schedule_task(task=app.run, repeat=commits_count, execute_at=time)
        else:
            app.run()
    except Exception as error:
        print(error)
        input('Press any button to exit')

