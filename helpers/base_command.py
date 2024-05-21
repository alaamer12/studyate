from abc import abstractmethod, ABC

class ICommand(ABC):
    @abstractmethod
    def run(self):
        pass