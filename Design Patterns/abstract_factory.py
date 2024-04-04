from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def createCar(self):
        pass

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Truck(Car):
    def drive(self):
        print("Truck is Driving!")

class Sedan(Car):
    def drive(self):
        print("Sedan is driving!")

class NAFactory(Factory):
    def createCar(self):
        return Sedan()

class EUFactory(Factory):
    def createCar(self):
        return Truck()

class Client:
    def __init__(self):
        # This factory is to be picked by config file or config of application
        self.factory = NAFactory()

    def getCar(self):
        car = self.factory.createCar()
        car.drive()
        return car

factory1 = NAFactory()
factory2 = EUFactory()
client1 = Client()
client1.getCar()