from TASKS.LAMBDA.LAMBDA_READY import *


def test_task1():
    assert task1(10) == 25


def test_task1_1():
    assert task1_1(12, 4) == 48


def test_task2():
    assert task2_quares == 30


def test_task3():
    assert list_task3 == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


def test_task4():
    assert task4 == [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
                     {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
                     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]


def test_task5_even():
    assert task5_even == [2, 4, 6, 8, 10]


def test_task5_odd():
    assert task5_odd == [1, 3, 5, 7, 9]


def test_tasks6():
    assert square_nums6 == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def test_task6_1():
    assert cube_nums6 == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


def test_task7():
    assert task7('Python') is True, task7('Java') is False


task9_assert_true = ['26587', '4.2365', '00', '001']
task9_assert_false = ['-12547', 'A001']


def test_task8():
    assert [x for x in task9_assert_true if is_num(x) is True] == task9_assert_true


def test_task9():
    assert [x for x in task9_assert_false if is_num(x) is False] == task9_assert_false


def test_task10():
    assert is_num9('-16.4') and is_num9('-16324.4') is True


def test_task10_1():
    assert fib_series(2) == [0, 1], fib_series(9) == [0, 1, 1, 2, 3, 5, 8, 13, 21]


def test_task11():
    assert task11 == [1, 2, 8, 9]


def test_task12():
    assert task12 == [2, 5, 7, 8, 9, -10, -3, -1]


def test_task13():
    assert odd_ctr == 5, even_ctr == 3


def test_task14():
    assert task14 == ['Monday', 'Friday', 'Sunday']


def test_task15():
    assert task15 == [5, 7, 9]


def test_task16():
    assert task16 == [19, 65, 57, 39, 152, 190]


def test_task17():
    assert task17 == ['php', 'aaa']


def test_task18():
    assert task18 == ['bcda', 'cbda', 'adcb']


def test_task19():
    assert task19 == [20, 23, 56]


def test_task20():
    assert task20 == '4 8 12 18 22'


def test_task21():
    assert task21 == 16


def test_task22():
    assert summ_positive == 48, summ_negative == -32


def test_task23():
    assert max_length_list(list_23) == (3, [13, 15, 17]), min_length_list(list_23) == (1, [0])


def test_task24():
    assert sort_sublists(color1) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


def test_task25():
    assert sort_sublists25(list25) == [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]


def test_task26():
    assert max_val(list_26) == 5
