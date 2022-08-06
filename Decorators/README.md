DECORATORS
===============
- [setter-getter](https://github.com/stupns/HOME/tree/master/OOP/Getter-and-Setter "getter and setter")

A decorator in Python is a function that takes another function as its argument, and returns yet another function.
Decorators can be extremely useful as they allow the extension of an existing function, without any modification to
the original function source code.

- In Python, we can define a function inside another function.
- In Python, a function can be passed as parameter to another function (a function can also return another function).

**Simple decorator:**
```
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
```
**Simple decorator with args:**

```
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))
```

# [**property**](https://github.com/stupns/HOME/blob/master/Decorators/property.py)

In Python, getters and setters are not the same as those in other object-oriented programming languages.
Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.
Private variables in python are not actually hidden fields like in other object-oriented languages. Getters and Setters
in python are often used when:

- We use getters & setters to add validation logic around getting and setting a value.
- To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

**Using @property decorators to achieve getters and setters behaviour**

In previous method we used property() function in order to achieve getters and setters behaviour.
However, as mentioned earlier in this post getters and setters are also used for validating the getting and setting of
attributes value. There is one more way to implement property function i.e. by using decorator. Python @property is one
of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes in such a 
way so that the user of your class no need to make any change in their code.

# [**static**](https://github.com/stupns/HOME/blob/master/Decorators/static.py)

Static method can be called without creating an object or instance. Simply create the method and call it directly.
This is in a sense orthogonal to object orientated programming: we call a method without creating objects.

This runs directly against the concept of object-oriented programming and might be frowned upon, but at times it can be
useful to have a static method.

**Calling static methods**

Normal class methods and static methods can be mixed (because why not?).
This can get very confusing: we use both the concept of object orientation and functional programming mixed in one class.

If you create an object, we can call non-static methods. But you can also call the static method without creating the object.

```
class Music:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")

Music.play()

obj = Music()
obj.stop()
```

Overall, static methods are an interesting concept to know, but in practice you’d rarely use them.
Sometimes using static methods could be an indication of having a bad design.

# [**classmethod**](https://github.com/stupns/HOME/blob/master/Decorators/classmethod.py)

A class method is a method that’s shared among all objects. To call a class method, put the class as the first argument.

Class methods can be called from instances and from the class itself. All of these use the same method.
The method can use the classes variables and methods.

**Calling classmethod`s**

To turn a method into a classmethod, add @classmethod before the method definition. As parameter the method always takes the class.

The example below defines a class method. The class method can then be used by the class itself. In this example the
class method uses the class property name.

``` 
class Fruit:
    name = 'Fruits'

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)

Fruit.printName()
```


