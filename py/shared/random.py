import random
import json


class Random:
    @staticmethod
    def random_number(min: int, max: int) -> int:
        return random.randint(min, max)

    def random_name(self, path: str) -> str:
        with open(path, "r") as f:
            names = json.load(f)
        return random.choice(names)
