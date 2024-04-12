# Sets
"""
Множина (set) це контейнер, що містить унікальні елементи в довільній послідовності.
Створити множину можна з допомогою функції set, фігурних душок або генератора множин.
"""
# region 1. Default set
set_word = set('word')
new_set = {'w', 'd', 'r', 'r'}
set_gen = {i ** 2 for i in range(3)}
print(f'1.1 set(): {set()},'
      f'\n1.2 set(`word`): {set_word},'
      f'\n1.3 set(`w`, `d`, `r`, `r`): {new_set},'
      f'\n1.4 i ** 2 for i in range(3): {set_gen}'
      )
# endregion

# region 2 .isdisjoint()
""" Isdisjoint . Метод set.isdisjoint(other) повертає True , якщо set i other не мають спільних елементів."""

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = {1, 8}
print(f'\ns1: {s1},\ns2: {s2},\ns3: {s3}\n')
print(f'2.1 Isdisjoint: s1.isdisjoint(s2) - {s1.isdisjoint(s2)}')
print(f'2.2 Isdisjoint: s1.isdisjoint(s3) - {s1.isdisjoint(s3)}')
# endregion

# region 3 .issubset()
""" Issubset. Метод set.issubset(other) повертає True, якщо всі елемента set належать other."""

print(f'3.1 Issubset: s1.issubset(s2) - {s1.issubset(s2)}')
print(f'3.2 Issubset: s1.issubset(s3) - {s1.issubset(s3)}')
# endregion

# region 4 .difference()
""" Difference. Метод set.difference(other, ...) повертає елементи із set, які не належать ні одному з other."""

a1 = {1, 2, 5, 15}
a2 = {1, 2, 3, 4}
a3 = {15, 8}

print(f'\na1: {a1},\na2: {a2},\na3: {a3}')
print(f'4 Difference: a1.difference(a2, a3) - {a1.difference(a2, a3)}')
# endregion

# region 5 .symmetric_difference()
""" Symmetric_difference. Метод set.symmetric_difference(other) повертає елементи обох множин, які є лише в одній 
 множині, але немає в іншій. """

print(f'5 Symmetric_difference: a1.symmetric_difference(a2) - {a1.symmetric_difference(a2)}')
# endregion

# region 6 .discard()
""" Discard. Метод set.discard(x) видаляє елемент х, якщо він знаходиться в множині set. Якщо елементу немає, то виняток
не виникає (як з випадком remove).
"""

print(f'Discard: a1.discard(10) - {a1.discard(10)}')
# endregion

def anagram(first_w, second_w):
    if len(first_w) == len(second_w):
        set_words = set(first_w)
        diff_set_word = set(second_w)
        result = set_words.issubset(diff_set_word)
        return result
    else:
        return False


if __name__ == '__main__':
    word = 'насос'
    diff_word = 'сосна'
    print(f'Anagram({word},{diff_word}) - {anagram(word, diff_word)}')
