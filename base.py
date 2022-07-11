from abc import ABC, abstractclassmethod

class Process(ABC):

    @abstractclassmethod
    def __init__(self, files) -> None:
        return None

    @abstractclassmethod
    def open_files(self) -> str:
        return

    @abstractclassmethod
    def process_file(self) -> str:
        return
    
    @abstractclassmethod
    def process_seventy(self) -> str:
        return

    @abstractclassmethod
    def sorted_files(self)-> str:
        return