from Tasks import make_pizza
# functions

def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


example1 = formatted_name('serhii', 'stupnitskiy')
print(example1)
print('\n')


def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


example2 = build_person('serhii', 'stupnitskiy')
print(example2)
print('\n')

usernames = ['ivan', 'taras', 'serhii', 'igor']


def filter_name(names):
    for name in names[:]:
        if name == 'taras':
            names.remove(name)
    for item in names:
        print(f'Hello {item.title()}')


filter_name(usernames)
print('\n')


# 2 func


def print_models(my_list_device, finish_device):
    while my_list_device:
        current_work = my_list_device.pop()
        print(f'We are now work on {current_work}')
        finish_device.append(current_work)


def show_finish_elements(finish_device):
    for elem in finish_device:
        print(f'My element in finish work: {elem}')


my_list_work = ['iphone', 'notebook', 'macbook']
finish_list_work = []

print_models(my_list_work[:], finish_list_work)
print('\n')
show_finish_elements(finish_list_work)


# *args , **kwargs

print('\n')


def build_profile(first_name, last_name, **kwargs):
    kwargs['first_name'] = first_name
    kwargs['last_name'] = last_name
    return kwargs


user_profile = build_profile('serhii', 'ivanov', location='princeton', field='physics', age=12)
print(user_profile)
print('\n')

# use func from import module

make_pizza('potato', 'cheese', 'eggs')