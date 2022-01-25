# Different exercises of lists comprehension

# Creating a list within a range

a = [n for n in range(1, 7)]

# print(a)

# First 10 squares of 2

b = [2 ** n for n in range(10)]

# print(b)

# Getting all the numbers multiples by 7 within a range

c = [n for n in range(100) if n % 7 == 0]

# print(c)

# Combine lists of list

d = [['Camisa roja', 'Camisa azul', 'Camisa verde', 'Camisa amarilla'], ['Pantalon negro', 'Pantalon blanco']]

d_a = [(n, x) for n in d[0] for x in d[1]]

# print(d_a)

# O Or

eA = ['Camisa roja', 'Camisa azul', 'Camisa verde', 'Camisa amarilla']
eB = ['Pantalon negro', 'Pantalon blanco']

eC = [(n, x) for n in eA for x in eB]

# print(eC)

# Print an element of a list if a given parameter matches

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits if 'a' in x]

# print(newlist)

# Capitalize first letter

newlist2 = [x.capitalize() for x in fruits]

# print(newlist2)

# Upper case all letters

newlist3 = [x.upper() for x in fruits]

# print(newlist3)

# working with Dictionaries

# Accesing to the keys of a dict as lists

dict_one = {
    'Mersedes': 'Fiat',
    'Model': 'A3',
    'Year': '2014'
}

itr = [[k for k in dict_one[v]] for v in dict_one.keys()]

# Shows the keys related to the values

itr2 = [v for v in dict_one.values()]

# Shows the values related to the keys

itr3 = [v for v in dict_one.keys()]

print(itr)
print(itr2)
print(itr3)

# Tuples the values and keys

itr4 = [v for v in dict_one.items()]

# print(itr2)
# print(itr3)
print(itr4)

# Copy a list

list_to_copy = [1, 2, 3, 4, 5, 6]
copied_list = [element for element in list_to_copy]

# print(copied_list)

myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newList = ["ukraine", "iran", "USA"]

result = [x for y in [myList, newList] for x in y]
print(result)
