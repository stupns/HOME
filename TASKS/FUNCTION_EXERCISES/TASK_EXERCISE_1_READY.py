"""
1. Cтворити список з парних чисел від 1-21, і створити без ліст компрехеншн.
2. Добавити до списку 21.
3. Написати функцію, що приймаж список, 2 аргумент розмір. Результат повинен розбитим на вложений листи по розмірах.
4. Апгрейднути фнкцію по валідації від'ємного розміру.
5. Створити функцію для валідації від'ємного розміру.
6. Пробігтися по чанкам і прантанути всі групи окремо.
7. Створити функцію, що би брала перші 2 чанка і зводила до 2 степені.
8. Змерджити список до початкового стану.
"""
import pytest

from settings import test_path

# even_num = [x for x in list(range(2,99,2))]
even_num = list(range(2, 21, 2))
even_num.append(21)


def chunk(nums, chunk_size):
    nums_copy = nums.copy()
    last_chunk = []
    result = []
    if chunk_size < 0:
        raise ValueError(f'chunk_size must be > 0 (not {chunk_size})')
    while nums_copy:
        if len(last_chunk) == chunk_size:
            result.append(last_chunk)
            last_chunk = []
        last_chunk.append(nums_copy[0])
        del nums_copy[0]
    return result


def check_chunk_negative():
    try:
        chunk(even_num, -1)
    except ValueError:
        pass
    else:
        return False


check_chunk_negative()
chunks = chunk(even_num, 3)

chunk_for_chunks = [chunk for chunk in chunks]


def square_first_two_chunks(nums):
    i = 2
    if len(nums) < 2:
        i = len(nums)
    for j in range(i):
        nums[j] = [k ** 2 for k in nums[j]]
    return nums


def merge_chunks(nums):
    result = []
    for num in nums:
        result.extend(num)
    return result


pytest.main(['-rpP', test_path.TEST_CLASSES])
