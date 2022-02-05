# print((lambda x: x + 1)(3))
#
# new = lambda x: x + 1
# print(new(2))
#
# full_name = lambda first_name, last_name: f'{first_name} {last_name}'
# print(full_name('Serhii', 'Strupnitskyi'))
#
# new2 = lambda x, y: x+y
# print(new2(3, 4))

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))

new3 = lambda *args: sum(args)(1,2,3)
print(new3)
new4 = lambda **kwargs: sum(kwargs.values())(one=1, two=2, three=3)
print(new4)
new5 = lambda x, *, y=0, z=0: x + y + z(1, y=2, z=3)
print(new5)
even = lambda x: x%2 == 0
print(list(filter(even, range(11))))