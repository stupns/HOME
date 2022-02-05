# Dicts__________________________________________________________________________________________________________

new_dict = {'color': 'green',
            'points': 5}

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

show_all_items = [elem for elem in new_dict.items()]
show_all_values = [elem for elem in new_dict.values()]
show_all_keys = [elem for elem in new_dict.keys()]
new_dict_point = new_dict['points']

print(f'Show all items :{show_all_items}\n'
      f'Show all values :{show_all_values}\n'
      f'Show all keys :{show_all_keys} \n'
      f'Points have item points :{new_dict_point} \n')
#
# print(155 * "-" + '\n')
#
# # get() method return value of the argument keys
# method_get_value = new_dict.get('color')
# method_get_key = list(new_dict.keys())[-1]
#
# print(f'get() : value -> {method_get_value}, key -> {method_get_key}\n')
#
# # 1 method output key and value
# first_key = list(new_dict.keys())[list(new_dict.values()).index('green')]
# second_key = list(new_dict.keys())[list(new_dict.values()).index(5)]
# first_value, second_value = new_dict['color'], new_dict['points']
#
# print(f'This {first_value} {first_key} have {second_value} {second_key}.\n')
#
# # 2 method output key and value with cycle for
# for key, value in new_dict.items():
#     print(f'Using cycle for - {key} : {value} \n')
#
# print(155 * "-" + '\n')
#
# # 3 method output key and value
# example_filter_key = [key for key, value in new_dict.items() if value == 5]
# example_filter_value = [value for key, value in new_dict.items() if key == 'color']
#
# print(f'List comprehension: {example_filter_key[0]}\n'
#       f'List comprehension: {example_filter_value[0]}\n')
#
# # Filter a Dictionary by keys in Python using dict comprehension
#
# filtered_dictionary_keys = {key: value for (key, value) in dict_for_filter_key.items() if key > 5}
# new_filter_correct_key = filtered_dictionary_keys.get(453)
#
# print(f'Using condition len > 5 for all elem dicts:'
#       f' {filtered_dictionary_keys}, and get(453) :'
#       f' {new_filter_correct_key}')
#
# # Filter a Dictionary by values in Python using dict comprehension
#
# filtered_dictionary_values = {key: value for (key, value) in dict_for_filter_value.items() if value >= 45}
# new_filter_correct_value = filtered_dictionary_values['five']
#
# print(f'Using condition len => 45 for values elem dicts: '
#       f'{filtered_dictionary_values}, and get[`five`]: '
#       f'{new_filter_correct_value}\n')
#
# print(155 * "-" + '\n')
#
# # Methods :
# # Clear() method removes all the elements from a dictionary.
# new_dict.clear()
# print(f'Clear() new_dict : {new_dict}\n')
#
# # Copy() method returns a copy of the specified dictionary.
# new_dict = dict_for_filter_key.copy()
# print(f'Copy() id dict_for_filter : {id(dict_for_filter_key)} and id copy dict : {id(new_dict)} \n'
#       f'print copy dict : {new_dict}\n')
#
# # Fromkeys() method returns a dictionary with the specified keys and the specified value.
# x = ('key1', 'key2', 'key3')
# y = 0
#
# example_dict = dict.fromkeys(x, y)
# print(f'Fromkeys(x,y) : {example_dict}')
#
# # Such as u can fill keys None`s
# example_dict = dict.fromkeys(x)
# print(f'Fromkeys(x) with Nones : {example_dict}\n')
#
# # Popitem() removes last elements in dict (if use pop('key3') need print key)
# example_dict.popitem()
# print(f'Popitem() : {example_dict}')
#
# # Update() method inserts the specified items to the dictionary.
# example_dict.update({'key3': None})
# print(f'Update() : {example_dict}')
