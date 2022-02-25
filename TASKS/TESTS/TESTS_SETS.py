from TASKS.SETS.SETS_READY import *


def test_task1():
    assert empty_set == {}
    assert non_empty_set == {0, 1, 2, 3, 4}
    assert set_literal == {1, 2, 3, 'foo', 'bar'}


def test_task2():
    """ 0 1 2 3 4 5"""
    pass


def test_task3():
    assert color_set == {'Green', 'Red', 'Blue'}


def test_task4():
    assert num_set4 == {1, 2, 3, 4, 5}


def test_task5():
    assert num_set5 == {0, 1, 2, 3}


def test_task6():
    assert task6 == {"blue"}


def test_task7():
    assert task7_1, task7_2 == {1, 2, 3, 4, 5, 6, 7, 8, 9}


def test_task8():
    assert task8_1, task8_2 == {2, 3, 4}


def test_task9():
    assert task9_1, task9_2 == {2, 3, 4, 6, 7, 8, 9}


def test_task10():
    new_l = [task10_xy, task10_yz, task10_xz]
    comprehen = [x for x in new_l if x is True]
    assert comprehen == []
    assert task10_zy, task10_subset is True


def test_task11():
    pass


def test_task12():
    pass


def test_task13():
    pass


def test_task14():
    pass


def test_task15():
    pass


def test_task16():
    pass


def test_task17():
    pass


def test_task18():
    pass


def test_task19():
    pass


def test_task20():
    pass
