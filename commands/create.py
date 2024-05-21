import os
from helpers.reader import block_reader
from helpers.base_command import ICommand
from helpers.constants import DIR_DEFINITIONS
from .init import Init

class Create(ICommand):
    def __init__(self, path: str, entry_point_file: str = "index.txt", strict: bool = True):
        self.__path = path
        self.__entry_point_file = entry_point_file
        self.__strict = strict
    def init(self):
        Init(cwd=self.__path).run()

    def _strict_path_valid(self):
        if not os.path.exists(self.__path) or os.path.isfile(self.__path):
            raise Exception(f"Invalid path: {self.__path}")
        if self.__strict:
            for dir in DIR_DEFINITIONS:
                if not os.path.exists(os.path.join(self.__path, dir)):
                    raise Exception(f"Invalid path: {self.__path}")
        return True



    def run(self):
        if self._strict_path_valid():
            try:
                for dir in DIR_DEFINITIONS:
                    blocks = block_reader(os.path.join(self.__path, dir, self.__entry_point_file))
                    for block_file, block_content in blocks.items():
                        with open(os.path.join(self.__path, dir, block_file + '.txt'), 'w') as file:
                            file.write(block_content + '\n')
            except Exception as e:
                raise Exception('Failed to create studyate: ' + str(e))
        if not self.__strict:
            raise NotImplementedError
        raise Exception('Failed to create studyate')
