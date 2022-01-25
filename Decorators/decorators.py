# def basic_function(a):
#     """Базова функція"""
#     print(f'Базова функція:{a}')
#     return a + 1
#
#
# print('старт програми')
# print('імя:', basic_function.__name__)
# print('док:', basic_function.__doc__)
# b = basic_function(1)
# print(f'кінець програми:{b}')

# ________________________________________________


# def decorator(func):
#     print('декоратор')
#
#     def wrapper():
#         print(f'-- перед функцією', func.__name__)
#         func()
#
#     return wrapper
#
#
# @decorator
# def basic():
#     print('основна функція')
#
#
# print('>> start')
# basic()
# print('>> finish')

# _____Decorator-class

# class Decorator:
#     def __init__(self, func):
#         print('> Клас Decorator метод __init__')
#         self.func = func
#
#     def __call__(self):
#         print('> перед викликом класу...', self.func.__name__)
#         self.func()
#         print('> після виклику класу')
#
#
# @Decorator
# def helloWorld():
#     print('функція hello world')
#
#
# print('>> старт')
# helloWorld()
# print('>> кінець')

# ________ Function with arguments

# def decorator_with_args(func):
#     def decorated(a, b):
#         ret = func(a ** 2, b * 2)
#         print(f'a changed: {a ** 2}, b changed {b * 2}')
#         return ret
#
#     return decorated
#
#
# @decorator_with_args
# def add(a, b):
#     print('функція a + b')
#     return a + b
#
#
# @decorator_with_args
# def sub(a, b):
#     print('функція а - b')
#     return a - b
#
#
# print('>> старт')
# r = add(10, 5)
# print('r:', r)
# g = sub(10, 5)
# print('g:', g)
# print('>> кінець')

# ________ Class with arguments
#
# class Decorator:
#     def __init__(self, func):
#         print('> Класс Decorator метод __init__')
#         self.func = func
#
#     def __call__(self, a, b):
#         a = self.func(a**2, b*2)
#         print(a)
#
# @Decorator
# def my_func(a, b):
#     return a * b
#
# print('>> старт')
# my_func(10, 20)
# print('>> кiнець')

# ________ Decorator with arguments


# def decodecorator(dataType, message1, message2):
#     def decorator(func):
#         print(message1)
#
#         def wrapper(*args, **kwargs):
#             print(message2)
#             if all([type(arg) == dataType for arg in args]):
#                 return func(*args, **kwargs)
#             return "Invalid Input"
#
#         return wrapper
#
#     return decorator
#
#
# @decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
# def stringJoin(*args):
#     st = ''
#     for i in args:
#         st += i
#     return st
#
#
# @decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
# def summation(*args):
#     summ = 0
#     for arg in args:
#         summ += arg
#     return summ
#
#
# print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
# print()
# print(summation(19, 2, 8, 533, 67, 981, 119))

# Перевірка станів

# user_permissions = ["user"]
#
#
# def check_permission(permission):
#     def wrapper_permission(func):
#         def wrapped_check():
#             if permission not in user_permissions:
#                 raise ValueError("Недостаточно прав")
#             return func()
#
#         return wrapped_check
#
#     return wrapper_permission
#
#
# @check_permission("user")
# def check_value():
#     return "значение"
#
#
# @check_permission("admin")
# def do_something():
#     return "только админ"
#
#
# print('старт программы')
# check_value()
# do_something()
# print('конец программы')



