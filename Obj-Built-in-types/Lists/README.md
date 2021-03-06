LISTS
===============
**Тип даних**: *mutable*.

**Задачі**: [list-comprehension-tasks.](https://github.com/stupns/HOME/blob/master/TASKS/COMPREHENSION/COMPREHENSION_READY.py "List comprehension")

**Список** — змінна послідовність із впорядкованими елементами.
Під капотом списки представлені як масив.

**```list([iterable])```**

Елементами списків можуть бути будь-які об'єкти.
___
**<p align=center>Об'явлення</p>**

___
У коді списки можуть бути оголошені за допомогою квадратних дужок - 
[] - усередині дужок через кому перераховуються елементи в потрібній послідовності.

```
my_empty_list = list()
my_empty_list = []
my_list = [1, 'some', 3.5]
my_list = list(idx for idx in range(3))  # [0, 1, 2]
```

Крім того, можна оголосити їх за допомогою конструктора list().
___
**<p align=center>Заміна елементів</p>**

___

Для заміни значень використовується звернення індексу з наступним присвоєнням нового значення.

``` 
my_list = [1, 2, 3]
my_list[1] = 11  # [1, 11, 3]
my_list[10] = 22  # IndexError
```
___
**<p align=center>Видалення елементів</p>**

___

Для видалення зі списку одиночних елементів та зрізів може використовуватись інструкція del:

```
my_list = [1, 2, 3, 4, 5]
del my_list[0]  # [2, 3, 4, 5]
del my_list[:2]  # [4, 5]
del my_list[:]  # []
```
___
**<p align=center>Порівняння</p>**

___
Два списки, що порівнюються лексикографічно: вважаються рівними, якщо мають однакову довжину і
дорівнюють їх відповідні елементи:

```
a = [3, 2, 1]
b = [1, 2, 3]
d = [3, 2, 2]
e = [3, 2]
f = [3, 2, 'a']
a > b  # True
a > d  # False
d > b  # True
a > e  # True
a > f  # False
```
___
**<p align=center>Деталі реалізації CPython</p>**

___
Списки реалізовані за допомогою динамічних масивів (а не зв'язкових списків у стилі Lisp). У реалізації використовується
безперервний масив посилань на об'єкти, а на початку структури списку зберігається покажчик на цей масив та його довжина.
Такий підхід дозволяє звертатися до елементів за постійний час O(1) незалежно від довжини списку.

При додаванні або вставці нових елементів масив посилань змінює розмір. Спеціальне для випадків повторених додавань
елементів до списку масив нарощується таким чином, щоб зменшити ймовірність необхідності зміни розміру надалі
(наперед резервується додаткове місце). Тобто при додаванні елементів до списку відбувається нарощування слотів
(місця під поточні та майбутні елементи) в масиві. Розмір нарощування залежить від поточної кількості елементів,
прогресія: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88 і т.д
(при додаванні першого елемента, виділиться 3 додаткові слоти, при додаванні 17-го 8 слотів).

**При видаленні списку (наприклад, за допомогою del або збирача сміття), його спустошений об'єкт кешується
і використовується в подальшому для створення нового списку. Див. приклад нижче.**

___

Найбільші витрати відбуваються за необхідності доповнити список
(коли спочатку виділеної під нього пам'яті недостатньо, всі елементи доведеться перемістити в інше місце), або при
вставці/видаленні елемента близько до початку (наступні елементи потрібно перемістити назад).

<table style="{
    margin-left: auto;
    margin-right: auto;
}">

| Спосіб                       	| Складність          	|    Приклад                	|  Опис                                         	|
|------------------------	|------------	|--------------------	|-------------------------------------------	|
| Звернення по індексу   	| O(1)       	| l[i]               	|                                           	|
| Присвоєння             	| O(1)       	| l[i] = 0           	|                                           	|
| len                    	| O(1)       	| len(l)             	|                                           	|
| .append                	| O(1)       	| l.append(5)        	|                                           	|
| .pop                   	| O(1)       	| l.pop()            	| Те ж саме що і l.pop(-1) — викид з кінця. 	|
| .clear                 	| O(1)       	| l.clear()          	|                                           	|
| Зріз                   	| O(b-a)     	| l[a:b]             	|                                           	|
| .extend                	| O(k)       	| l.extend(a)        	|                                           	|
| Створення              	| O(k)       	| list(a)            	|                                           	|
| Перевірки ==, !=       	| O(n)       	| l1 == l2           	|                                           	|
| .insert                	| O(n)       	| l.insert(0, 5)     	|                                           	|
| del                    	| O(n)       	| del l[i]           	| Те ж саме що й з видаленням зрізу         	|
| .remove                	| O(n)       	| l.remove(...)      	|                                           	|
| Перевірка на входження 	| O(n)       	| x in l             	| Прохід по списку.                         	|
| .copy                  	| O(n)       	| l.copy()           	| Те ж саме що і l[:].                      	|
| .pop                   	| O(n)       	| l.pop(i)           	|                                           	|
| min, max               	| O(n)       	| min(l)             	|                                           	|
| .reverse               	| O(n)       	| l.reverse()        	|                                           	|
| Прохід                 	| O(n)       	| for v in l:        	|                                           	|
| Присвоэння зрізу       	| O(k+n)     	| l[... : ...] = ... 	|                                           	|
| .sort                  	| O(n log n) 	| l.sort()           	|                                           	|
| Множення               	| O(k×n)     	| i l                	|                                           	|
</table>