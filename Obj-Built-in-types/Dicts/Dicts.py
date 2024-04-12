# Dicts
# region Condition
dict_info = {'full_name': 'Serhii Stupnytskyi',
             'age': 27}

dict_for_filter_key = {
    1: 'one',
    132: 'five',
    -23: 'second',
    453: 'six'}

dict_for_filter_value = {
    'one': 1,
    'five': 132,
    'second': -23,
    'six': 453}

print(155 * "-" + '\n')

# endregion

# region 1. Simple comprehension get items & values
show_all_items = [elem for elem in dict_info.items()]
show_all_values = [elem for elem in dict_info.values()]
show_all_keys = [elem for elem in dict_info.keys()]
show_age = dict_info['age']

print(f'1.1 Show all items :{show_all_items}\n'
      f'1.2 Show all values :{show_all_values}\n'
      f'1.3 Show all keys :{show_all_keys} \n'
      f'1.4 Age have item ages :{show_age} \n')

print(155 * "-" + '\n')

# endregion

# region 2. Methods .get() and .keys()
# get() method return value of the argument keys
get_value = dict_info.get('full_name')
get_keys = list(dict_info.keys())

print(f'2 .get() : value -> {get_value}, keys() -> {get_keys}\n')

# endregion

# region 3. Output key and value list and keys()

first_key = list(dict_info.keys())[list(dict_info.values()).index('Serhii Stupnytskyi')]
second_key = list(dict_info.keys())[list(dict_info.values()).index(27)]
first_value, second_value = dict_info['full_name'], dict_info['age']

print(f'3. This {first_value} {first_key} have {second_value} {second_key}.\n')

# endregion

# region 4. Output key and value with cycle for
for key, value in dict_info.items():
    print(f'4. Using cycle for - {key} : {value} \n')

print(155 * "-" + '\n')

# endregion

# region 5. Output keys and values with [list comprehension]
example_filter_key = [key for key, value in dict_info.items() if value == 27]
example_filter_value = [value for key, value in dict_info.items() if key == 'full_name']

print(f'5.1 List comprehension: {example_filter_key[0]}\n'
      f'5.2 List comprehension: {example_filter_value[0]}\n')

# endregion

# region 6. Filter a Dictionary by keys in Python using [dict comprehension]


filtered_dictionary_keys = {key: value for (key, value) in dict_for_filter_key.items() if key > 5}
new_filter_correct_key = filtered_dictionary_keys.get(453)

print(f'6.1 Using condition len > 5 for all elem dicts:'
      f' {filtered_dictionary_keys}, and get(453) :'
      f' {new_filter_correct_key}')

# endregion

# region 7. Filter a Dictionary by values in Python using [dict comprehension]

filtered_dictionary_values = {key: value for (key, value) in dict_for_filter_value.items() if value >= 45}
new_filter_correct_value = filtered_dictionary_values['five']

print(f'7. Using condition len => 45 for values elem dicts: '
      f'{filtered_dictionary_values}, and get[`five`]: '
      f'{new_filter_correct_value}\n')

print(155 * "-" + '\n')

# endregion

# METHODS:

# region 1 .clear()
# Clear() method removes all the elements from a dictionary.
dict_info.clear()
print(f'1 clear() new_dict : {dict_info}\n')

# endregion

# region 2 .copy()
# Copy() method returns a copy of the specified dictionary.
new_dict = dict_for_filter_key.copy()
print(f'2. copy() id dict_for_filter : {id(dict_for_filter_key)} and id copy dict : {id(new_dict)} \n'
      f'print copy dict : {new_dict}\n')

# endregion

# region 3 dict.fromkeys()
# Fromkeys() method returns a dictionary with the specified keys and the specified value.
x = ('key1', 'key2', 'key3')
y = 0

example_dict = dict.fromkeys(x, y)
print(f'3. dict.fromkeys(x,y) : {example_dict}')

# Such as u can fill keys None`s
example_dict = dict.fromkeys(x)
print(f'Fromkeys(x) with Nones : {example_dict}\n')

# endregion

# region 4 .popitem()
# Popitem() removes last elements in dict (if use pop('key3') need print key)
example_dict.popitem()
print(f'4 .popitem() : {example_dict}')

# endregion

# region 5 .update()
# Update() method inserts the specified items to the dictionary.
example_dict.update({'key3': None})
print(f'5 .update() : {example_dict}')

# endregion

# region 6 Merge Two Dictionaries
dict_merged = {**dict_for_filter_key, **dict_for_filter_value}
dict_merged_2 = dict_for_filter_key | dict_for_filter_value
print(f'6. Merged dicts : {dict_merged}, \nMerged using union operator: {dict_merged_2}')
# endregion
