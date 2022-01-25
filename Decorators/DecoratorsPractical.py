



def fictive(decorator_text):
    def decorator_func(func):
        print('Input in decorator')
        def wrapper(*args):
            print(f'{decorator_text}', end='')
            func(*args)
            print('Output with decorator')
        return wrapper
    return decorator_func



@fictive(decorator_text='Hello, ')
def result(text):
    print(text)

result('world')
