import os

from pydantic import BaseSettings


class SettingsPath(BaseSettings):

    TEST_COMPREHENSION = str(os.path.join('../TESTS/TESTS_COMPREHENSION.py'))
    TEST_CLASSES = str(os.path.join('../TESTS/TESTS_CLASSES.py'))
    TEST_LAMBDA = str(os.path.join('../TESTS/TESTS_LAMBDA.py'))
    TEST_SETS = str(os.path.join('../TESTS/TESTS_SETS.py'))
    TEST_FUNCTION = str(os.path.join('../TESTS/TEST_FUNCTIONS/TESTS_TASK_EXERCISE_1.py'))


test_path = SettingsPath()
