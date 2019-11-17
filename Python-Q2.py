from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def get_gender(self):
        pass
class Male(Person):
    def get_gender(self):
        print("Male")

class Female(Person):
    def get_gender(self):
        print("Female")
try:
    p1=Person()
except TypeError as e:
    print("Error: ",e)
