n = 300
m = n
# print(id(n))
# print(id(m))

# ____

code_picked = (5, 9, 0, 3)
code_attempt1 = (9, 5, 0, 3)
code_attempt2 = (5, 9, 0, 3)
unhashable_set = {1, 3, 4, 5, 4}
unhashable_dict = {1: 'hello', 2: 3.14}
unhashable_lst = [12, 4, 'hello', [21, 44]]

stored_code = hash(code_picked)
hashed_attempt1 = hash(code_attempt1)
hashed_attempt2 = hash(code_attempt2)
# print(hash(unhashable_set))
# print(hash(unhashable_dict))
# print(hash(unhashable_lst))

# print(stored_code)
# print(hashed_attempt1)
# print(hashed_attempt2)

stored_code == hashed_attempt1
# print(stored_code == hashed_attempt2)
