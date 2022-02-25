"""
TASK 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
Sample Output:
25
48
"""
import pytest

task1 = lambda x: (x*2) + 5
task1_1 = lambda x, y: x*y

"""
TASK 2. Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number. Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
"""


def func_task2(n):
    return lambda x: n*x


task2 = func_task2(2)
task2_quares = task2(15)

"""
TASK 3: Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
list_task3 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list_task3.sort(key=lambda x: x[1])

"""
TASK 4: Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
list_of_dict_task4 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
                      {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
                      {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

task4 = sorted(list_of_dict_task4, key=lambda x: x['color'])

"""
TASK 5: Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""
nums_task5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
task5_even = list(filter(lambda x: x % 2 == 0, nums_task5))
task5_odd = list(filter(lambda x: x % 2 != 0, nums_task5))

"""
TASK 6: Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""
nums_task6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_nums6 = list(map(lambda x: x**2, nums_task6))
cube_nums6 = list(map(lambda x: x**3, nums_task6))

"""
TASK 7: Write a Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False
"""

task7 = lambda x: True if x.startswith('P') else False

"""
TASK 8: Write a Python program to extract year, month, date and time using Lambda.
use import datetime.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
"""
import datetime

now = datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()

"""
TASK 9: Write a Python program to check whether a given string is number or not using Lambda.
is_num9('26587') -> True
is_num9('4.2365') -> True
is_num9('-12547') -> False
is_num9('00') -> True
is_num9('A001') -> False
is_num9('001') -> True
is_num9m('-16.4') -> True
is_num9m('-24587.11') -> True
"""

is_num = lambda x: x.replace('.', '', 1).isdigit()
is_num9 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)

"""
TASK 10: Write a Python program to create Fibonacci series upto n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]

"""
from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x + x[-2] + x[-1], range(n - 2), [0, 1])


"""
TASK 11: Write a Python program to find intersection of two given arrays using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
"""
list_a = [1, 2, 3, 5, 7, 8, 9, 10]
list_b = [1, 2, 4, 8, 9]
task11 = list(filter(lambda x: x in list_a, list_b))
"""
TASK 12: Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
"""
list_12 = [-1, 2, -3, 5, 7, 8, 9, -10]
task12 = sorted(list_12, key=lambda x: 0 if x == 0 else -1 / x)
"""
TASK 13: Write a Python program to count the even, odd numbers in a given array of integers using Lambda
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
"""
list_13 = [1, 2, 3, 5, 7, 8, 9, 10]
odd_ctr = len(list(filter(lambda x: x % 2 != 0, list_13)))
even_ctr = len(list(filter(lambda x: x % 2 == 0, list_13)))

"""
TASK 14: Write a Python program to find the values of length six in a given list using Lambda.
Sample Output:
Monday
Friday
Sunday
"""
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
task_lambda = filter(lambda day: day if len(day) == 6 else '', weekdays)
task14 = [x for x in task_lambda]

"""
TASK 15: Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
"""
list_c = [1, 2, 3]
list_d = [4, 5, 6]
task15 = list(map(lambda x, y: x + y, list_c, list_d))

"""
TASK 16: Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]
"""
list_16 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
task16 = list(filter(lambda x: x % 13 == 0 or x % 19 == 0, list_16))

"""
TASK 17: Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
"""

string = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
task17 = list(filter(lambda x: x == ''.join(reversed(x)), string))

"""
TASK 18: Write a Python program to find all anagrams of a string in a given list of strings using lambda.
Orginal list of strings:
from collections import Counter 
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']
"""
from collections import Counter

string_list = ["bcda", "abce", "cbda", "cbea", "adcb"]
string18 = 'abcd'
task18 = list(filter(lambda x: Counter(string18) == Counter(x), string_list))
"""
TASK 19: Write a Python program to find the numbers of a given string and store them in a list, display the numbers 
which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.
Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56
"""

string19 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
str_num = [x for x in string19.split(' ')]
lenght = len(str_num)
numbers19 = [int(x) for x in str_num if x.isdigit()]
task19 = sorted([i for i in filter(lambda x: x > lenght, numbers19)])

"""
TASK 20: Write a Python program that multiply each number of given list with a given number using lambda function. 
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
Remember about method join because need result in string type : 4 8 12 18 22
"""

list_20 = [2, 4, 6, 9, 11]
n = 2
task20 = ' '.join(map(str, list(map(lambda num: num * n, list_20))))

"""
TASK 21: Write a Python program that sum the length of the names of a given list of names after removing the names that 
starts with an lowercase letter. Use lambda function.
Result:
16
"""
list_21 = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
list_21 = list(filter(lambda x: x[0].isupper() and x[1:].islower(), list_21))
task21 = len(''.join(list_21))

"""
TASK 22: Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers
 using lambda function.
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48
"""

list_22 = [2, 4, -6, -9, 11, -12, 14, -5, 17]
summ_positive = sum(list(filter(lambda x: x > 0, list_22)))
summ_negative = sum(list(filter(lambda x: x < 0, list_22)))

"""
TASK 23: Write a Python program to find the list with maximum and minimum length using lambda.
List with maximum length of lists:
(3, [13, 15, 17])

List with minimum length of lists:
(1, [0])
"""
list_23 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]


def max_length_list(input_list):
    max_length = max(len(x) for x in input_list)
    max_lists = max(input_list, key=lambda x: len(x))
    return max_length, max_lists


def min_length_list(input_list):
    min_length = min(len(x) for x in input_list)
    min_lists = min(input_list, key=lambda x: len(x))
    return min_length, min_lists


"""
TASK 24: Write a Python program to sort each sublist of strings in a given list of lists using lambda.
"""


def sort_sublists(input_list):
    result = [sorted(x, key=lambda x: x[0]) for x in input_list]
    return result


color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]

"""
TASK 25: Write a Python program to sort a given list of lists by length and value using lambda.
"""

list25 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]


def sort_sublists25(input_list):
    result = sorted(input_list, key=lambda l: (len(l), l))
    return result


"""
26 TASK : Write a Python program to find the maximum value in a given heterogeneous list using lambda.
Maximum values in the said list using lambda:
5
"""

list_26 = ['Python', 3, 2, 4, 5, 'version']


def max_val(list_val):
    max_val = max(list_val, key=lambda i: (isinstance(i, int), i))
    return max_val

# ___________________________________________________TESTS

pytest.main([r'-rpP','..\\TESTS\\TESTS_LAMBDA.py'])
