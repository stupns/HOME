# 1. Creating a list within a range
print(f'1. {[n for n in range(1, 7)]}')

# 2. First 10 squares of 2
print(f'2. {[2 ** n for n in range(6)]}')

# 3. Getting all the numbers multiples by 7 within a range
print(f'3. {[n for n in range(40) if n % 7 == 0]}\n')

# 4. Combine lists of list
list_1 = [['one', 'two', 'three'], ['five', 'six']]
A = ['one', 'two', 'three']
B = ['five', 'six']
print(f'A = {A}, B = {B}\n')
print(f'4. {[(n, x) for n in list_1[0] for x in list_1[1]]}')

# 5. Combine lists of list
print(f'5. {[(n, x) for n in A for x in B]}\n')

# 6. Print an element of a list if a given parameter matches
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print(f'Fruits = {fruits}\n')
newList = [x for x in fruits if 'a' in x]
print(f'6. {newList}')

# 7. Capitalize first letter
print(f'7. {[x.capitalize() for x in fruits]}')

# 8. Upper case all letters
print(f'8. {[x.upper() for x in fruits]}\n')

# WORKING WITH DICTIONARIES

# 9. Accesing to the keys of a dict as lists
dict_one = {
    'Mersedes': 'Fiat',
    'Model': 'A3',
    'Year': '2014'
}
print(f'{dict_one}\n')
print(f'9. {[[k for k in dict_one[v]] for v in dict_one.keys()]}')

# 10. Shows the keys related to the values
print(f'10. {[v for v in dict_one.values()]}')

# 11. Shows the values related to the keys
print(f'11. {[v for v in dict_one.keys()]}')

# 12. Tuples the values and keys
print(f'12. {[v for v in dict_one.items()]}\n')

# 13. Copy a list
list_to_copy = [1, 2, 3, 4, 5, 6]
print(f'13. {[element for element in list_to_copy]}')

# 14. print(copied_list)
myList = ['a', 'b', 'c', 'd', 'e']
newList = ['f', 'g', 'h']
print(f'14. {[x for y in [myList, newList] for x in y]}')

# 15. List comprehension list all the students born before the year 2000
dict_two = [('Dana Hausman', 1996), ('Corrine Haley', 1998), ('Huan Xin (Winnie) Cai', 1997),
            ('Greg Willits', 2001), ('Michael Lyda', 1995), ('Aidana Utepkaliyeva', 2000),
            ]
print(f'15 {[car for (car, year) in dict_two if year < 2000]}')

# 16. Deque:

from collections import deque
# Припустимо, нам потрібно знайти кількість чисел, більших за 5
d = deque([1, 6, 3, 8, 4, 7, 2, 6])

# Використання генератора списку і функції len для підрахунку
count_greater_than_5 = sum(1 for item in d if item > 5)
count_greater_than_6 = sum(i for i in d if i > 5)
print(f"Кількість чисел більших за 5: {count_greater_than_6}")