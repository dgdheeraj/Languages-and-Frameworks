from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        print("Dog sound!")

d = Dog()
d.makeSound()
