# Counter
___
Клас **Counter** з модуля collections у Python – це спеціалізований підклас **dict**, призначений для підрахунку 
**хешованих** об'єктів. Він особливо корисний, коли потрібно підрахувати елементи в ітерабельному об'єкті 
(наприклад, у списку або рядку) або коли потрібно визначити частоту виникнення окремих елементів.

Основні характеристики Counter:
- Елементи зберігаються як ключі словника, а їх кількість – як значення.
- Підрахунок елементів відбувається автоматично при створенні Counter.
- Можна легко додавати або віднімати елементи, об'єднувати лічильники, а також виконувати інші операції, специфічні 
для підрахунку.

## Methods
Counter objects support additional methods beyond those available for all dictionaries:

- **elements()**
* * Return an iterator over elements repeating each as many times as its count. Elements are returned in the order first
encountered. If an element’s count is less than one, elements() will ignore it.

- **most_common([n])**
* * Return a list of the n most common elements and their counts from the most common to the least. If n is omitted or None,
most_common() returns all elements in the counter. Elements with equal counts are ordered in the order first encountered:

- **subtract([iterable-or-mapping])**
* * Elements are subtracted from an iterable or from another mapping (or counter). Like dict.update() but subtracts counts
instead of replacing them. Both inputs and outputs may be zero or negative.

- **total()**
* * Compute the sum of the counts.

- **fromkeys(iterable)**
* * This class method is not implemented for Counter objects.

- **update([iterable-or-mapping])**
* * Elements are counted from an iterable or added-in from another mapping (or counter). Like dict.update() but adds counts
instead of replacing them. Also, the iterable is expected to be a sequence of elements, not a sequence of (key, value) pairs.
___

Приклади використання Counter:

1. Базовий підрахунок елементів
```python
from collections import Counter

# Підрахунок символів у рядку
chars_count = Counter("banana")
print(chars_count)  # Counter({'a': 3, 'n': 2, 'b': 1})
```

2. Підрахунок елементів у списку
```python
# Підрахунок чисел у списку
nums_count = Counter([1, 2, 3, 4, 1, 2, 1])
print(nums_count)  # Counter({1: 3, 2: 2, 3: 1, 4: 1})
```
3. Використання методів Counter
```python
# Отримання найпоширеніших елементів
common_elements = chars_count.most_common(2)
print(common_elements)  # [('a', 3), ('n', 2)]

# Оновлення підрахунку з іншого ітерабельного об'єкта
chars_count.update('apple')
print(chars_count)  # Counter({'a': 4, 'p': 2, 'n': 2, 'b': 1, 'l': 1, 'e': 1})
```
4. Арифметичні операції з Counter

```python
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter('alphabet')

# Віднімання елементів
result_subtract = c1 - c2
print(result_subtract)  # Counter({'a': 1})

# Об'єднання лічильників (максимальне значення)
result_union = c1 | c2
print(result_union)  # Counter({'a': 2, 'b': 1, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})
```


Counter є потужним інструментом для роботи з даними, коли потрібен ефективний підрахунок елементів. 
Його легкість у використанні та гнучкість роблять його ідеальним для широкого спектру задач, від обробки тексту до
аналізу даних.