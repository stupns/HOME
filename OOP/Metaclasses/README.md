Metaclasses
===============

Metaclasses are an esoteric OOP concept, lurking behind virtually all Python code. You are using them whether you are
aware of it or not. For the most part, you don’t need to be aware of it. Most Python programmers rarely, if ever,
have to think about metaclasses.

_New-Style Classes_

New-style classes unify the concepts of class and type. If obj is an instance of a new-style class,
type(obj) is the same as **obj.__class__:**


```
>>> class Foo:
...     pass
>>> obj = Foo()
>>> obj.__class__
<class '__main__.Foo'>
>>> type(obj)
<class '__main__.Foo'>
>>> obj.__class__ is type(obj)
True
```

```
>>> n = 5
>>> d = { 'x' : 1, 'y' : 2 }

>>> class Foo:
...     pass
...
>>> x = Foo()

>>> for obj in (n, d, x):
...     print(type(obj) is obj.__class__)
...
True
True
True
```
# Defining a Class Dynamically

The built-in type() function, when passed one argument, returns the type of an object.
For new-style classes, that is generally the same as the **object’s __class__ attribute**:
```
>>> type(3)
<class 'int'>

>>> type(['foo', 'bar', 'baz'])
<class 'list'>

>>> t = (1, 2, 3, 4, 5)
>>> type(t)
<class 'tuple'>

>>> class Foo:
...     pass
...
>>> type(Foo())
<class '__main__.Foo'>
```

You can also call type() with three arguments—type(<name>, <bases>, <dct>):

- < name > specifies the class name. This becomes the __name__ attribute of the class.
- < bases > specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.
- < dct > specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.

Calling type() in this manner creates a new instance of the type metaclass. In other words, it dynamically creates a new class.

In each of the following examples, the top snippet defines a class dynamically with type(), while the snippet below it
defines the class the usual way, with the class statement. In each case, the two snippets are functionally equivalent.

# Custom Metaclasses

Consider again this well-worn example:

```
>>> class Foo:
...     pass
...
>>> f = Foo()
```

The expression Foo() creates a new instance of class Foo. When the interpreter encounters Foo(), the following occurs:

- The __call__() method of Foo’s parent class is called. Since Foo is a standard new-style class, its parent class is the type metaclass, so type’s __call__() method is invoked.

- That __call__() method in turn invokes the following:
  - __new__()
  - __init__()
  
If Foo does not define __new__() and __init__(), default methods are inherited from Foo’s ancestry. But if Foo does
define these methods, they override those from the ancestry, which allows for customized behavior when instantiating Foo.

In the following, a custom method called new() is defined and assigned as the __new__() method for Foo:

```
>>> def new(cls):
...     x = object.__new__(cls)
...     x.attr = 100
...     return x
...
>>> Foo.__new__ = new

>>> f = Foo()
>>> f.attr
100

>>> g = Foo()
>>> g.attr
100
```

You can define your own metaclass, which derives from type, and then you can muck around with that instead.
The first step is to define a metaclass that derives from type, as follows:

```
>>> class Meta(type):
...     def __new__(cls, name, bases, dct):
...         x = super().__new__(cls, name, bases, dct)
...         x.attr = 100
...         return x
...
```

The definition header class Meta(type): specifies that Meta derives from type. Since type is a metaclass,
that makes Meta a metaclass as well.

Note that a custom __new__() method has been defined for Meta. It wasn’t possible to do that to the type metaclass directly.
The __new__() method does the following:

- Delegates via super() to the __new__() method of the parent metaclass (type) to actually create a new class
- Assigns the custom attribute attr to the class, with a value of 100
- Returns the newly created class

Now the other half of the voodoo: Define a new class Foo and specify that its metaclass is the custom metaclass Meta,
rather than the standard metaclass type. This is done using the metaclass keyword in the class definition as follows:

```
>>> class Foo(metaclass=Meta):
...     pass
...
>>> Foo.attr
100
```

Voila! Foo has picked up the attr attribute automatically from the Meta metaclass. Of course, any other classes you 
define similarly will do likewise:

```
>>> class Bar(metaclass=Meta):
...     pass
...
>>> class Qux(metaclass=Meta):
...     pass
...
>>> Bar.attr, Qux.attr
(100, 100)
```

In the same way that a class functions as a template for the creation of objects, a metaclass functions as a template
for the creation of classes. Metaclasses are sometimes referred to as class factories.

Compare the following two examples:

**Object Factory:**
```
>>> class Foo:
...     def __init__(self):
...         self.attr = 100
...

>>> x = Foo()
>>> x.attr
100

>>> y = Foo()
>>> y.attr
100

>>> z = Foo()
>>> z.attr
100
```

**Class Factory:**

```
>>> class Meta(type):
...     def __init__(
...         cls, name, bases, dct
...     ):
...         cls.attr = 100
...
>>> class X(metaclass=Meta):
...     pass
...
>>> X.attr
100

>>> class Y(metaclass=Meta):
...     pass
...
>>> Y.attr
100

>>> class Z(metaclass=Meta):
...     pass
...
>>> Z.attr
100
```

#**Is This Really Necessary?**

As simple as the above class factory example is, it is the essence of how metaclasses work. They allow customization of
class instantiation.

Still, this is a lot of fuss just to bestow the custom attribute attr on each newly created class. Do you really need a
metaclass just for that?

In Python, there are at least a couple other ways in which effectively the same thing can be accomplished:

**Simple Inheritance:**

```
>>> class Base:
...     attr = 100
...

>>> class X(Base):
...     pass
...

>>> class Y(Base):
...     pass
...

>>> class Z(Base):
...     pass
...

>>> X.attr
100
>>> Y.attr
100
>>> Z.attr
100
```

**Class Decorator:**

```
>>> def decorator(cls):
...     class NewClass(cls):
...         attr = 100
...     return NewClass
...
>>> @decorator
... class X:
...     pass
...
>>> @decorator
... class Y:
...     pass
...
>>> @decorator
... class Z:
...     pass
...

>>> X.attr
100
>>> Y.attr
100
>>> Z.attr
100
```

# Conclusion

As Tim Peters suggests, metaclasses can easily veer into the realm of being a “solution in search of a problem.”
It isn’t typically necessary to create custom metaclasses. If the problem at hand can be solved in a simpler way,
it probably should be. Still, it is beneficial to understand metaclasses so that you understand Python classes in
general and can recognize when a metaclass really is the appropriate tool to use.