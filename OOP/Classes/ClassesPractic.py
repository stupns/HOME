class MyClass(object):  ...
class A(MyClass):  ...
class B(MyClass):  ...
class C(MyClass):  ...


# Here are the names of the subclasses:
print([cls.__name__ for cls in MyClass.__subclasses__()])

# Here are the subclasses themselves:
print(MyClass.__subclasses__())

# Confirmation that my_class is the base class:
for cls in MyClass.__subclasses__():
    print(cls.__base__)


def get_all_subclasses(cls):
    all_subclasses = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses


# Pass base class as argument
print(get_all_subclasses(MyClass))
