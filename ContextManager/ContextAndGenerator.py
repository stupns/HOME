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
    toy.run()