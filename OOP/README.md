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

# *[Inheritance](https://github.com/stupns/HOME/blob/master/OOP/Classes/%D0%A1lasses.py)*
**Задачі**: [Classes-tasks.](https://github.com/stupns/HOME/tree/master/TASKS/CLASSES "Classes tasks")


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

# *[Polymorphism](https://github.com/stupns/HOME/blob/master/OOP/Polymorphism.py)*

Polymorphism simply means having many forms. It refers to the use of a single type entity (method, operator or object)
to represent different types in different scenarios.For example, we need to determine if the given species of birds fly or not,
using polymorphism we can do this using a single function.

# *[Encapsulation](https://github.com/stupns/HOME/blob/master/OOP/Encapsulation.py)*
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

# *[Abstraction](https://github.com/stupns/HOME/blob/master/OOP/Abstraction.py)*

Abstraction in python is defined as hiding the implementation of logic from the client and using the particular
application. And the most important key feature of Object-Oriented Programming. It hides the irrelevant data specified
in the project, reducing complexity and giving value to the efficiency. Abstraction is made in Python using Abstract
classes and their methods in the code.

**Syntax:**

_Abstract class Syntax is declared as_
```
from abc import ABC
// declaration
Class classname(ABC);
```
_Abstract method Syntax is declared as_
```
Def abstractmethod name():
Pass
```

**How does Abstraction work in Python?**

As the primary role of the Abstraction is to hide the internal functioning of the code, and the interactions are made
with the users through the basic implementation. In other words, the user knows what he is doing, not how the works are
done behind. So let’s go deeper into the topic to find its importance.

In Python, Abstraction works by incorporating abstract classes and methods.

**Abstract Class:** A class specified in the code that has abstract methods is named Abstract Class.

**Abstract Method:** Here, it doesn't have any implementation. All the implementations are done inside the sub-classes.

Python makes use of a self-variable in method definitions and in initializing a variable. In python, a class method
gives information about the class. To define an instant method, this method should declare self as a parameter.

**Declared abstract class:**

```
from abc import ABC
class abs_class(ABC):
    def method(self):  #normal method
        pass
        
    @abstractmethod
    def Abs_method(self):  #method definition
        #Abs_method definition
        pass
```

[MRO](https://github.com/stupns/HOME/blob/master/OOP/MRO.py) (Method resolution order)
===============

**Method Resolution Order(MRO)** it denotes the way a programming language resolves a method or attribute.
Python supports classes inheriting from other classes. The class being inherited is called the Parent or Superclass,
while the class that inherits is called the Child or Subclass. In python, method resolution order defines the order
in which the base classes are searched when executing a method. First, the method or attribute is searched within a
class, and then it follows the order we specified while inheriting. This order is also called Linearization of a class
and set of rules are called MRO(Method Resolution Order).While inheriting from another class, the interpreter needs a
way to resolve the methods that are being called via an instance.Thus, we need the method resolution order. 

In the above example we use multiple inheritances, and it is also called **Diamond inheritance**, and it looks as follows: 
![mro](https://github.com/stupns/HOME/blob/master/images-git/mro.png)

Python follows a depth-first lookup order and hence ends up calling the method from class A. By following the method
resolution order, the lookup order as follows. 
Class D -> Class B -> Class C -> Class A 
Python follows depth-first order to resolve the methods and attributes. So in the above example,
it executes the method in class B. 

```
class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
 
r = B()
r.rk()
```
**Output:** 

  `In class B`
  
**Old and New Style Order :** 

In the older version of Python(2.1) we are bound to use old-style classes but in Python(3.x & 2.2) we are bound to use
only new classes. New style classes are the ones whose first parent inherits from Python root ‘object’ class.

```
# Old style class
class OldStyleClass:
    pass
 
# New style class
class NewStyleClass(object):
    pass
```

Method resolution order(MRO) in both the declaration style is different.
Old style classes use **DLR or depth-first left to right algorithm** whereas new style classes use **C3 Linearization algorithm**
for method resolution while doing multiple inheritances. 

**C3 Linearization Algorithm :** 

C3 Linearization algorithm is an algorithm that uses new-style classes. It is used to remove an inconsistency created by DLR Algorithm. It has certain limitation they are: 
 

- Children precede their parents
- If a class inherits from multiple classes, they are kept in the order specified in the tuple of the base class.

C3 Linearization Algorithm works on three rules: 
 

- Inheritance graph determines the structure of method resolution order.
- User have to visit the super class only after the method of the local classes are visited.
- Monotonicity

**Methods for Method Resolution Order(MRO) of a class:** 
To get the method resolution order of a class we can use either __mro__ attribute or mro() method.
By using these methods we can display the order in which methods are resolved.
For Example 

```
class A:
    def rk(self):
        print(" In class A")
class B:
    def rk(self):
        print(" In class B")
 
# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")
 
r = C()
 
# it prints the lookup order
print(C.__mro__)
print(C.mro())
```

**Output:**
```
Constructor C

(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```