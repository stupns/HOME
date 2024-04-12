class Foo:
    pass


obj = Foo()

print(obj.__class__)  # <class '__main__.Foo'>
type(obj)  # <class '__main__.Foo'>
print(obj.__class__ is type(obj))  # True
print(type(Foo))  # <class 'type'>

# Example 1

Foo = type('Foo', (), {})
x = Foo()
print(x)  # <__main__.Foo object at 0x0000020F6015BE50>

# Example 2

Bar = type('Bar', (Foo,), dict(attr=100))
a = Bar()
print(a.attr)  # 100
print(a.__class__)  # <class '__main__.Bar'>
print(a.__class__.__bases__)  # (<class '__main__.Foo'>,)


# Example 3

def f(obj):
    return f'attr = {obj.attr}'


class Boo:
    attr = 100
    attr_val = f


boo = Boo()
print(boo.attr)  # 100
print(boo.attr_val())  # attr = 100


# Example 4

class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


class NewMet(metaclass=Meta):
    pass


print(NewMet.attr)  # 100


# Class Factory:

class Meta(type):
    def __init__(cls, name, basis, dct):
        cls.attr = 100


class X(metaclass=Meta):
    pass


class Y(metaclass=Meta):
    pass


print(X.attr, Y.attr)  # 100 100


# Simple Inheritance:

class Base:
    attr = 100


class A(Base):
    pass


class B(Base):
    pass


print(A.attr, B.attr)  # 100 100


# Class Decor:

def decorator(cls):
    class NewClass(cls):
        attr = 100

    return NewClass


@decorator
class C(Base):
    pass


@decorator
class D(Base):
    pass


print(C.attr, D.attr)  # 100 100
