import os
from helpers.base_command import ICommand
from helpers.reader import block_reader


class ThisFile(ICommand):
    def __init__(self, file_path: str, out_dir: str = "out", extension: str = ".txt"):
        self.__file_path = file_path
        self.__out_dir = out_dir
        self.__extension = extension

    def _validate_path(self):
        return os.path.exists(self.__file_path) and os.path.isfile(self.__file_path) and not os.path.islink(self.__file_path)

    def run(self):
        if self._validate_path():
            blocks = block_reader(self.__file_path)
            try:
                if not os.path.exists(self.__out_dir):
                    os.mkdir(self.__out_dir)
                for block_file, block_content in blocks.items():
                    with open(os.path.join(self.__out_dir, block_file + self.__extension), 'w') as file:
                        file.write(block_content + '\n')
            except Exception as e:
                raise Exception('Failed to create studyate: ' + str(e))
        raise Exception('Path does not exist or is not a file')
