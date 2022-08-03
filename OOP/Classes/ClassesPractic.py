class my_class(object):
    pass
class A(my_class):
    pass
class B(my_class):
    pass
class C(my_class):
    pass

#Here are the names of the subclasses:
print([cls.__name__ for cls in my_class.__subclasses__()])

#Here are the subclasses themselves:
print(my_class.__subclasses__())

#Confirmation that my_class is the base class:
for cls in my_class.__subclasses__():
    print(cls.__base__)


def get_all_subclasses(cls):
    all_subclasses = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses


# pass base class as argument
print(get_all_subclasses(my_class))