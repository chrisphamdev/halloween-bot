import sqlite3
import time
import datetime
from pathlib import Path


def adapt_datetime(ts):
    return time.mktime(ts.timetuple())


class DatabaseConnection:

    def __init__(self):
        self.database_folder_path = Path.cwd().joinpath('database')
        self.database_file_path = self.database_folder_path.joinpath('user_data.db')
        self.connection = None
        self.cursor = None

    def initialise_connection(self) -> None:
        if self.connection is None:
            try:
                # TODO add logging here.
                self.connection = sqlite3.connect(self.database_file_path, detect_types=sqlite3.PARSE_DECLTYPES)
                sqlite3.register_adapter(datetime.datetime, adapt_datetime)
                self.cursor = self.connection.cursor()
            except sqlite3.Error as e:
                print(str(e).upper())

    def close_connection(self) -> None:
        self.connection.close()

    def has_connection(self) -> bool:
        if self.connection:
            return True
        else:
            return False

