from time import sleep
from datetime import datetime, time
import random


class TimeChecker:
    @staticmethod
    def random_sleep(min: float = 1, max: float = 5):
        sleep(random.uniform(min, max))

    @staticmethod
    def is_within_time(start_time: time, end_time: time) -> bool:
        current_time = datetime.now().time()
        return start_time <= current_time <= end_time

    @staticmethod
    def wait_until_time(target_time: time):
        while True:
            if datetime.now().time() >= target_time:
                break
            sleep(60)
        return
