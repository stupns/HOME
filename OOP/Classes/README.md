Class(es) and Objects in Python
===============

Python class is concept of “object-oriented programming”. Python is an object-oriented programming language (oop).
OOP is a way to build software.

With OOP you can make your program much more organized, scalable, reusable and extensible. The OOP concept can be a bit
weird. It can be challenging to grasp, but it’s a very powerful concept.

Example
===============

- **Objects**

In Python, you can define objects. An object is a collection of methods and variables. Objects live somewhere in the
computer's memory. They can be manipulated at runtime.

Let's create a theoretical example, we create an object dog. Creating an object is just one line of code:

```
obj1 = dog()
```

Each object can have variables. The values of those variables are unique to the object. We set object variables (name,age)

```
obj1.name = "Woof"
obj1.age = 5
```

If methods exist for an object, they can be called. The objects unique variables can be used in those methods.
The methods can be used multiple times:

```
obj1.bark()
obj1.bark()
```

In your program you can have multiple objects. Those objects can be of the same type or a different type.

```
obj1 = dog()
obj2 = dog()
obj3 = dog()
obj4 = bird()
```

So how does Python know the type of object? How does it know which methods and variables exist for a type?
They are defined in a class.

- **Class**

Objects are always created from classes. A class define each method and variable that exists within the object. You could see classes as blueprints for objects.

Remember we had objects of type dog in the previous example?

The object had **variables** (age,name) and a **method** (bark). they are defined in the class dog.
This is how that class is defined:

```
class dog:
    name = ""
    age = 0

    def bark(self):
        print('Bark')	
```

First we define the class itself: class dog. Then the variables are defined (name,dog). Finally, we define the method. If you look closely you’ll see the method has the word self in it. The word self refers to the object (You can create several objects from a class.)


- **Detailed example**

Classes are not just used for funny examples (dog,bird). They’re used all over computer software.

If you are given the task of making a web browser, you need to show a website at some point.
Let`s say the program will be object-orientated. Then a class can be defined in this way:

```
#!/usr/bin/python
class Website:
    def __init__(self,title):
        self.title = title

    def showTitle(self):
        print(self.title)
```

_Wait... what’s init?_

If an object is created, the method **init** is called. This is always the first method that is called when creating
a new object. The method is called the **constructor**.

Then you can create the web browser object.

```
#!/usr/bin/python
class Website:
    def __init__(self,title):
        self.title = title

    def showTitle(self):
        print(self.title)

obj = Website('pythonbasics.org')
obj.showTitle()
```

In this example we have one object (obj), created from the class Website.
The class has two methods: **init()** and showTitle().