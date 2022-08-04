OOP
===============

**Overview of OOP Terminology**

- **Class** − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

- **Class variable** − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.

- **Data member** − A class variable or instance variable that holds data associated with a class and its objects.

- **Function overloading** − The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.

- **Instance variable** − A variable that is defined inside a method and belongs only to the current instance of a class.

- **Inheritance** − The transfer of the characteristics of a class to other classes that are derived from it.

- **Instance** − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

- **Instantiation** − The creation of an instance of a class.

- **Method** − A special kind of function that is defined in a class definition.

- **Object** − A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.

- **Operator overloading** − The assignment of more than one function to a particular operator.

PRINCIPLES OOP
===============

#*Inheritance*

**Inheritance**: A class can get the properties and variables of another class. This class is called the super class or parent class.

Inheritance saves you from repeating yourself (in coding: don't repeat yourself), you can define methods once and use
them in one or more subclasses.

**Types of Inheritance** 

**Single Inheritance:**
Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.

**Multilevel Inheritance:**
Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn
inherits properties from his parent class.

**Hierarchical Inheritance:**
Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.

**Multiple Inheritance:**
Multiple level inheritance enables one derived class to inherit properties from more than one base class.

# *Polymorphism*

Polymorphism simply means having many forms. It refers to the use of a single type entity (method, operator or object)
to represent different types in different scenarios.For example, we need to determine if the given species of birds fly or not,
using polymorphism we can do this using a single function.

# *Encapsulation*
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping
data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods
directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable
can only be changed by an object’s method. Those types of variables are known as **private variables**.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

- **Protected members:**

Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be
accessed from within the class and its subclasses. To accomplish this in Python, just follow **the convention** by prefixing
the name of the member by a single underscore “_”.

Although the protected variable can be accessed out of the class as well as in the derived class(modified too in derived
class), it is customary(convention not a rule) to not access the protected out the class body.

```
class Person:
    def __init__(self, name, age):
        self._name = name # protected 
        self._age  = age  # protected 
```

- **Private members**

Private members are similar to protected members, the difference is that the class members declared private should
neither be accessed outside the class nor by any base class. In Python, there is no existence of **Private** instance
variables that cannot be accessed except inside a class.

However, to define a private member prefix the member name with double underscore “__”.

```
class Person:
    def __init__(self, name, age):
        self.__name = name # private
        self.__age  = age  # private
```

The __name and __age instance variables cannot be accessed outside the class, doing so will give an AttributeError:
```
p1 = Person("John", 20)
p1.__name  # will give AttributeError
```

You can still access the private members outside the class. Python performs name mangling, so every member prefixed
with **__** is changed to **_class__member**. So, accessing name will then be **p1._Person__name**. 
However, this is highly unadvised.