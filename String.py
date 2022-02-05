last_name = ' Ser hii '
first_name = 'Stupnsss'
txt = f'hello my name is {last_name} {first_name}'
year_born = str(1996)
dict_info = {'city': 'Lviv', 'country': 'Ukraine'}

# Old styles string formating
print('Hello, %s %s' % (last_name, first_name))

# New styles string formating

print(f'Hello, {last_name} {first_name}')

print('Hello, {} {}'.format(last_name, first_name))

# rstrip, lstrip, strip - видалення пробілів справа, зліва, цілком

rstrip_str = last_name.rstrip()
print(f'rstrip() {rstrip_str}.')

lstrip_str = last_name.lstrip()
print(f'lstrip() {lstrip_str}.')

strip_str = last_name.strip()
print(f'strip() {strip_str}.')

# find() rfind()
find_str = last_name.find(' ')
print(f'find(): {find_str}.')  # порядковий номер першого співпадіння

rfind_str = last_name.rfind(' ')
print(f'rfind(): {rfind_str}.')  # порядковий номер останнього співпадіння

# index() rindex()
index_str = first_name.index('s')
print(f'index(): {index_str}.')  # порядковий номер першого співпадіння

rindex_str = first_name.rindex('s')
print(f'index(): {rindex_str}.')  # порядковий номер останнього співпадіння

# replace()
replace_str = last_name.replace('Ser ', 'serg')
print(f'replace(): {replace_str}.')  # порядковий номер останнього співпадіння

# split() - розбиття речення по знайденому аргументу, як список
split_str = txt.split(' ')
print(f'split_str(): {split_str}.')

# isdigit() - входження чисел в строці - True \ False
isdigit_str = txt.isdigit()
print(f'isdigit_str(): {isdigit_str}.')

# isalpha() - входження символів в строці - True \ False (пробел та інші, видаватимуть False)
isalpha_str = first_name.isalpha()
print(f'isalpha_str(): {isalpha_str}.')

# isalnum() - входження символів або чисел в строці - True \ False (пробел та інші, видаватимуть False)
isalnum_str = txt.split()
isalnum_str = ''.join(isalnum_str).isalnum()
print(f'isalnum_str(): {isalnum_str}.')

# capitalize() - конвертує перший символ в верхній регістр
capitalize_str = txt.capitalize()
print(f'capitalize(): {capitalize_str}.')

# casefold() - конвертує перший символ в нижній регістр
casefold_str = txt.casefold()
print(f'casefold(): {casefold_str}.')

# count() - кількість входжень
count_str = first_name.count('s')
print(f'count() `s` in {first_name} : {count_str}.')

# endswith() - перевіряє закінчення строки на вказаний аргумент
endswith_str = txt.endswith('.')
print(f'endswith() last symbol `.` in txt : {endswith_str}.')

# isidentifier() method returns True if the string is a valid identifier, otherwise False
# A valid identifier cannot start with a number, or contain any spaces.
isidentifier_str = txt.split()
isidentifier_str = ''.join(isidentifier_str).isidentifier()
print(f'isidentifier(): {isidentifier_str}.')

# isnumeric() method returns True if all the characters are numeric
isnumeric_str = year_born.isnumeric()
print(f'isnumeric() in {year_born}: {isnumeric_str}.')

# isspace() якщо є будь який символ крім спейсу - поверне фолс
isspace_str = txt.isspace()
print(f'isspace() full in txt: {isspace_str}.')

# istitle()  method returns True if all words in a text start with a upper case letter
istitle_str = txt.istitle()
print(f'istitle() all words starts to uppercase in txt: {istitle_str}.')

# join() Join all items in a tuple\dict into a string, using a any character as separator
join_str = txt.join(dict_info)
print(f'join() : {join_str}.')

# maketrans() replace all characters to characters
maketrans_str = txt.maketrans('Hello', 'ALOHA')
# and add translate method:
print(f'maketrans() : {txt.translate(maketrans_str)}.')

# startswith(), endswith()
startswith_str = txt.startswith('H')
endswith_str = txt.endswith('s')
print(f'startswith() `H` in txt : {startswith_str}, and endswith() `s` in txt : {endswith_str}.')

# partition() rpartition() - Returns a tuple where the string is parted into three parts (first and last)
partition_str = txt.partition('s')
rpartition_str = txt.rpartition('s')
print(f'partition() `s` in txt : {partition_str}, and rpartition() `s` in txt : {rpartition_str}.')
