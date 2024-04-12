# Deque
___
Клас **deque** з модуля **collections** в Python — це об'єкт двосторонньої черги, який підтримує додавання та видалення
елементів з обох кінців з високою продуктивністю.

Методи:
- **append(x)¶**
Add x to the right side of the deque.

- **appendleft(x)**
Add x to the left side of the deque.

- **clear()**
Remove all elements from the deque leaving it with length 0.

- **copy()**
Create a shallow copy of the deque.

- **count(x)**
Count the number of deque elements equal to x.

- **extend(iterable)**
Extend the right side of the deque by appending elements from the iterable argument.

- **extendleft(iterable)**
Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in 
reversing the order of elements in the iterable argument.

- **index(x[, start[, stop]])**
Return the position of x in the deque (at or after index start and before index stop). Returns the first match or raises ValueError if not found.

- **insert(i, x)**
Insert x into the deque at position i. If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raised.

- **pop()**
Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

- **popleft()**
Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

- **remove(value)**
Remove the first occurrence of value. If not found, raises a ValueError.

- **reverse()**
Reverse the elements of the deque in-place and then return None.

- **rotate(n=1)**
Rotate the deque n steps to the right. If n is negative, rotate to the left.
When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()),
and rotating one step to the left is equivalent to d.append(d.popleft()).

Deque objects also provide one read-only attribute:

- **maxlen**
Maximum size of a deque or None if unbounded.

___
Ось кілька ключових аспектів та прикладів використання deque:

Основні характеристики deque:
- Швидке додавання та видалення: Операції append та pop виконуються швидко на обох кінцях.
- Гнучкість: deque підтримує безпечне і ефективне використання як стека так і черги.
- Обмеження розміру: Можливість встановлення максимальної довжини, при досягненні якої, додавання нових елементів викликає видалення найстаріших.

**Приклади використання deque:**
1. Створення та додавання елементів:
```python
from collections import deque

# Створення deque
d = deque()

# Додавання елементів на кінець
d.append('a')
d.append('b')

# Додавання елементів на початок
d.appendleft('0')
print(d)  # deque(['0', 'a', 'b'])
```
2. Видалення елементів:
```python
# Видалення елемента з кінця
d.pop()
print(d)  # deque(['0', 'a'])

# Видалення елемента з початку
d.popleft()
print(d)  # deque(['a'])
```
3. Використання як обмеженої черги:
```python
# Створення deque з обмеженням розміру
d = deque(maxlen=3)

# Додавання елементів
d.append(1)
d.append(2)
d.append(3)
print(d)  # deque([1, 2, 3], maxlen=3)

# Додавання ще одного елемента виштовхне найстаріший (1)
d.append(4)
print(d)  # deque([2, 3, 4], maxlen=3)
```
4. Обертання елементів:

- **deque** також підтримує обертання елементів, що дозволяє ефективно "зсувати" всі елементи вліво або вправо.
```python
d = deque([1, 2, 3, 4, 5])

# Обертання вправо
d.rotate(1)
print(d)  # deque([5, 1, 2, 3, 4])

# Обертання вліво
d.rotate(-2)
print(d)  # deque([2, 3, 4, 5, 1])
``` 

deque є дуже універсальним і може бути використаним у багатьох сценаріях, зокрема для реалізації стеків, черг, 
кільцевих буферів та для підтримки алгоритмів, яким потрібен швидкий доступ до елементів з обох кінців колекції.


5. Копіювання:

Метод **copy()** у deque з модуля **collections** у Python створює поверхневу копію об'єкта deque. 
"Поверхнева" копія означає, що створюється новий об'єкт deque, який містить посилання на ті ж об'єкти, 
що і оригінальний deque. Якщо елементи в deque є незмінними (наприклад, цілі числа, рядки), то поверхнева копія 
функціонуватиме майже як глибока копія, оскільки незмінні об'єкти не можуть бути змінені. 
Однак, якщо елементи є змінними об'єктами (наприклад, списками), зміни в цих об'єктах в одному deque відобразяться 
і в іншому, оскільки вони ділять ті самі об'єкти.

```python
# Створення оригінального deque
original_deque = deque([1, 2, 3])

# Створення копії
deque_copy = original_deque.copy()

# Виведення обох deque
print("Оригінал:", original_deque)
print("Копія:", deque_copy)

# Додавання елементу до копії
deque_copy.append(4)

# Виведення обох deque після модифікації копії
print("Оригінал після модифікації копії:", original_deque)
print("Копія після додавання елемента:", deque_copy)
```
**Особливості поверхневої копії:**

- **Незмінні об'єкти**: Для незмінних типів даних, таких як числа та рядки, поверхнева копія ефективно діє як 
глибока копія.
- **Змінні об'єкти**: Якщо елементи в deque є списками або іншими змінними типами, то зміни в цих елементах
відображатимуться в обох deque (оригінальному та копії), оскільки вони ділять ті самі внутрішні об'єкти.
Тому важливо розуміти відмінності між поверхневою та глибокою копіями, особливо при роботі зі складними
структурами даних, що містять змінні об'єкти.

6. Count(x):

Підрахунок кількості елементів, які дорівнюють х в об`єкті deque.

```python
d = deque(['a', 'b', 'c', 'a', 'b', 'b'])
print(d.count('b'))  # 3
```
