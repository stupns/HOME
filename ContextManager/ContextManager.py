import sqlite3
from contextlib import contextmanager
from urllib.request import urlopen

'''
with open(path, 'w') as f_obj:
    f_obj.write(some_data)
'''

# 0. Classic File create contextmanager using magic method

class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f'Opening the file {self.filename}.')
        self.__file = open(self.filename, self.mode)
        return self.__file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f'Closing the file {self.filename}.')
        if not self.__file.closed:
            self.__file.close()

        return False


with File('../Obj-Built-in-types/Dicts/Dicts.py', 'r') as f:
    print(int(next(f)))


# 1. Classic Class create contextmanager using magic method

class Resource:
    def __init__(self, name):
        print('Resource: create {}'.format(name))
        self.__name = name

    def get_name(self):
        return self.__name

    def post_work(self):
        print('Resource: close')


# create contextmanager
class ResourceForWith:
    def __init__(self, name):
        self.__resource = Resource(name)

    def __enter__(self):
        return self.__resource

    def __exit__(self, type, value, traceback):
        self.__resource.post_work()


with ResourceForWith('Worker') as r:
    print(r.get_name())

"""
1 Оператор with зберігає метод __exit__ классу ResourceForWith.
2. Викликається метод __enter__ классу ResourceForWith.
3. __enter__ запам'ятовує переданий об'єкт.
4. Дескриптор передается в змінну r.
5. Викликається метод повернення об'єкту.
6. Викликається  метод __exit__, який закриває файл з виводом повідомлення з методу post_work.
"""

# # 2. Classic Class create contextmanager using magic method for DB connection
# class DataConn:
#
#     def __init__(self, db_name):
#         self.db_name = db_name
#
#     def __enter__(self):
#         self.conn = sqlite3.connect(self.db_name)
#         return self.conn
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.conn.close()
#         if exc_val:
#             raise
#
#
# if __name__ == '__main__':
#     db = 'test.db'
#
#     with DataConn(db) as conn:
#         cursor = conn.cursor()
#
# #create decorator_______________________________________________
#
# @contextmanager
# def file_open(path):
#     try:
#         f_obj = open(path, 'w')
#         yield f_obj
#     except OSError:
#         print("We had an error!")
#     finally:
#         print('Closing file')
#         f_obj.close()
#
#
# if __name__ == '__main__':
#     with file_open('test.txt') as fobj:
#         fobj.write('Testing context managers')
#
#
# # close
# @contextmanager
# def closing(db):
#     try:
#         yield db.conn()
#     finally:
#         db.close()
#
#
# # close 2 method
#
# with closing(urlopen('http://www.google.com')) as webpage:
#     for line in webpage:
#         # обрабатываем строку...
#         pass
