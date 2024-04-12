Constructor
===============

The constructor is a method that is called when an object is created. This method is defined in the class and can be used
to initialize basic variables.

If you create four objects, the class constructor is called four times. Every class has a constructor, but its not 
required to explicitly define it.

Example
===============

**Constructor**
Each time an object is created a method is called. That methods is named the constructor.

The constructor is created with the function init. As parameter we write the self keyword, which refers to itself
(the object). The process visually is:

![constructor](https://github.com/stupns/HOME/blob/master/images-git/Constructor.png)

Inside the constructor we initialize two variables: legs and arms. Sometimes variables are named properties in the 
context of object oriented programming. We create one object (bob) and just by creating it, its variables are initialized.

```
class Human:
   def __init__(self):
       self.legs = 2
       self.arms = 2

bob = Human()
print(bob.legs)
```

The newly created object now has the variables set, without you having to define them manually. You could create tens or 
hundreds of objects without having to set the values each time.

**python __init__**

The function **init(self)** builds your object. Its not just variables you can set here, you can call class methods too.
Everything you need to initialize the object(s).

Lets say you have a class Plane, which upon creation should start flying. There are many steps involved in taking off:
accelerating, changing flaps, closing the wheels and so on.

The default actions can be defined in methods. These methods can be called in the constructor.
```
class Plane:
    def __init__(self):
        self.wings = 2

        # fly
        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
            print('Accelerating')

    def flaps(self):
            print('Changing flaps')

    def wheels(self):
            print('Closing wheels')

ba = Plane()
```

To summarize: A constructor is called if you create an object. In the constructor you can set variables and call methods.

**Default value**

The constructor of a class is unique: initiating objects from different classes will call different constructors.

Default values of newly created objects can be set in the constructor.

The example below shows two classes with constructors. Then two objects are created but different constructors are called.

```
class Bug:
   def __init__(self):
       self.wings = 4

class Human:
   def __init__(self):
       self.legs = 2
       self.arms = 2

bob = Human()
tom = Bug()

print(tom.wings)
print(bob.arms)
```

But creating multiple objects from one class, will call the same constructor.