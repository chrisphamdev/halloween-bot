"""
    This class removes the repetition for access and writing JSON files.
"""

from typing import Union, List, Dict

import json


class JsonHelper:

    @staticmethod
    def json_write(filepath: str, obj):
        with open(filepath, 'w') as file_input:
            json.dump(obj, file_input, indent=4)

    @staticmethod
    def json_read(filepath: str) -> Union[List, Dict]:
        with open(filepath, 'r') as file_output:
            result = json.load(file_output)
            return result
