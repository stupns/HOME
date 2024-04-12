import pytest
from TASKS.FUNCTION_EXERCISES.TASK_EXERCISE_1_READY import *


def test_even1_2():
    assert even_num == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 21]


def test_chunk_3():
    assert chunk(even_num, 3) == [[2, 4, 6], [8, 10, 12], [14, 16, 18]]


def test_chunk_valid_negative_inside_4():
    with pytest.raises(ValueError, match=r".* must be > 0 .*"):
        chunk(even_num, -3)


def test_check_chunk_negative_5():
    assert check_chunk_negative() is None


def test_chunk_for_chunks_6():
    assert chunk_for_chunks == [chunk for chunk in chunks]


def test_chunk_first_two_chunks_7():
    assert square_first_two_chunks(chunks) == [[4, 16, 36], [64, 100, 144], [14, 16, 18]]


def test_merged_chunks_8():
    assert merge_chunks(chunks) == [4, 16, 36, 64, 100, 144, 14, 16, 18]
