# Lists
import itertools

# region Condition
import copy

my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
new_list = ["ukraine", "iran", "USA"]
empty_list = []

# endregion

# region 1. Cut`s [:]
print(f'1.1 list[2:5] =>  {my_list[2:5]}')
print(f'1.2 list[:4] =>  {my_list[:4]}')
print(f'1.3 list[2:] =>  {my_list[2:]}')
print(f'1.4 list[-4:-2] =>  {my_list[-4:-2]}')
print(f'\n')
# endregion

# region 2 .append()
# append() -> Adds an element at the end of the list

new_list.append(my_list)
result = new_list
print(f'2. append() : {result}')
# endregion

# region 3 .clear()
# clear() -> Removes all the elements from the list
new_list.clear()
result = new_list
print(f'3 .clear() : {result}')
# endregion

# region 4 .copy()
# copy() -> Returns a copy of the list
new_list = my_list.copy()
a = [123]
b = [123, [12, 34]]
copy.deepcopy(a)

print(f'4 .copy() : {new_list}')
# endregion

# region 5 .count()
# count() -> method returns the number of elements with the specified value.
new_list = my_list.count('apple')
print(f'5 .count(`apple`) in myList : {new_list}')
# endregion

# region 6 .extend() + comprehension
# extend() -> Add the elements of a list (or any iterable), to the end of the current list
oldList = ["russia", "belarus", "china"]
new_list = ["ukraine", "iran", "USA"]
new_list.extend(oldList)
result = new_list
print(f'6 .extend() : {result}')

result = [x for y in [my_list] + [new_list] for x in y]
print(f'6.1 Comprehension : {result}')
# endregion

# region 7 .index()
# index() Returns the index of the first element with the specified value
intList = [1, 2, 3, 4, 5, 4, 3, 43, 2, 23, 11]
print(f'7 .index(4) : {intList.index(4)}')
# endregion

# region 8 .insert()
# insert() Adds an element at the specified position
new_list.insert(0, 'england')
result = new_list
print(f'8 .insert(`england`) : {result}')
# endregion

# region 9 .pop()
# pop() removes element, remove() removes the item at the specified position
new_list.remove('england')
new_list.remove(new_list[0])
new_list.pop(0)
result = new_list
print(f'9 .remove(`england`) and 0 index : {result}')
# endregion

# region 10 .reverse()
# reverse() Reverses the order of the list
new_list.reverse()
print(f'10 .reverse()  : {new_list}')
# endregion

# FUNCTIONS:
print('\n' + 20 * '*' + 'FUNCTIONS' + 20 * '*' + '\n')

# region 1. del
# del remove element
del new_list[0]
print(f'1. del 0 element: {new_list}')
# endregion

# region 2. sorted() and .sort()
# sort(reverse=True) and sorted(reverse=True), returns a sorted list of the specified iterable object.
alpha_list = ['g', 'h', 'a', '5', 'k', 'b']
print(f'\n2. sorted:\nalpha_list : {alpha_list} \nalpha_list with func sorted() : {sorted(alpha_list)}\n'
      f'again output alpha_list: {alpha_list}')

print(f'\n2.1 .sort()\nalpha_list : {alpha_list}')
alpha_list.sort()
print(f'alpha_list with method sort() : {alpha_list}\nagain output alpha_list: {alpha_list}')


# endregion

# region 3. Use func key for .sort(key=func)


def my_func(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=my_func)
print(f'\n3. Reverse cars to year: {cars}\n')
# endregion

# region 4. Cycle for and enumerate
for item in new_list:
    print(f'for item in new_list: {item}')
print(f'\n')

for item in range(0, len(new_list)):
    print(f'for item in range(0, len(new_list)): {str(item + 1)} {new_list[item]}')

# [print(f' for item in range(0, len(new_list)): {str(item + 1)} {new_list[item]}') for item in range(len(new_list))]
print(f'\n')

# 2 method using func enumerate()

for i, item in enumerate(new_list):
    print(f'for i, item in enumerate(new_list): {i + 1} {item}')
print(f'\n')
# [print(f' checkout item in list: {i + 1} {item}') for i, item in enumerate(new_list)]
# endregion

# region 5. Use range(0,10,2) for even and cycle
# even numbers in lists using range

even_numbers = list(range(0, 11, 2))
print(f'even numbers using range : {even_numbers}')

for i in range(0, 6):
    empty_list.append(i * 2)
print(f'even numbers using cycle : {empty_list}')
# endregion

print('\n' + 20 * '*' + 'NESTED LISTS' + 20 * '*' + '\n')

# region NESTED LISTS
# 1 methods:

nested_list = ['a', 'b', ['c', 'd', ['f']], 'g']


def flatten_list(input_lst):
    flattened = []
    for nested_item in input_lst:
        if isinstance(nested_item, list):
            flattened.extend(flatten_list(nested_item))
        else:
            flattened.append(nested_item)
    return flattened


flattened_list = flatten_list(nested_list)
print(flattened_list)

# 2 method

while any(isinstance(item, list) for item in nested_list):
    nested_list = list(itertools.chain.from_iterable(nested_list))

print(nested_list)
# endregion
