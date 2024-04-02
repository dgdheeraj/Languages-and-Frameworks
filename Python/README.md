# OOP Python

- Structuring programs such that properties and behaviors are bundles into objects.
- Model Real-world entities as software objects that have data associated with them

## Class

- You can consider class to be a complex data type that can handle info in a managable and maintainable fashion
- Blueprint to create data structures called objects
- Python class names are written in CapitalizedWords notation by convention
- Every Object created will have the following 
    - **State** (attributes of the obj)
    - **Behavior** (methods of an obj)
    - **Identity** (unique name to the obj)

```
class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age
```

## Printing out Objects
Adding a `__str__()` or `__repr__()` method in the class will be invoked whenever object is printed
```
class Test: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
    def __repr__(self): 
        return "Test a:%s b:%s" % (self.a, self.b) 
  
    def __str__(self): 
        return "From str method of Test: a is %s," \ 
              "b is %s" % (self.a, self.b) 
  
t = Test(1234, 5678) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__() 
```

### Attributes
- Instance attributes: Ones created in constructor
- Class attributes: Have the same value for all instances for this class (defined by assigning value to a variable name outside constructor)

```
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```
In this example, species is a class attribute and name, age are instance attributes

Q) Are class attributes shared by all objects?
A) Yes, consider the example below. But instead of changing `Dog.species`, if you change `d.species` or `d1.species`, the species attribute will only change for that object
```
d = Dog("Dog0",5)
d1 = Dog("Dog1",7)
print(d.species, d1.species, Dog.species)
Dog.species = "New species"
print(d.species, d1.species, Dog.species)
```
<b>Ouput:</b>
```
Canis familiaris Canis familiaris Canis familiaris
New species New species New species
```

-  The tricks list in the following code should not be used as a class variable because just a single list would be shared by all Dog instances
```
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

### Access Modifiers
Python does not have access modifiers to hide/protect any attributes. There are a few conventions followed in Python to suggest access modifiers
- For public, `<obj>.<attribute>` 
- For protected, `<obj>._<attribute>`
- For private,  `<obj>.__<attribute>`

Adding two underscores also induces **Name mangling**
Any attribute of the format `__<attribute_name>` is replaces with `_<class name>__<attribute_name>` with leading underscores stripped.
Main reson of Name Mangling is to avoid name clases of names with names defined by subclasses. 
Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls
```
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

### Class Methods vs Static Methods

- Class methods are essentially used to change state of the class (class variables)
- Static Methods are methods which do not access or change the state of the class or an instance
- Python does not have a `static` keyword. Any variable inside a static method is a static variable.

#### Class Methods

```
class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.
```
A class method is a method that is bound to the class and not the object of the class.
It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.

#### Static Methods
```
class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.
```
A static method does not receive an implicit first argument. A static method is also a method that is bound to the class and not the object of the class. This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.

### Constructors
- Default Constructors: Does not take in any arguments
- Parameterized Constructors: Takes in arguments

Constructor Overloading not supported (since Python is dynamically typed, the differentiation cannot happen when python code is being converted to inermediate byte code)

### Destructors
```
# Python program to illustrate destructor
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj
```

## Polymorphism

In general there are two types of polymorphism
- Compile Time Polymorphism (Overloading)
- Run Time Polymorphism (Overriding)

NOTE: Python does not support function overloading [Link Here](https://stackoverflow.com/questions/6434482/python-function-overloading#:~:text=Why%20Not%20Overloading%3F)

Example of inbuilt polymorphic functions
- len()

```
class Bird: 
    def intro(self): 
        print("There are many types of birds.") 
  
    def flight(self): 
        print("Most of the birds can fly but some cannot.") 
  
class sparrow(Bird): 
    def flight(self): 
        print("Sparrows can fly.") 
  
class ostrich(Bird): 
    def flight(self): 
        print("Ostriches cannot fly.") 
```

## Encapsulation

Wrapping data and the methods that work on data within one unit
The data in this case are private variables
```
class Bird: 
    def __init__(self,name): 
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
```

### Inheritance
Ability of a class to derive or inherit characteristics from another class. The class that inherits properties are calles subclasses/dervied class/child class

Why is it needed?
- Provide reusability of code by preventing code duplication
- You can extend a feature by inheritng instead of directly changing an existing feature

Types of Inheritance
- Single: one parent, one child
- Multilevel: Derived class inherits from an intermediate class that in turns inherits from a parent class 
- Hierarchial: One parent class, multiple subclasses
- Multiple: multiple parents, one child

NOTE: Multiple inheritance not supported by Java

```
class Person(object): 
  
    # __init__ is known as the constructor 
    def __init__(self, name, idnumber): 
        self.name = name 
        self.idnumber = idnumber 
  
    def display(self): 
        print(self.name) 
        print(self.idnumber) 
          
    def details(self): 
        print("My name is {}".format(self.name)) 
        print("IdNumber: {}".format(self.idnumber)) 
      
class Employee(Person): 
    def __init__(self, name, idnumber, salary, post): 
        self.salary = salary 
        self.post = post 
  
        # invoking the __init__ of the parent class 
        super().__init__(self, name, idnumber) 
          
    def details(self): 
        print("My name is {}".format(self.name)) 
        print("IdNumber: {}".format(self.idnumber)) 
        print("Post: {}".format(self.post)) 
  
  
a = Employee('Rahul', 886012, 200000, "Intern") 
```

In Python (from version 3. x), the object is the root of all classes. 
- In Python 3.x, `class Test(object)` and `class Test` are same. 
- In Python 2. x, `class Test(object)` creates a class with the object as a parent (called a new-style class), and “class Test” creates an old-style class (without an objecting parent). 

#### Method Resolution Order
In python 2.1 the MRO was Depth First Left to Right (DLR), which uses old style classes
From laster versions (2.2 and 3.x), C3 Linearization Algorithm was used for MRO, and the new style classes are implemented

##### DLR

```
class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(A):
    def rk(self):
        print("In class C")
 
# classes ordering
class D(B, C):
    pass
    
r = D()
r.rk()
```

Was used for old styles classes 

In the above Example algorithm first looks into the instance class for the invoked method. If not present, then it looks into the first parent, if that too is not present then-parent of the parent is looked into. This continues till the end of the depth of class and finally, till the end of inherited classes

The MRO: D, B, A, C, A
but since A can't be there twice, the order is D, B, A, C

But this algorithm varying in different ways and showing different behaviours at different times. Due to this inconsistency, L3 Linearization Algorithm was introduced

#### L3 Linearization

[Link Here for Detailed Explanation](https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc)
Uses new-style classes
Removes inconsistency created by DLR Algorithm

Limitations of L3: 
- Children precede thier parents
- If a class inherits from multiple classes, they are kept in the order specified in the tuple of the base class.

C3 Linearization Algorithm works on three rules: 
- Inheritance graph determines the structure of method resolution order.
- User have to visit the super class only after the method of the local classes are visited.
- Monotonicity

```
class A:
    def rk(self):
        print(" In class A")
class B:
    def rk(self):
        print(" In class B")
class C(A, B):
    def __init__(self):
        print("Constructor C")
 
r = C() 
# it prints the lookup order 
print(C.__mro__)
print(C.mro())
```

In case any ambiguity is there in the MRO, `TypeError: Cannot create a consistent method resolution` is thrown
Example:
```
class A: 
	pass
class B: 
	pass
class C(A, B): 
	pass
class D(B, A): 
	pass
class E(C,D): 
	pass
```
Here, Class E inherits from C and D, both C and D inherit from A and B but in different order, this causes ambiguity

Based on the [link](https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc) here, the MRO would be:
```
O = Object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(D,E): pass
class A(B,C): pass
```

```
L[F] = F O
L[E] = E O
L[D] = D O

L[C] = C + merge(L[D],L[F], D F)
     = C + merge(D O, F O, D F)
     = D + F + O

L[B] = B + merge(L[D],L[E], DE)
     = B + merge(DO, EO, DE) 
     = B + D + E + O

L[A] = A + merge(L[B], L[C], BC)
     = A + merge(BDEO, DFO, BC)
     = A + B + merge(DEO, DFO, C)
     = A + B + C + merge(DEO, DFO)
     = A + B + C + D + merge(EO, FO)
     = A + B + C + D + merge(EO, FO)
     = A + B + C + D + E + F + O
```

# References
- [Python Docs](https://docs.python.org/3/tutorial/classes.html)
- [Real Python](https://realpython.com/python3-object-oriented-programming/#what-is-object-oriented-programming-in-python)
- [Geeksforgeeks](https://www.geeksforgeeks.org/python-oops-concepts/)
- [Geeksforgeeks](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)
- [Geeksforgeeks MRO](https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/)