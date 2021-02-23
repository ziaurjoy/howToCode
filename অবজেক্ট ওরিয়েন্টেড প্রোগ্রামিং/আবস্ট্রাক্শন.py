

from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def do_study(self):
        pass

class Child(Father):
    def __init__(self, name):
        self.name = name

    def child_name(self):
        print(self.name)

    def do_study(self):     # Must be use
        print('Yes Father')

child1 = Child('Joy')
child1.child_name()
child1.do_study()