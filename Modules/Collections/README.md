# Collections
___

Модуль collections в Python — це вбудований модуль, який містить спеціалізовані типи даних, що доповнюють стандартні 
типи даних, такі як **dict**, **list**, **set**, та **tuple**. Він призначений для роботи з колекціями даних
і пропонує альтернативи з більш високим рівнем продуктивності або зручності використання в певних сценаріях.

## Counter

Клас **Counter** з модуля collections у Python – це спеціалізований підклас **dict**, призначений для підрахунку 
**хешованих** об'єктів. Він особливо корисний, коли потрібно підрахувати елементи в ітерабельному об'єкті 
(наприклад, у списку або рядку) або коли потрібно визначити частоту виникнення окремих елементів.

Основні характеристики Counter:
- Елементи зберігаються як ключі словника, а їх кількість – як значення.
- Підрахунок елементів відбувається автоматично при створенні Counter.
- Можна легко додавати або віднімати елементи, об'єднувати лічильники, а також виконувати інші операції, специфічні для підрахунку.

## Deque
**deque** (вимовляється як "deck") є скороченням від **"double-ended queue"** (двостороння черга) і представляє собою 
тип даних, який дозволяє ефективно додавати та видаляти елементи з обох кінців. 
В Python, deque реалізовано в модулі collections.

Основні характеристики deque:
Швидкість додавання та видалення елементів: deque оптимізовано для швидкого додавання та видалення елементів
з початку чи кінця, забезпечуючи операції за константний час, тобто O(1).
Гнучкість: може бути використано для реалізації стеків або черг, залежно від потреби додавати або видаляти елементи.
Обмеження розміру: deque можна налаштувати з максимальною довжиною, так що коли новий елемент додається до 
переповненого deque, протилежний кінець автоматично видаляється.

Приклад використання deque:
```python
from collections import deque

# Створення deque
d = deque([1, 2, 3])

# Додавання елементів
d.append(4) # Додає елемент до кінця
d.appendleft(0) # Додає елемент до початку

# Видалення елементів
d.pop() # Видаляє та повертає елемент з кінця
d.popleft() # Видаляє та повертає елемент з початку

# Приклад обмеженого розміру deque
limited = deque(maxlen=3)
limited.append(1)
limited.append(2)
limited.append(3)
limited.append(4) # Додає 4, видаляє 1, тепер limited містить [2, 3, 4]

print(d)
print(limited)

```