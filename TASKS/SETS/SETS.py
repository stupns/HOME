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
setp_11 = {"Red", "Green"}
setq_11 = {"Green", "Red"}
# task11_a =
# task11_b =

"""
TASK 12: Write a Python program to remove all elements from a given set.
"""
setc_12 = {"Red", "Green", "Black", "White"}
# setc_12 =

"""
TASK 13: Write a Python program to use of frozensets.
Note: Frozensets behave just like sets except they are immutable
"""
x_13 = frozenset([1, 2, 3, 4, 5])
y_13 = frozenset([3, 4, 5, 6, 7])
# task13_a =
# task13_b =
# task13 =

"""
TASK 14: Write a Python program to find maximum and the minimum value in a set.
"""
set14 = {5, 10, 3, 15, 2, 20}
# set_max =
# set_min =

"""
TASK 15: Write a Python program to find the length of a set.
"""
set15 = {5, 5, 5, 5, 5, 5, 7}
# set_len =

"""
TASK 16: Write a Python program to check if a given value is present in a set or not.
"""
nums16 = {10, 20, 30, 40, 50}
# task16 =


pytest.main(['-rpP', '..\\TESTS\\TESTS_SETS.py'])