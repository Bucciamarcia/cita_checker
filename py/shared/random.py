import random
import json


class Random:
    @staticmethod
    def random_number(min: int, max: int) -> int:
        return random.randint(min, max)

    @staticmethod
    def random_name(path: str) -> str:
        with open(path, "r") as f:
            names = json.load(f)
        return random.choice(names)
