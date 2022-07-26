# Lists
import copy

myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newList = ["ukraine", "iran", "USA"]
emptyList = []

print(f'list[2:5] =>  {myList[2:5]}')
print(f'list[:4] =>  {myList[:4]}')
print(f'list[2:] =>  {myList[2:]}')
print(f'list[-4:-2] =>  {myList[-4:-2]}')

# append() -> Adds an element at the end of the list
print(f'\n')

newList.append(myList)
result = newList
print(f'append() : {result}')

result = [x for y in [myList, newList] for x in y]
print(result)

# clear() -> Removes all the elements from the list
newList.clear()
result = newList
print(f'clear() : {result}')

# copy() -> Returns a copy of the list
newList = myList.copy()
a = [123]
b = [123,[12,34]]
copy.deepcopy(a)

print(f'copy() : {newList}')

# count() -> method returns the number of elements with the specified value.
newList = myList.count('apple')
print(f'count(`apple`) in myList : {newList}')

# extend() -> Add the elements of a list (or any iterable), to the end of the current list
oldList = ["russia", "belarus", "china"]
newList = ["ukraine", "iran", "USA"]
newList.extend(oldList)
result = newList
print(f'extend() : {result}')

# index() Returns the index of the first element with the specified value
intList = [1, 2, 3, 4, 5, 4, 3, 43, 2, 23, 11]
print(f'index(4) : {intList.index(4)}')

# insert() Adds an element at the specified position
newList.insert(0, 'england')
result = newList
print(f'insert(`england`) : {result}')

# pop() removes element, remove() removes the item at the specified position
newList.remove('england')
newList.remove(newList[0])
newList.pop(0)
result = newList
print(f'remove(`england`) and 0 index : {result}')

# reverse() Reverses the order of the list
newList.reverse()
print(f'reverse()  : {newList}')

# del remove element
del newList[0]
print(f'delete 0 element: {newList}')

# sort(reverse=True) and sorted(reverse=True), returns a sorted list of the specified iterable object.
alpha_list = ['g', 'h', 'a', '5', 'k', 'b']
print(f'\nalpha_list : {alpha_list} \nalpha_list with func sorted() : {sorted(alpha_list)}\n'
      f'again output alpha_list: {alpha_list}')

print(f'\nalpha_list : {alpha_list}')
alpha_list.sort()
print(f'alpha_list with method sort() : {alpha_list}\nagain output alpha_list: {alpha_list}')


def myFunc(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(f'\nreverse cars to year {cars}\n')

# ______________________________________________________________________________________________________________________

for item in newList:
    print(f'checkout item in list: {item}')

print(f'\n')

counter = len(newList)
for item in range(0, counter):
    print(f'checkout item in list: {str(item + 1)} {newList[item]}')

# 2 method using func enumerate()
print(f'\n')
for i, item in enumerate(newList):
    print(f'checkout item in list: {i + 1} {item}')

# even numbers in lists using range
print(f'\n')
even_numbers = list(range(0, 11, 2))
print(f'even numbers using range : {even_numbers}')

for i in range(0, 6):
    emptyList.append(i * 2)
print(f'even numbers using cycle : {emptyList}')

# list comprehension
print(f'\n')
[print(x) for x in emptyList]


