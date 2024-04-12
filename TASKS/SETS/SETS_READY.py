import pytest

from settings import test_path

"""
TASK 1: Write a Python program to create a set.
Variables: 
empty_set,
non_empty_set -> [0, 1, 2, 3, 4]
set_literal -> [1,2,3,'foo','bar']
"""
empty_set = {}
non_empty_set = {0, 1, 2, 3, 4}
set_literal = {1, 2, 3, 'foo', 'bar'}

"""
TASK 2: Write a Python program to iteration over sets.

"""
num_set2 = {0, 1, 2, 3, 4, 5}
for value, char in enumerate(num_set2):
    print(char, end=' ')
print('\n')

"""
TASK 3: Write a Python program to add member(s) in a set.
-> {'Red'}
-> {'Green', 'Red', 'Blue'}
"""
color_set = set()
color_set.add("Red")
color_set.update(["Blue", "Green"])

"""
TASK 4: Write a Python program to remove item(s) from a given set.
"""
num_set4 = {0, 1, 2, 3, 4, 5}
num_set4.pop()

"""
TASK 5: Write a Python program to remove an item from a set if it is present in the set.
remove -> 4,5,5,15
"""
num_set5 = {0, 1, 2, 3, 4, 5}
num_set5.discard(4)
num_set5.discard(5)
num_set5.discard(5)
num_set5.discard(15)

"""
TASK 6: Write a Python program to create an intersection of sets.
"""
setx = {"green", "blue"}
sety = {"blue", "yellow"}
task6 = setx.intersection(sety)

"""
TASK 7: Write a Python program to create a union of sets.
1 method using nested method.
2 method using special operator.
"""
setn1 = {1, 1, 2, 3, 4, 5}
setn2 = {1, 5, 6, 7, 8, 9}
task7_1 = setn1.union(setn2)
task7_2 = setn1 | setn2

"""
TASK 8: Write a Python program to create set difference.
1 method using nested method.
2 method using special operator.
"""
setn_8a = {1, 1, 2, 3, 4, 5}
setn_8b = {1, 5, 6, 7, 8, 9}

task8_1 = setn_8a - setn_8b
task8_2 = setn_8a.difference(setn_8b)
"""
TASK 9: Write a Python program to create a symmetric difference.
1 method using nested method.
2 method using special operator.
"""
setn_9a = {1, 1, 2, 3, 4, 5}
setn_9b = {1, 5, 6, 7, 8, 9}

task9_1 = setn_9a ^ setn_9b
task9_2 = setn_9a.symmetric_difference(setn_9b)

"""
TASK 10: Write a Python program to check if a set is a subset of another set.
1 method using nested method.
2 method using special operator.
"""
setx_10 = {"apple", "mango"}
sety_10 = {"mango", "orange"}
setz_10 = {"mango"}

task10_xy = setx_10 <= sety_10
task10_yz = sety_10 <= setz_10
task10_xz = setx_10 <= setz_10
task10_zy = setz_10 <= sety_10
task10_subset = setz_10.issubset(sety)

"""
TASK 11: Write a Python program to create a shallow copy of sets.
"""
setp_11 = {"Red", "Green"}
setq_11 = {"Green", "Red"}
task11_a = setp_11.copy()
task11_b = setq_11.copy()

"""
TASK 12: Write a Python program to remove all elements from a given set.
"""
setc_12 = {"Red", "Green", "Black", "White"}
setc_12.clear()

"""
TASK 13: Write a Python program to use of frozensets.
Note: Frozensets behave just like sets except they are immutable
"""
x_13 = frozenset([1, 2, 3, 4, 5])
y_13 = frozenset([3, 4, 5, 6, 7])
task13_a = x_13.isdisjoint(y_13)
task13_b = x_13.difference(y_13)
task13 = x_13 | y_13

"""
TASK 14: Write a Python program to find maximum and the minimum value in a set.
"""
set14 = {5, 10, 3, 15, 2, 20}
set_max = max(set14)
set_min = min(set14)

"""
TASK 15: Write a Python program to find the length of a set.
"""
set15 = {5, 5, 5, 5, 5, 5, 7}
set_len = len(set15)

"""
TASK 16: Write a Python program to check if a given value is present in a set or not.
"""
nums16 = {10, 20, 30, 40, 50}
task16 = nums16.issuperset(nums16)


pytest.main(['-rpP', test_path.TEST_SETS])
