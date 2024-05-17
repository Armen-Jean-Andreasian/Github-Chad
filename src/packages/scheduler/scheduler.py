import schedule
from typing import Callable


class Scheduler:
    """Job scheduler with schedule task method"""
    @staticmethod
    def schedule_task(task: Callable, repeat: int, execute_at: str):
        """
        Main thread blocker method, that schedules and executes the task

        :param task: the function that's needed to be executed
        :param repeat: how many times to execute
        :param execute_at: time in 'HH:SS' 24-h format.
        """
        schedule.every().day.at(execute_at).do(task, repeat=repeat)
        while True:
            schedule.run_pending()
