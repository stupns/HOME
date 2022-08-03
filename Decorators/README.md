DECORATORS
===============
- [setter-getter](https://github.com/stupns/HOME/tree/master/OOP/Getter-and-Setter "getter and setter")

# **property**

In Python, getters and setters are not the same as those in other object-oriented programming languages.
Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.
Private variables in python are not actually hidden fields like in other object-oriented languages. Getters and Setters
in python are often used when:

- We use getters & setters to add validation logic around getting and setting a value.
- To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

# <p align=center>Using @property decorators to achieve getters and setters behaviour</p>

In previous method we used property() function in order to achieve getters and setters behaviour.
However, as mentioned earlier in this post getters and setters are also used for validating the getting and setting of
attributes value. There is one more way to implement property function i.e. by using decorator. Python @property is one
of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes in such a 
way so that the user of your class no need to make any change in their code.