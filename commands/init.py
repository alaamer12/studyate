from .base_command import ICommand
import pathlib



class Init(ICommand):
    def __init__(self, name):
        self.__name = None
        self__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def create(self):
        pass

    def run(self):
        pass

    def _generate_content(self, file):
        match file:
            case 'modules.txt':
                return 'python'
            case 'topics.txt':
                return 'python'
            case 'projects.txt':
                return 'python'
            case 'notes.txt':
                return 'python'
            case 'readme.txt':
                return 'python'
            case 'content.txt':
                return 'python'
            case _:
                return 'python'