elements = (200, 50)
print(id(elements))

#add new elements in tuple
new_elements = list(elements)
new_elements.append(10)
elements = tuple(new_elements)
print(id(elements))

#print all elements
new_tuple = ('one', 'two', 'three')

for i in range(len(new_tuple)):
    print(f'Range all elements in tuple: {new_tuple[i]}')
