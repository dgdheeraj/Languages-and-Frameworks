# Design Patterns
Design patterns are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code.

- Design patterns are a toolkit of tried and tested solutions to common problems in software design.
- Design patterns define a common language that you and your teammates can use to communicate more efficiently. You can say, “Oh, just use a Singleton for that,” and everyone will understand the idea behind your suggestion. No need to explain what a singleton is if you know the pattern and its name

## Classification of Patterns
- `Creational patterns` provide object creation mechanisms that increase flexibility and reuse of existing code.
- `Structural patterns` explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.
- `Behavioral patterns` take care of effective communication and the assignment of responsibilities between objects.

## Singleton (Creational)
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

Example Use Case: A front end code uses a Singleton object to make network calls to the backend or any external APIs.
```
class Singleton:
    instance = None
    def __init__(self):
        if Singleton.instance:
            raise NotImplementedError("This class cannot be instantiated directly. Use a getInstance method instead.")
        Singleton.instance = self
        
    @classmethod
    def getInstance(cls):
        if not cls.instance:
            cls.instance = Singleton()
        return cls.instance
```

## Factory (Creational)
Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

Example: A car factory creates cars. There are two types of factories, North America and Europe, which has different kinds of cars generating, one generates trucks, other sedans.
```
class Car:
    def drive(self):
        raise NotImplementedError("drive() method must be implemented by subclasses")

class Truck(Car):
    def drive(self):
        print("Truck is being driven")

class Sedan(Car):
    def drive(self):
        print("Sedan is being driven")

class CarFactory:
    def create_car(self):
        raise NotImplementedError("create_car() method must be implemented by subclasses")

class NorthAmericaFactory(CarFactory):
    def create_car(self):
        return Truck()

class EuropeFactory(CarFactory):
    def create_car(self):
        return Sedan()

na_factory = NorthAmericaFactory()
europe_factory = EuropeFactory()

car1 = na_factory.create_car()
car1.drive()  # Output: Truck is being driven

car2 = europe_factory.create_car()
car2.drive()  # Output: Sedan is being driven
```

## Observer (Behavorial)
Observer allows defining a subscription mechanism to notify multiple objects if an event takes place in the object they're observing.

eg: Publisher maintains a list of users associated to it. As soon as the publisher gets hold of a new book, it will notify all users about the new book.

# References
- [Refactoring Guru](https://refactoring.guru/design-patterns)
- [Factory](https://refactoring.guru/design-patterns/factory-method)
- [Obersver](https://refactoring.guru/design-patterns/observer)