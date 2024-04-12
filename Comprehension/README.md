СOMPREHENSION
===============
- [Comprehension tasks](https://github.com/stupns/HOME/blob/master/TASKS/COMPREHENSION/COMPREHENSION_READY.py
"comprehension tasks")



```
new_list = [expression for member in iterable]
```
 A more complete description of the comprehension formula adds support for optional **conditionals**. The most common way
 to add conditional logic to a list comprehension is to add a conditional to the end of the expression:

```
new_list = [expression for member in iterable (if conditional)]
```
**Example**:
```
>>> sentence = 'the rocket came back from mars'
>>> vowels = [i for i in sentence if i in 'aeiou']
>>> vowels
['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
```
You can place the conditional at the end of the statement for simple filtering, but what if you want to change a member
value instead of filtering it out? In this case, it’s useful to place the conditional near the beginning of the expression:

```
new_list = [expression (if conditional) for member in iterable]
```
**Example**:
```
>>> original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
>>> prices = [i if i > 0 else 0 for i in original_prices]
>>> prices
[1.25, 0, 10.22, 3.78, 0, 1.16]
```

Comprehensions can be nested to create combinations of lists, dictionaries, and sets within a collection. 
```
>>> cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
>>> temps = {city: [0 for _ in range(7)] for city in cities}
>>> temps
{
    'Austin': [0, 0, 0, 0, 0, 0, 0],
    'Tacoma': [0, 0, 0, 0, 0, 0, 0],
    'Topeka': [0, 0, 0, 0, 0, 0, 0],
    'Sacramento': [0, 0, 0, 0, 0, 0, 0],
    'Charlotte': [0, 0, 0, 0, 0, 0, 0]
}
```
Nested lists are a common way to create matrices, which are often used for mathematical purposes. Take a look at the code block below:
```
>>> matrix = [[i for i in range(5)] for _ in range(6)]
>>> matrix
[
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]
```
So far, the purpose of each nested comprehension is pretty intuitive. However, there are other situations, such as
flattening nested lists, where the logic arguably makes your code more confusing. Take this example, which uses a nested
list comprehension to flatten a matrix:
```
matrix = [
...     [0, 0, 0],
...     [1, 1, 1],
...     [2, 2, 2],
... ]
>>> flat = [num for row in matrix for num in row]
>>> flat
[0, 0, 0, 1, 1, 1, 2, 2, 2]
```
