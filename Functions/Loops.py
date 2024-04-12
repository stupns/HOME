current_number = 0

while current_number <= 5:
    print(current_number)
    current_number += 1

# Example 2:
print('\nExample 2: ')

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# Example 3:
print('\nExample 3: ')
unconfirmed_users = ['serhii', 'yulia', 'lubomur']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user.title())

print(f'\nThe following users gave been confirmed:')
for user in confirmed_users:
    print(user.title())

# Example 4:
print('\nExample 4: ')
pets = ['dog', 'cat', 'fish', 'cat', 'dog', 'cat', 'frog', 'rabbit']

while pets.count('cat') > 1:
    pets.remove('cat')
print(pets)

# Example 5:
print('\nExample 5: ')
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# Example 6:
print('\nExample 5: ')
i = 0
a = 'Python'

while i < len(a):
    if a[i] == 't' or a[i] == 'h':
        i += 1
        break

    print('Current Letter :', a[i])
    i += 1
