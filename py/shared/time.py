from time import sleep
import random


class Time:
    @staticmethod
    def random_sleep(min: float = 1, max: float = 5):
        sleep(random.uniform(min, max))
