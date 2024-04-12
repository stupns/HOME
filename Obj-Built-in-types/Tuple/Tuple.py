# region Condition
# 1. Init tuple

a = ()  # Empty tuple
b = (5, 'Hello', True)  # tuple of 3 elements of different types
c = ('world', (2.88, "abc"))  # nested tuple
d = 5, 'Hello', True  # same tuple as b
e = (3.88,)  # A tuple is strictly one element
print(f'id c = (`world`, (2.88, "abc"): {id(c)}')
# endregion

# region 2. Operation tuple()
word = 'hello'  # ('H', 'e', 'l', 'l', 'o')
example_var = tuple((3, 2, 0, -5))   # (3, 2, 0, -5)
# endregion

# region 3. Operation T[i]
a_el = ('a', 'bc', 'def', 'gin')
item_2 = a_el[2]  # item_2 = 'def'
# endregion\\\\\\\\\\\\\\sazxc

# region 3.1 A tuple containing another tuple and its elements
b_el = (a_el, a_el[1], True)  # (('a', 'bc', 'def', 'gin'), 'bc', True)
item_0 = b_el[0]  # item_0 = ('a', 'bc', 'def', 'gin')
item_1 = b_el[1]  # item_1 = 'bc'
# endregion

# region 3.2 A tuple containing a list
c = (1, [2, 3, 4], "text")

# Extract a list from a tuple
item_3 = c[1]  # item_3 = [2, 3, 4], с = (1, [2, 3, 4], 'text')
# endregion

# region 3.2. The list in the tuple is mutable, so it can be changed
c[1][1] = 8  # с = (1, [2, 8, 4], 'text')
# endregion

# region 4. Concatenation
A = (1, 2, 3)
B = (4, 5, 6)
C = A + B  # C = (1, 2, 3, 4, 5, 6)
# endregion

# region 5. Cycle a tuple in a loop

a_new = ("abc", "abed", "bcd", "cde")

# Output all tuple elements
for item in a_new:
    print(item)

"""
abc
abed
bcd
cde
"""
# endregion

# region 6. Cycle while
# The output tuple - integers
A_int = (-1, 3, -8, 12, -20)

# Calculate the number of positive numbers
i = 0
k = 0  # к-number positive numbers

while i < len(A_int):
    if A_int[i] < 0:
        k = k + 1
    i = i + 1

# Output result
print("k = ", k)  # k = 3
# endregion

# region 6.1 Cycle for in a loop
# Given a tuple containing strings
A_chr = ("abc", "ad", "bcd")

# Form a new list from the elements of tuple A, in the new list B, each element
# is doubled
B_chr = [item * 2 for item in A_chr]

print("A = ", A_chr)
print("B = ", B_chr)
# endregion

# region 7. Method index() in tuple

# The index method - determines the position (index) of the element in the tuple
A_week = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")

# Request to enter the name of the day of the week
day = str(input("Enter day: "))

# Correctly calculate the index
if day in A_week:  # checking whether the string day is in the tuple A
    num = A_week.index(day)
    print("Number of day = ", num + 1)
else:
    num = -1
    print("Wrong day.")
# endregion