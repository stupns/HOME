SETS
===============
**Тип даних**: *mutable*.

**Задачі**: 

- [sets-tasks](https://github.com/stupns/HOME/blob/master/TASKS/SETS/SETS_READY.py "Sets tasks")

- [sets-Comprehension](https://github.com/stupns/HOME/blob/master/Comprehension/SetComprehension.py "Sets Comprehension")

**Sets** — це невпорядкована сукупність елементів. Кожен елемент набору унікальний (без дублікатів) і повинен бути незмінним
(не може бути змінений).

Однак сам набір є змінним. Ми можемо додавати або видаляти елементи з нього.

Набори також можна використовувати для виконання математичних операцій із наборами,
таких як об’єднання, перетин, симетрична різниця тощо.

___

# <p align=center>Python Set Operations</p>

Набори можна використовувати для виконання математичних операцій із наборами, таких як об’єднання, перетин, різниця та 
симетрична різниця. Ми можемо зробити це за допомогою операторів або методів.

Розглянемо наступні два набори для наступних операцій

``` 
>>> A = {1, 2, 3, 4, 5}
>>> B = {4, 5, 6, 7, 8}
```

___

## Set Union

![sets-union](https://github.com/stupns/HOME/blob/master/images-git/set-union.webp)

Об'єднання A і B - це множина всіх елементів обох множин.

Об'єднання виконується за допомогою **|** оператора. Те ж саме можна зробити за допомогою методу **union()**.

``` 
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

>>> print(A | B)

# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# use union function
>>> A.union(B)

# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# use union function on B
>>> B.union(A)

# Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

## Set Intersection

![sets-intersection](https://github.com/stupns/HOME/blob/master/images-git/set-intersection.webp)

Перетин A і B - це множина елементів, спільних в обох множинах.

Перетин виконується за допомогою оператора **&**. Те ж саме можна зробити за допомогою методу **intersection()**.

``` 
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

>>> print(A & B)

# Output: {4, 5}

# use intersection function on A
>>> A.intersection(B)

# Output: {4, 5}

# use intersection function on B
>>> B.intersection(A)

# Output: {4, 5}
```

## Set Difference

![sets-difference](https://github.com/stupns/HOME/blob/master/images-git/set-difference.webp)

Відмінність множини **B** від множини **A(A - B)** - це набір елементів, які знаходяться лише в A, але не в B.
Подібним чином B - A є набором елементів у B, але не в A.

Різниця виконується за допомогою оператора **-**. Те саме можна зробити за допомогою методу **difference()**.

``` 
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
>>> print(A - B)

# Output: {1, 2, 3}

# use difference function on A
>>> A.difference(B)

# Output: {1, 2, 3}

# use - operator on B
>>> B - A

# Output: {8, 6, 7}

# use difference function on B
>>> B.difference(A)

# Output: {8, 6, 7}
```

## Set Symmetric Difference

![set-symmetric-difference](https://github.com/stupns/HOME/blob/master/images-git/set-symmetric-difference.webp)

Симетрична різниця A і B — це набір елементів в A і B, але не в обох (за винятком перетину).

Симетрична різниця виконується за допомогою оператора **^**.
Те саме можна зробити за допомогою методу **symmetric_difference()**.

``` 
# Symmetric difference of two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
>>> print(A ^ B)

# Output: {1, 2, 3, 6, 7, 8}

# use symmetric_difference function on A
>>> A.symmetric_difference(B)

# Output: {1, 2, 3, 6, 7, 8}

# use symmetric_difference function on B
>>> B.symmetric_difference(A)

# Output: {1, 2, 3, 6, 7, 8}
```

___

# <p align=center>Other Python Set Methods</p>

Існує багато методів набору, деякі з яких ми вже використовували вище.
Ось список усіх методів, які доступні для набору об’єктів:

| Method                        	|                                            Опис                                            	|
|-------------------------------	|:------------------------------------------------------------------------------------------:	|
| **add()**                         	|                                   Додає елемент до набору                                  	|
| **clear()**                       	|                                Вилучає всі елементи з набору                               	|
| **copy()**                        	|                                    Повертає копію набору                                   	|
| **difference()**                  	|                   Повертає різницю двох чи більше наборів як новий набір                   	|
| **difference_update()**           	|                      Видаляє всі елементи іншого набору з цього набору                     	|
| **discard()**                     	| Вилучає елемент із набору, якщо він є членом. (Нічого не робити, якщо елемент не в наборі) 	|
| **intersection()**                	|                        Повертає перетин двох наборів як новий набір                        	|
| **intersection_update()**         	|                        Оновлює набір перетином самого себе та іншого                       	|
| **isdisjoint()**                  	|                    Повертає True, якщо два набори мають нульовий перетин                   	|
| **issubset()**                    	|                      Повертає True, якщо інший набір містить цей набір                     	|
| **issuperset()**                  	|                      Повертає True, якщо цей набір містить інший набір                     	|
| **pop()**                         	|    Вилучає та повертає довільний елемент набору. Викликає KeyError, якщо набір порожній    	|
| **remove()**                      	|           Вилучає елемент із набору. Якщо елемент не є членом, викликає KeyError           	|
| **symmetric_difference()**        	|                   Повертає симетричну різницю двох наборів як новий набір                  	|
| **symmetric_difference_update()** 	|              Оновлює набір за допомогою симетричної різниці між собою та іншим             	|
| **union()**                       	|                          Повертає об’єднання наборів у новий набір                         	|
| **update()**                      	|                           Оновлює набір об'єднанням себе та інших                          	|

___
# <p align=center> Built-in Functions with Set </p>

Вбудовані функції, такі як **all(), any(), enumerate(), len(), max(), min(), sorted(), sum()** тощо, зазвичай
використовуються з наборами для виконання різних завдань.

| Function    	|                                               Опис                                              	|
|-------------	|:-----------------------------------------------------------------------------------------------:	|
| **all()**       	|         Повертає True, якщо всі елементи множини є істинними (або якщо множина порожня).        	|
| **any()**      	|    Повертає True, якщо будь-який елемент множини є true. Якщо набір порожній, повертає False.   	|
| **enumerate()** 	| Повертає об'єкт перерахування. Він містить індекс і значення для всіх елементів набору як пари. 	|
| **len()**       	|                         Повертає довжину (кількість елементів) у наборі.                        	|
| **max()**       	|                              Повертає найбільший елемент у наборі.                              	|
| **min()**       	|                               Повертає найменший елемент у наборі.                              	|
| **sorted()**    	|         Повертає новий відсортований список з елементів у наборі (не сортує сам набір).         	|
| **sum()**       	|                              Повертає суму всіх елементів у наборі.                             	|

___

# <p align=center> Python Frozenset </p>

**Frozenset** — це новий клас, який має характеристики набору, але його елементи не можна змінити після призначення.
У той час як кортежі є незмінними списками, frozenset це незмінні набори.

Sets, будучи змінними, не хешуються, тому їх не можна використовувати як ключі словника. З іншого боку, frozensets
можна хешувати і їх можна використовувати як ключі до словника.

**Frozensets** можна створити за допомогою функції **frozenset()**.

Цей тип даних підтримує такі методи, як **copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(),
symmetric_difference() і union()**. Будучи незмінним, він не має методів, які додають або видаляють елементи.

``` 
# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

>>> A.isdisjoint(B)

# Output: False

>>> A.difference(B)

# Output: frozenset({1, 2})

>>> A | B

# Output: frozenset({1, 2, 3, 4, 5, 6})

>>> A.add(3)

# Output: 
...
AttributeError: 'frozenset' object has no attribute 'add'
```