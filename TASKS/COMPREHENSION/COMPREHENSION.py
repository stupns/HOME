import pytest

task1 = [-x for x in range(10)]
"""
TASK 2. Create comprehension with range(10).
"""

task2 = []

"""
TASK 3: Use x*2 in comprehension.
"""

task3 = []

"""
TASK 4: Use x+1 elem in comprehension.
"""

task4 = []

"""
TASK 5:Output (x*2)+1 to 1..10 in comperhension.
"""

task5 = []

"""
TASK 6: Output quares 1..10 in comperhension. 
"""

task6 = []

"""
TASK 7: Find all of the numbers from 1–1000 that are divisible by 8.
Use variable range(20).
"""
nums7 = []
task7 = []

"""
TASK 8: Find all of the numbers from 1–1000 that have a 6 in them.
Use variable range(20).
"""
nums8 = [x for x in range(20)]
task8 = []

"""
TASK 9: Count the number of spaces in a string.
"""

string9 = 'Practice Problems to Drill List Comprehension in Your Head.'
task9 = []

"""
TASK 10: Remove all of the vowels in a string.  Vowels = ["a", "e", "i", "o", "u"]
Use method (.join)
"""

string10 = 'Practice Problems to Drill List Comprehension in Your Head.'
task10 = []

"""
TASK 11: This is a slightly different way of applying list comprehension. 
Problem Statement: The goal is to tokenize the following 5 sentences into words, excluding the stop words.
Use method split.
"""

sentences11 = ["a new world record was set",
               "in the holy city of ayodhya",
               "on the eve of diwali on tuesday",
               "with over three lakh diya or earthen lamps",
               "lit up simultaneously on the banks of the sarayu river"]
stopwords11 = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']
task11 = []

"""
TASK 12: Find all of the words in a string that are less than 5 letters.
Use variable with method split.
"""

string12 = 'Practice Problems to Drill List Comprehension in Your Head.'
words_split12 = string12.split()
task12 = []

"""
TASK 13: Use a dictionary comprehension to count the length of each word in a sentence (use string above)
Use variable with method split.
"""

string13 = 'Practice Problems to Drill List Comprehension in Your Head.'
words_split13 = string13.split()
task13 = {}

"""
TASK 14: Use a nested(вкладений) list comprehension to find all of the numbers from 1–1000
that are divisible by any single digit besides 1 (2–9).
Use variable range(20) comprehension.
[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18]
"""

nums14 = [x for x in range(20)]
task14 = []

"""
TASK 15: For all the numbers 1–1000, use a nested list/dictionary comprehension to find the 
highest single digit any of the numbers is divisible by.
Use variable range range(20) comprehension.
"""

nums15 = [x for x in range(20)]
task15 = {}

"""
TASK 16:Using list comprehension, construct a list from the squares of each element in the list, if the square 
is greater than 50.
range(0,15) only even.
"""

task16 = []

"""
TASK 17: Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of
 vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.
"""

dict17 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
          "Motorcycle": 110}
task17 = []

"""
TASK 18: Get the index and the value as a tuple for items in the
list ["hi", 4, 8.99, 'apple', ('t,b','n')]. Result would look like [(index, value), (index, value)]
Index + 1 enumerate.
"""

list_18 = ["hi", 4, 8.99, 'apple', ('t,b', 'n')]
task18 = []

"""
TASK 19: Find the common numbers in two lists (without using a tuple or set) 
list_a = [1, 2, 3, 4],
list_b = [2, 3, 4, 5]
"""

list_a19 = [1, 2, 3, 4]
list_b19 = [2, 3, 4, 5]
task19 = []


"""
TASK 20: Get only the numbers in a sentence like 'In 1984 there were 13 instances of
a protest with over 1000 people attending'. Result is a list of numbers like [3,4,5]
Use variable with inside method split.
"""

sentence20 = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
string_split = sentence20.split()
task20 = []

"""
TASK 21: Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even,
 and the word 'odd' if the number is odd. Result would look like ['odd','odd', 'even']
"""

task21 = []

"""
TASK 22: Produce a list of tuples consisting of only the matching numbers in these lists
list_a = [1, 2, 3,4,5,6,7,8,9], list_b = [2, 7, 1, 12]. Result would look like (4,4), (12,12) -
"""

list_a22 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b22 = [2, 7, 1, 12]
task22 = []

"""
TASK 23:  Given a 1D list, negate all elements which are between 3 and 8, using list comprehensions.
[1, 2, -3, -4, -5, -6, -7, -8, 9, 10]
"""
list_23 = [1, 2, -3, -4, -5, -6, -7, -8, 9, 10]
task23 = []

"""
TASK 24: Make a dictionary of the 26 english alphabets mapping each with the corresponding integer.

{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
 
import string
using : string.ascii_letters[:26]
"""

import string

task24 = {}

"""
TASK 25: Replace all alphabets in the string ‘Lee Quan Yew’, by substituting the alphabet with the corresponding
 numbers, like 1 for ‘a’, 2 for ‘b’ and so on.
 
Variables:
d = {}
[] in 'Lee Quan Yew'
"""

dict25 = {}
task25 = []

"""
26 TASK : Get the unique list of words from the following sentences, excluding any stopwords.
"""

sentences26 = ["The Hubble Space telescope has spotted",
             "a formation of galaxies that resembles",
             "a smiling face in the sky"]
stopwords26 = {'face', 'formation', 'galaxies', 'has', 'hubble', 'resembles',
             'sky', 'smiling', 'space', 'spotted', 'telescope', 'that', 'the'}

task26 = {}

pytest.main(['-rpP', '..\\TESTS\\TESTS_COMPREHENSION.py'])
