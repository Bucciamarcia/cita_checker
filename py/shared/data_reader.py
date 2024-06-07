import json


class DataReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        with open(self.file_path, "r") as file:
            return json.load(file)
