import pytest
"""
TASK 1: Write a Python program to create a set.
Variables: 
empty_set,
non_empty_set -> [0, 1, 2, 3, 4]
set_literal -> [1,2,3,'foo','bar']
"""
# empty_set =
# non_empty_set =
# set_literal

"""
TASK 2: Write a Python program to iteration over sets.
"""
num_set2 = {0, 1, 2, 3, 4, 5}

"""
TASK 3: Write a Python program to add member(s) in a set.
-> {'Red'}
-> {'Green', 'Red', 'Blue'}
"""
color_set = {}

"""
TASK 4: Write a Python program to remove item(s) from a given set.
"""
num_set4 = {0, 1, 2, 3, 4, 5}

"""
TASK 5: Write a Python program to remove an item from a set if it is present in the set.
remove -> 4,5,5,15
"""
num_set5 = {0, 1, 2, 3, 4, 5}

"""
TASK 6: Write a Python program to create an intersection of sets.
"""
setx = {"green", "blue"}
sety = {"blue", "yellow"}
# task6 =

"""
TASK 7: Write a Python program to create a union of sets.
1 method using nested method.
2 method using special operator.
"""
setn1 = {1, 1, 2, 3, 4, 5}
setn2 = {1, 5, 6, 7, 8, 9}
# task7_1 =
# task7_2 =

"""
TASK 8: Write a Python program to create set difference.
1 method using nested method.
2 method using special operator.
"""
setn_8a = {1, 1, 2, 3, 4, 5}
setn_8b = {1, 5, 6, 7, 8, 9}

# task8_1 =
# task8_2 =

"""
TASK 9: Write a Python program to create a symmetric difference.
1 method using nested method.
2 method using special operator.
"""
setn_9a = {1, 1, 2, 3, 4, 5}
setn_9b = {1, 5, 6, 7, 8, 9}

# task9_1 =
# task9_2 =
"""
TASK 10: Write a Python program to check if a set is a subset of another set.
1 method using nested method.
2 method using special operator.
"""
# task10_xy =
# task10_yz =
# task10_xz =
# task10_zy =
# task10_subset =

"""
TASK 11: Write a Python program to create a shallow copy of sets.
"""

"""
TASK 12: Write a Python program to remove all elements from a given set.
"""


"""
TASK 13: Write a Python program to use of frozensets.
Note: Frozensets behave just like sets except they are immutable
"""

"""
TASK 14: Write a Python program to find maximum and the minimum value in a set.
"""

"""
TASK 15: Write a Python program to find the length of a set.
"""

"""
TASK 16: Write a Python program to check if a given value is present in a set or not.
"""

"""
TASK 17: Write a Python program to check if two given sets have no elements in common.
"""

"""
TASK 18: Write a Python program to check if a given set is superset of itself and superset of another given set.
"""

"""
TASK 19: Write a Python program to find the elements in a given set that are not in another set.
"""

"""
TASK 20: Write a Python program to remove the intersection of a 2nd set from the 1st set.
"""

pytest.main(['-rpP', '..\\TESTS\\TESTS_SETS.py'])