# a = 10
#
#
# def some_func():
#     b_num = 11
#     print(dir())
#
#
# some_func()
# print(dir())
#
# def outer_func():
#     c_num = 12
#     def inner_func():
#         d_num = 13
#         print(dir(), ' - names in inner_func')
#     e_num = 14
#     inner_func()
#     print(dir(), ' - names in outer_func')
#
# outer_func()

#_____________________________________________________________

a_num = 10
b_num = 11


def outer_func():
    global a_num
    a_num = 15
    b_num = 16
    def inner_func():
        a_num = 20
        b_num = 21
        print('a_num inside inner_func :', a_num)
        print('b_num inside inner_func :', b_num)
    inner_func()
    print('a_num inside outer_func :', a_num)
    print('b_num inside outer_func :', b_num)

outer_func()