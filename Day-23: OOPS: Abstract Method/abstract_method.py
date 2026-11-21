from abc import abstractmethod, ABC

# Abstraction: Hide implementation, but show only necessary details.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("my abstract method")
        
    def show(self):
        print("This is my parent method")    
    
    
class Car(Vehicle):
    def start(self):
        print("This is my car method")


c = Car()
c.show()
c.start()    
