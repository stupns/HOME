current_number = 0

# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Using continue
print('\n')

# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# Почати з користувачів, яких треба перевірити та порожнього списку підветрджених користувачів
# Перевіряти кожного перевіреного користувача до списку підтвердженних користувачів

unconfirmed_users = ['serhii', 'yulia', 'lubomur']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user.title())

print(f'\nThe following users gave been confirmed:')
for user in confirmed_users:
    print(user.title())

# Remove string in list with cycle while
pets = ['dog', 'cat', 'fish', 'cat', 'dog', 'cat', 'frog', 'rabbit']

while pets.count('cat') > 1:
    pets.remove('cat')
print(pets)
