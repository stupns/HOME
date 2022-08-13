string = 'Python'

# lambda returns a function object
print(lambda string: string)

# Example 2:

x = "Python"
(lambda x: print(x))(x)  # lambda gets pass to print


# Example 3 : showing difference between def() and lambda().
def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y
print(cube(5))  # using the normally defined function
print(lambda_cube(5))  # using the lambda function

# Example 4 : showing difference between def() and lambda().
tables = [lambda x=x: x * 10 for x in range(1, 11)]

for table in tables:
    print(table())

# Example 5 :
List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
# Get the second largest element
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)  # [3, 16, 9]

# Example 5 : filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)  # [5, 7, 97, 77, 23, 73, 61]

# Example 5 : Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print(adults)  # [90, 59, 21, 60]

# Example 5 : map() with lambda() to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)  # [10, 14, 44, 194, 108, 124, 154, 46, 146, 122]

# Example 5 : use of lambda() function with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
print(uppered_animals)  # ['DOG', 'CAT', 'PARROT', 'RABBIT']

# Example 5 : reduce() with lambda() to get sum of a list

from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)  # 193

# Example 5 :python code to demonstrate working of reduce() with a lambda function

lis = [1, 3, 5, 6, 2, ]

print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))  # The maximum element of the list is : 6
