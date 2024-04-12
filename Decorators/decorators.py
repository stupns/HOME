def decorator(func):
    # print('Inside dec')

    def wrapper():
        print(f'-- before func -- {func.__name__}')
        func()
        print(f'-- after func -- {func.__name__}')

    return wrapper


@decorator
def basic():
    print('основна функція')


# 2._____Decorator-class

class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print(f'> before...')
        self.func()
        print(f'> after...')


@ClassDecorator
def helloWorld():
    print(f'func run')


# 3. ________ Function with arguments

def decorator_with_args(func):
    def decorated(a, b):
        ret = func(a ** 2, b * 2)
        print(f'a changed: {a ** 2}, b changed {b * 2}')
        return ret

    return decorated


@decorator_with_args
def add(a, b):
    print('функція a + b')
    return a + b


@decorator_with_args
def sub(a, b):
    print('функція а - b')
    return a - b


# 4.________ Class with arguments

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print('decor squares args...')
        a = self.func(a ** 2, b * 2)
        print(a)


@Decorator
def my_func(a, b):
    return a * b


# 5.________ Decorator with arguments

def decodecorator(dataType, message1, message2):
    def decorator(func):
        print(message1)

        def wrapper(*args, **kwargs):
            print(message2)
            if all([type(arg) == dataType for arg in args]):
                return func(*args, **kwargs)
            return "Invalid Input"

        return wrapper

    return decorator


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
    st = ''
    for i in args:
        st += i
    return st


@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ


# Check instance
user_permissions = ["user"]


def check_permission(permission):
    def wrapper_permission(func):
        def wrapped_check():
            if permission not in user_permissions:
                raise ValueError("Permission closed")
            return func()

        return wrapped_check

    return wrapper_permission


@check_permission("user")
def check_value():
    return True


@check_permission("admin")
def do_something():
    return True


if __name__ == "__main__":
    basic()
    print('\n2.Example')
    helloWorld()
    print('\n3.Example')
    print(f'add: {add(10, 5)}\n')
    print(f'sub: {sub(10, 5)}')
    print('\n4.Example')
    my_func(10, 20)
    print('\n5.Example')
    stringJoin("I ", 'like ', "Geeks", 'for', "geeks")
    summation(19, 2, 8, 533, 67, 981, 119)
    print('\n6.Example')
    check_value()
    do_something()
