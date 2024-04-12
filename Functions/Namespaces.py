a = 10
b = 11


def some_func():
    b = 11
    print(f'All scope inside func: {dir()}')


some_func()
print(f'All scope outside func: {dir()}')

print('\nExample 2: ')
def outer_func():
    global a_num
    a = 15
    b = 16

    def inner_func():
        a = 20
        b = 21
        print('a_num inside inner_func :', a)
        print('b_num inside inner_func :', b)

    inner_func()
    print('a_num inside outer_func :', a)
    print('b_num inside outer_func :', b)


outer_func()
