from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def fly(self):
        pass


class SecondClass(AbstractClass):

    def fly(self):
        print("fly fly")


SecondClass()
