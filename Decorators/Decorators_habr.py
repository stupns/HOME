def decorator_with_arguments(function_to_decorate):
    def wrapper_accepting_arguments(arg1, arg2):  # arguments come from here
        print(f'Show, my arguments:{arg1, arg2}')
        function_to_decorate(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def print_full_name(first_name, last_name):
    print(f'My name is {first_name} {last_name}')


# Decorating methods
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)

    return wrapper


class Lucy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print(f'My age is {self.age + lie}')


if __name__ == "__main__":
    print_full_name('Serhii', 'Stupnytskyi')

    lucy = Lucy()
    lucy.sayYourAge(5)
