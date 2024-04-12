elem = [10, '30', 30, 10, '56']
unique_vlans = {int(vlan) for vlan in elem}
print(unique_vlans)

# Example 1
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newSet = {element*3 for element in myList if element % 2 == 0}
print(f'1 - {newSet}')

# Example 2
mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSet2 = {str(element) for element in mySet}
print(f'2 - {newSet2}')

# Example 3
newSet3 = {var: var ** 3 for var in myList if var % 2 != 0}
print(f'3 - {newSet3}')

# Example 4
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
newSet4 = {key: value for (key, value) in zip(state, capital)}
print(f'4 - {newSet4}')

# Example 5
sentence = "The cat in the hat had two sidekicks, thing one and thing two."
words = sentence.lower().replace('.', '').replace(',', '').split()
newSet5 = {word.capitalize() if word[0] == 'h' else word for word in words}
newSet5_3 = {word.capitalize() if word[0] == 'h' else word for word in words if len(word) <= 3}
print(f'5 - {newSet5}\n5_3 - {newSet5_3}')
