from .base_command import ICommand
import pathlib

FILES = ['modules.txt', 'topics.txt', 'projects.txt', 'notes.txt', 'readme.txt', 'content.txt']
CONTENTS = ["""
// Use this file to store your notes about programming language modules
// There are many types of modules, and they are depending on what u want to learn and what u 
// want to reach
// so in this modules.txt file i have provided u with the modules that makes u hard-rock
// in python in general , the modules i have provided are covering different topics
// starting from binary to AI tools [i have included simple AI tools so u can just take a peek
// to AI, i have not said to be data science analyst
// Also i have not cover all the libraries that would exist in the world, but i gave u a look
// of what they are
]

""", '', '', '', '', '']

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