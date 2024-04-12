from datetime import date


class Fruit:
    name = 'Fruits'

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)


# Alternative writing
class AltFruit:
    name = 'Fruits'

    def printName(cls):
        print('The name is:', cls.name)


# 2 Example
class Person:
    CONFIG = {
        'foo': 42
    }

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year)

    @classmethod
    def foo(cls):
        print(cls.CONFIG)

    @staticmethod
    def check_age(age):
        print(age > 18)


if __name__ == "__main__":
    apple = Fruit()
    berry = Fruit()
    Fruit.printName()
    apple.printName()
    berry.printName()
    print('\nAlternative writing:')
    AltFruit.printAge = classmethod(AltFruit.printName)  # use classmethod here
    AltFruit.printAge()
    print('\n2 Example:')
    person1 = Person('Mark', 20)
    person2 = Person.details('Rohan', 1992)
    print(person1.name, person1.age)
    print(person2.name, person2.age)
    Person.check_age(25)
    Person.foo()
