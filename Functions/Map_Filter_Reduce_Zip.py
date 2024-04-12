# *************MAP()**************
print('Maps():')
numbers = [2, 4, 6, 8, 10]


# returns square of a number
def square(number):
    return number * number


# apply square() function to each item of the numbers list
squared_numbers_iterator = list(map(square, numbers))
print(squared_numbers_iterator)  # [4, 16, 36, 64, 100]

# Example 2: Lambda with map():
numbers = (1, 2, 3, 4)

result = set(map(lambda x: x * x, numbers))
print(f'\nExample 2: \n{result}')

# Example 3: Multiple Iterators to map() Using Lambda:
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = list(map(lambda n1, n2: n1 + n2, num1, num2))
print(f'\nExample 3: \n{result}')

# Example 4: len words in lists
words = ["Welcome", "to", "Real", "Python"]

result = list(map(len, words))
print(f'\nExample 4: \n{result}')

# Example 5: Removing Punctuation
text = """Some people, when confronted with a problem, think 
I know, I'll use regular expressions.
Now they have two problems. Jamie Zawinski"""

import re


def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)


result = list(map(remove_punctuation, text.split()))
print(f'\nExample 5: \n{result}')

# *************FILTER()**************
print('\nFilter():')

numbers = [-2, -1, 0, 1, 2]
positive_numbers = list(filter(lambda n: n > 0, numbers))
print(f'{positive_numbers}')

# Example 2
objects = [0, 1, [], 4, 5, "", None, 8]
result = list(filter(lambda x: x, objects))
print(f'\nExample 2: \n{result}')

# Example 3
numbers = [1, 3, 10, 45, 6, 50]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(f'\nExample 3: \n{result}')

# Example 4
words = ["variable", "file#", "header", "_non_public", "123Class"]
result = list(filter(str.isidentifier, words))
print(f'\nExample 4: \n{result}')

# Example 5
words = ("filter", "Ana", "hello", "world", "madam", "racecar")


def is_palindrom(word):
    reversed_word = "".join(reversed(word))
    return word.lower() == reversed_word.lower()


result = list(filter(is_palindrom, words))
print(f'\nExample 5: \n{result}')

# ***********REDUCE()***********
print('\nReduce():\n')

from functools import reduce


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


numbers = [0, 1, 2, 3, 4]
print(f'\n{reduce(my_add, numbers)}')

# Example 2:
result = reduce(my_add, [], 0)
print(f'\nExample 2: \n{result}')  # 0

# Example 3:
numbers = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, numbers)
print(f'\nExample 3: \n{result}')

# Example 4:
numbers = [1, 2, 3, 4]
result = reduce(lambda a, b: a * b, numbers)
print(f'\nExample 4: \n{result}')


# Example 5:
def my_min_func(a, b):
    return a if a < b else b


def my_max_func(a, b):
    return a if a > b else b


numbers = [3, 5, 2, 4, 7, 1]

a = reduce(my_min_func, numbers)
b = reduce(my_max_func, numbers)
c = reduce(lambda a, b: a if a < b else b, numbers)
d = reduce(lambda a, b: a if a > b else b, numbers)
e = min(numbers)
f = max(numbers)
print(f'\nExample 5: \n'
      f'my_min_func: {a}\nmy_max_func: {b},'
      f'\nmin_lambda: {c}\nmax_lambda: {d},'
      f'\nmin(): {e}\nmax(): {f}')


# Example 6: func
def both_true(a, b):
    return bool(a and b)


res_1 = reduce(both_true, [1, 1, 1, 1, 1])
res_0 = reduce(both_true, [1, 1, 1, 1, 0])
res_empty = reduce(both_true, [], True)
print(f'\nExample 6: func \n'
      f'[1, 1, 1, 1, 1] : {res_1}\n'
      f'[1, 1, 1, 1, 0] : {res_0}\n'
      f'[] : {res_empty}')

# Example 7: Lambda

lambda_1 = reduce(lambda a, b: bool(a or b), [0, 0, 1, 1, 0])
lambda_0 = reduce(lambda a, b: bool(a or b), [0, 0, 0, 0, 0])
lambda_empty = reduce(lambda a, b: bool(a or b), [], False)
print(f'\nExample 7: lambda \n'
      f'[0, 0, 1, 1, 0] : {lambda_1}\n'
      f'[0, 0, 0, 0, 0] : {lambda_0}\n'
      f'[] : {lambda_empty}')

# Example 8: Any():

any_1 = any([1, 1, 1, 1, 1])
any_0 = any([1, 1, 1, 1, 0])
any_empty = any([])
print(f'\nExample 7: lambda \n'
      f'[1, 1, 1, 1, 1] : {any_1}\n'
      f'[1, 1, 1, 1, 0] : {any_0}\n'
      f'[] : {any_empty}')

print('\nZip():\n')

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = list(zip(numbers, letters))
print(f'zipped list: {zipped}')

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
zipped = list(zip(s1, s2))
print(f'zipped sets: {zipped}')

a = [1, 2, 3]
zipped = list(zip(a))
print(f'one arg: {zipped}')

integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = list(zip(integers, letters, floats))
print(f'triple args: {zipped}')

# Example 2: zip_longest:
from itertools import zip_longest

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = list(zip_longest(numbers, letters, longest, fillvalue=None))
print(f'\nExample 2: \nzip_longest: {zipped}')

# Example 3: ranged:
zipped = list(zip(range(5), range(100)))
print(f'\nExample 3: \nzip_ranged 2 args : {zipped}')

# Example 4: cycle for() with list:
print(f'\nExample 4:')
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')

# Example 5: cycle for() with dict:
print(f'\nExample 5:')
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)

# Example 6: Unzipping a Sequence
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(f'\nExample 6: \nnumbers: {numbers},\nletters: {letters}')

# Example 7: Building Dictionaries
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields, values))
print(f'\nExample 7: \n{a_dict}')
new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
print(f'Update : {a_dict}')
