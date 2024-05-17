import os.path

from src.packages.json_handler import Json
from typing import Any


class UserConfig:
    _empty_json_content = {"repo_url": None, "file_name": None, "execute_at": None, "repeat": None}
    _json_filepath = os.path.join(os.curdir, 'src', 'user_config', 'config.json')
    print(os.getcwd())

    @classmethod
    def set_new_json_path(cls, filepath: str):
        if os.path.exists(filepath):
            cls._json_filepath = filepath

    @classmethod
    def get_all_data(cls) -> dict:
        return Json.read(filepath=cls._json_filepath)

    @classmethod
    def get(cls, *keys: str, key: str = None) -> Any | None:
        user_data = cls.get_all_data()

        if key:
            return user_data.get(key)

        elif keys:
            result = list()
            for key in keys:
                result.append(user_data.get(key))
            return result

    @classmethod
    def save_data(cls, **data):
        user_config = Json.read(filepath=cls._json_filepath)

        for key, value in data.items():
            user_config[key] = value

        try:
            Json.write(filepath=cls._json_filepath, content=user_config)
        except Exception as err:
            Json.write(filepath=cls._json_filepath, content=cls._empty_json_content)
            raise err
