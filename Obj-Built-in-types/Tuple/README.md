TUPLE - (Кортежі)
===============
**Тип даних**: *immutable*.

**Кортеж** — немутабельна впорядкована послідовність.
Зазвичай кортежі використовуються для зберігання різнотипних даних (або однотипних, але які логічно представляють різні
сутності).

Кортежі представлені класом tuple. Кортежі підтримують усі загальні для усіх послідовностей операції.

_Яким чином вказати що об’єкт є кортежем, який складається з одного елементу?_

- Щоб вказати, що об’єкт є кортежем, потрібно після елементу вказати символ **‘,‘ (кома)**. Якщо не вказати коми,
то об’єкт буде сприйматись як **число**.

___

**Створення кортежів:**
| **Cпосіб**                                                                                	| **Приклад**           	|
|-------------------------------------------------------------------------------------------	|-----------------------	|
| Перераховування елементів в круглих дужках, якщо елемент один, після нього ставиться кома 	| _(1,)_                	|
| Перераховування елементів через кому                                                      	| _1, 2, 'some string'_ 	|
| Порожній кортеж                                                                           	| _()_                  	|
| Використання конструктора класа                                                           	| _tuple(range(8))_     	|