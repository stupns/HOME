# from datetime import date
#
# '''
# @staticmethod — используется для создания метода, который ничего не знает о классе или экземпляре, через который он был
#  вызван.
# '''
#
#
# class Myclass:
#     @staticmethod
#     def staticmethod():
#         print('static method called')
#
#
# Myclass.staticmethod()
#
#
# class Person:
#     @staticmethod
#     def is_adult(age):
#         if age > 18:
#             print(True)
#             return True
#         else:
#             print(False)
#             return False
#
#
# Person.is_adult(28)
#
# '''
# @classmethod — это обычный метод класса, имеющий доступ ко всем атрибутам класса, через который он был вызван.
#  Следовательно, classmethod — это метод, который привязан к классу, а не к экземпляру класса.
# '''
#
#
# class Person:
#     CONFIG = {
#         'foo': 42
#     }
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def details(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     @classmethod
#     def foo(cls):
#         print(cls.CONFIG)
#
#     @staticmethod
#     def check_age(age):
#         return age > 18


# person1 = Person('Mark', 20)
# person2 = Person.details('Rohan', 1992)
#
# print(person1.name, person1.age)
# print(person2.name, person2.age)
# print(Person.check_age(25))
# Person.foo()

# @property

class People:
    def __init__(self, name):
        self.__name = ''

    def setname(self, name):
        print('setname() called')
        self.__name = name

    def getname(self):
        print('getname() called')
        return self.__name

    name = property(getname, setname)


obj = People('serhii')
print(obj.__dict__)
obj.setname('ivan')
print(obj.__dict__)
obj.__name = 'SeRHII'
print(obj.__dict__)

# Вік людини не може бути від'ємним

# class People2:
#     def __init__(self):
#         #__ для внутрішнього використання
#         self.__name = ''
#         self.__age = 0
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         if new_age < 0:
#             raise ValueError('negative age')
#         self.__age = new_age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         if not new_name.isalpha():
#             raise ValueError('digits in name')
#         self.__name = new_name
#
# p = People2()
# p.age = 12
# p.name = 'Serhii'
# print(p.age, p.name)
#
# a = 'serhii'
# print(a.isdigit())

class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return 3.1415 * self.r**2

c = Circle(10)
print(c.area)