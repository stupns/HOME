def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


example1 = formatted_name('Serhii', 'Stupnytskyi')
print(f'{example1}')

print('\nExample 2: ')


def build_person(first_name, last_name, age=None):
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person


example2 = build_person('serhii', 'stupnytskyi')
print(f'{example2.get("first_name").title()} {example2.get("last_name").title()}')

print('\nExample 3:')


usernames = ['ivan', 'taras', 'serhii', 'igor']


def filter_name(names):
    for name in names[:]:
        if name == 'taras':
            names.remove(name)
    for item in names:
        print(f'Hello {item.title()}')


filter_name(usernames)

print('\nExample 4:')


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
print_models(my_list_work, finish_list_work)


print('\n')
show_finish_elements(finish_list_work)


print('\n')


def build_profile(first_name, last_name, **kwargs):
    kwargs['first_name'] = first_name
    kwargs['last_name'] = last_name
    return kwargs


user_profile = build_profile('serhii', 'ivanov', location='princeton', field='physics', age=12)
print(user_profile)
print('\n')
