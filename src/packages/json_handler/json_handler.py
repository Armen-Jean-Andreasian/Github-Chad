import json



class Json:
    """Json handler with read and write methods"""
    @staticmethod
    def read(filepath: str) -> dict:
        with open(filepath, 'r') as json_file:
            return json.load(json_file)

    @staticmethod
    def write(filepath: str, content: dict) -> None:
        with open(filepath, 'w') as json_file:
            json.dump(content, json_file, indent=4)
