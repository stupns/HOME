import sqlite3
import os
from contextlib import contextmanager
from urllib.request import urlopen

'''
with open(path, 'w') as f_obj:
    f_obj.write(some_data)
'''


# 0. Classic Class create contextmanager using magic method


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

        return True


with File('../Obj-Built-in-types/Dicts/Dicts.py', 'r') as f:
    new = f.readlines()
    not_words = [" ", "", ","]
    simple_con = [word for sentence in new for word in sentence.split(' ') if word not in not_words]
    words_dict = [x for x in simple_con if 'dict' in x]

print('1. ')


# 1. The same Class create contextmanager using magic method


class Resource:
    def __init__(self, name):
        print('Resource: create {}'.format(name))
        self.__name = name

    def get_name(self):
        return self.__name

    def post_work(self):
        print('Resource: close')


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

print('\n2. ')


# 2. Classic Class create contextmanager using magic method for DB connection


class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


db = 'test.db'
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

if os.path.exists('test.db'):
    with DataConn(db) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT SQLITE_VERSION()')
        data = cursor.fetchone()[0]
        print(f"SQLite version: {data}")
        cursor.execute("DROP TABLE IF EXISTS cars;")
        cursor.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
        cursor.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
        cursor.execute("SELECT * FROM cars")
        while True:
            rows = cursor.fetchall()
            if rows is None:
                break
            for row in rows:
                print(f'{row[0]} {row[1]} {row[2]}')
            break

print('\n3. ')


# 3. Using @contextmanager for create and write file

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'a')
        yield f_obj
    except OSError:
        print('We had an error!')
    finally:
        print('Closing file')


if not os.path.exists('test.txt'):
    with open('test.txt', mode='w') as f:
        print('Write first line.')
        f.write('This text is written in python\n')
else:
    with file_open('test.txt') as f:
        print('Write next line in txt.file')
        f.write('Testing context managers\n')

print('\n4. ')


# 4. Connect and Close DB

@contextmanager
def closing(db):
    try:
        query = "SELECT SQLITE_VERSION()"
        db_obj = sqlite3.connect(db)
        cursor = db_obj.cursor()
        cursor.execute(query)
        data = cursor.fetchone()[0]
        print(f"SQLite version: {data}")
        yield db_obj
    finally:
        print(f'Closed')


db = 'test.db'
if os.path.exists('test.db'):
    with closing(db) as conn:
        print('Checking work')

print('\n5. ')
# 5. Read urls using contextmanager

with urlopen('http://www.google.com') as response:
    body = response.read()
    print(response.headers.get_content_charset())
