from contextlib import contextmanager


class SomeClass:
    def run(self):
        print('run')


@contextmanager
def toy_example():
    print('Starting')
    try:
        yield SomeClass()
    except ValueError as e:
        print(e)
        print('ignore Exception')
    except Exception as e:
        print(e)
        print('Do not ignore Exception')
        raise
    finally:
        print('Exiting')


with toy_example() as toy:
    print(f'{toy.run()}')

print('\nExample 2: ')


# 2. Example

@contextmanager
def hello_name(name):
    try:
        print('What is your name?')
        yield name
    except Exception as e:
        print(e)
        print('Do not ignore Exception')
        raise
    finally:
        print('Goodbye', name)


with hello_name('David') as my_name:
    print(f'Run yield var: {my_name}')
