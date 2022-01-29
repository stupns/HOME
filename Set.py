"""
Множина (set) це контейнер, що містить унікальні елементи в довільній послідовності.
Створити множину можна з допомогою функції set, фігурних душок або генератора множин
"""
print(set())
print(set('word'))
new_set = {'w', 'd', 'r', 'r'}
print(new_set)
set_gen = {i**2 for i in range(3)}
print(set_gen)

""" Isdisjoint . Метод set.isdisjoint(other) повертає True , якщо set i other не мають спільних елементів."""

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = {1, 8}

print(f'Isdisjoint: {s1.isdisjoint(s2)}')
print(f'Isdisjoint: {s1.isdisjoint(s3)}')

""" Issubset. Метод set.issubset(other) повертає True, якщо всі елемента set належать other."""

print(f'Issubset: {s1.issubset(s2)}')
print(f'Issubset: {s1.issubset(s3)}')

""" Difference. Метод set.difference(other, ...) повертає елементи із set, які не належать ні одному з other."""

a1 = {1, 2, 5, 15}
a2 = {1, 2, 3, 4}
a3 = {15, 8}
print(f'Difference: {a1.difference(a2, a3)}')

""" Symmetric_difference. Метод set.symmetric_difference(other) повертає елементи обох множин, які ж лише в одній 
 множині, але немає в іншій. """

print(f'Symmetric_difference: {a1.symmetric_difference(a2)}')

""" Discard. Метод set.discard(x) видаляє елемент х, якщо він знаходиться в множині set. Якщо елементу немає, то виняток
не виникає (як з випадком remove).
"""

b = {1, 2, 5, 15}
print(f'Discard: {b.discard(10)}')



word1 = 'насос'
word2 = 'сосна'

def anagram(word1, word2):
    if len(word1) == len(word2):
        word1 = set(word1)
        word2 = set(word2)
        result = word1.issubset(word2)
        return result
    else:
        return False



print(anagram(word1, word2))