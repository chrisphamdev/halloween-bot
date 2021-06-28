import pathlib
from pathlib import Path

from helper.JsonHelper import JsonHelper


class ConfigHelper:
    """
    This class initialises the config object that handles the config.json.
    """

    def __init__(self):

        self.config_filepath = pathlib.Path.cwd() / 'config' / 'config.json'

        self._role_id = None
        self._role_message_id = None
        self._category_id = None
        self._info_channel_id = None
        self._boss_channel_id = None
        self._hunting_channel_id = None
        self._shop_channel_id = None

        # Check if the config.json is present. Pathlib is used to make file path manipulation os agnostic.
        config_path = Path(self.config_filepath)
        # If the file is not present, it'll create the file.
        if not config_path.exists():
            self.write_to_file()
        else:
            # If a file is detected, it'll load data to memory.
            self.load_from_file()

    @property
    def role_id(self) -> int:
        return self._role_id

    @role_id.setter
    def role_id(self, new_role_id: int) -> None:
        self._role_id = new_role_id
        self.write_to_file()

    @role_id.deleter
    def role_id(self) -> None:
        self._role_id = None
        self.write_to_file()

    @property
    def role_message_id(self) -> int:
        return self._role_message_id

    @role_message_id.setter
    def role_message_id(self, new_role_message_id: int) -> None:
        self._role_message_id = new_role_message_id
        self.write_to_file()

    @role_message_id.deleter
    def role_message_id(self) -> None:
        self._role_message_id = None
        self.write_to_file()

    @property
    def category_id(self) -> int:
        return self._category_id

    @category_id.setter
    def category_id(self, new_category_id: int) -> None:
        self._category_id = new_category_id
        self.write_to_file()

    @category_id.deleter
    def category_id(self) -> None:
        self._category_id = None
        self.write_to_file()

    @property
    def info_channel_id(self) -> int:
        return self._info_channel_id

    @info_channel_id.setter
    def info_channel_id(self, new_info_channel_id: int) -> None:
        self._info_channel_id = new_info_channel_id
        self.write_to_file()

    @info_channel_id.deleter
    def info_channel_id(self) -> None:
        self._info_channel_id = None
        self.write_to_file()

    @property
    def boss_channel_id(self) -> int:
        return self._boss_channel_id

    @boss_channel_id.setter
    def boss_channel_id(self, new_boss_channel_id: int) -> None:
        self._boss_channel_id = new_boss_channel_id
        self.write_to_file()

    @boss_channel_id.deleter
    def boss_channel_id(self) -> None:
        self._boss_channel_id = None
        self.write_to_file()

    @property
    def hunting_channel_id(self) -> int:
        return self._hunting_channel_id

    @hunting_channel_id.setter
    def hunting_channel_id(self, new_hunting_ground_id: int) -> None:
        self._hunting_channel_id = new_hunting_ground_id
        self.write_to_file()

    @hunting_channel_id.deleter
    def hunting_channel_id(self) -> None:
        self._hunting_channel_id = None
        self.write_to_file()

    @property
    def shop_channel_id(self) -> int:
        return self._shop_channel_id

    @shop_channel_id.setter
    def shop_channel_id(self, new_shop_channel_id) -> None:
        self._shop_channel_id = new_shop_channel_id
        self.write_to_file()

    @shop_channel_id.deleter
    def shop_channel_id(self) -> None:
        self._shop_channel_id = None
        self.write_to_file()

    def write_to_file(self) -> None:
        dict_to_save = {
            'role_id': self._role_id,
            'role_message_id': self._role_message_id,
            'category_id': self._category_id,
            'info_channel_id': self._info_channel_id,
            'boss_channel_id': self._boss_channel_id,
            'hunting_channel_id': self._hunting_channel_id,
            'shop_channel_id': self._shop_channel_id
        }
        JsonHelper.json_write(str(self.config_filepath), dict_to_save)

    def load_from_file(self) -> None:
        config_dict = JsonHelper.json_read(str(self.config_filepath))

        self._role_id = config_dict['role_id']
        self._role_message_id = config_dict['role_message_id']
        self._category_id = config_dict['category_id']
        self._info_channel_id = config_dict['info_channel_id']
        self._boss_channel_id = config_dict['boss_channel_id']
        self._hunting_channel_id = config_dict['hunting_channel_id']
        self._shop_channel_id = config_dict['shop_channel_id']

    def __str__(self):
        return 'List of Stored IDs:' \
            f'\n Role ID: {self._role_id}' \
            f'\n Role Message ID: {self._role_message_id}' \
            f'\n Category ID: {self._category_id}' \
            f'\n Info Channel ID: {self._info_channel_id}' \
            f'\n Boss Channel ID: {self._boss_channel_id}' \
            f'\n Hunting Channel ID: {self.hunting_channel_id}' \
            f'\n Shop Channel ID: {self.shop_channel_id}'
