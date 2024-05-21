from helpers.base_command import ICommand
# import pathlib
from typing import Optional, Union
import os
from helpers.constants import DIR_DEFINITIONS, MAIN_DIR, EXTENSIONS


class Init(ICommand):
    def __init__(self, main_dir_name: Optional[str] = None,
                 extension: Union[EXTENSIONS] = EXTENSIONS.TXT.value,
                 cwd: Optional[str] = None
                 ) -> None:
        self.__main_dir_name = main_dir_name if main_dir_name is not None else MAIN_DIR
        self.__extension = extension
        self.__cwd = cwd if cwd is not None else os.getcwd()

    def _generate_main_dir(self):
        if not os.path.exists(self.__main_dir_name):
            os.mkdir(os.path.join(self.__cwd, self.__main_dir_name))

    def save_state(self):
        """About: it will save the state of init command"""
        pass

    def get_state(self):
        pass

    def _generate_dirs(self):
        for dir_name, dir_content in DIR_DEFINITIONS.items():
            dir_path = os.path.join(self.__main_dir_name, dir_name)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
                with open(os.path.join(dir_path, 'index' + self.__extension), 'w') as file:
                    file.write(dir_content + '\n')

    def run(self):
        try:
            self._generate_main_dir()
            self._generate_dirs()
        except Exception as e:
            raise Exception('Failed to initialize studyate: ' + str(e))
