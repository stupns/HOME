"""
Как должен вести себя Singleton при создании повторного экземпляра?
- ругаться исключением
- отдать единтсвенный экземпляр без запуска нового констркутора
- отдать единтсвенный экземпляр с запуском нового констркутора
  (! тогда нужно учесть как это отразится на уже созданных связанных объектах внутри, в общем нужно быть аккуратным !)
"""

# # подход к созданию одиночки с вызовом конструктора этого же экземпляра при создании нового объекта-ссылки на одиночку
import sqlite3


class Singleton1(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        # запуск нового конструктора этого же экземпляра
        # при повторной попытке создать экземпляр одиночки
        # (фактически при получении нового объекта-ссылки на одиночку в нужном месте программы)
        print('! Singleton1.__init__ !')
        self.x = args[0]
        self.y = kwargs['y']


s = Singleton1(1, y=2)
print("Object created", s, s.__dict__)
ss = Singleton1(10, y=20)
print("Object created", ss, ss.__dict__)

# out:
'''
! Singleton1.__init__ !
Object created <__main__.Singleton1 object at 0x00C11FD0> {'x': 1, 'y': 2}
! Singleton1.__init__ !
Object created <__main__.Singleton1 object at 0x00C11FD0> {'x': 10, 'y': 20}
'''


# подход к созданию одиночки без вызова конструктора этого же экземпляра каждый раз при создании нового объекта-ссылки
# на одиночку
class MetaSingleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = type.__call__(cls, *args, **kwargs)
        return cls._instance


class Singleton2(metaclass=MetaSingleton):
    def __init__(self, *args, **kwargs):
        # полное игнорирование новых аргументов конструктора
        # т.к. сюда даже не попадаем при повторном создании экземпляра одиночки
        print('! Singleton2.__init__ !')
        self.x = args[0]
        self.y = kwargs['y']


s = Singleton2(1, y=2)
print("Object created", s, s.__dict__)
ss = Singleton2(10, y=20)
print("Object created", ss, ss.__dict__)

# out:
'''
! Singleton2.__init__ !
Object created <__main__.Singleton2 object at 0x00C3EAF0> {'x': 1, 'y': 2}
Object created <__main__.Singleton2 object at 0x00C3EAF0> {'x': 1, 'y': 2}
'''

# Practical singleton

'''Мы создали метакласс по имени MetaSingleton. Как мы объясняли в предыдущем разделе, специальный метод __call__ 
используется в метаклассе для создания Singleton. Класс Database создан с помощью метакласса MetaSingleton и является 
синглтон. Таким образом, когда создается экземпляр класса Database, он создает только один объект. Когда 
веб-приложение хочет выполнить определенные операции с БД, оно несколько раз создает экземпляр класса Database (в 
качестве примера, например в разных частях приложения), но создается только один объект. Поскольку существует только 
один объект, обращения к базе данных синхронизируются. Кроме того, такой подход позволяет ограничить использование 
системных ресурсов, и мы можем избежать ситуации нехватки памяти или ресурсов процессора. '''


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def __init__(self):
        self.cursorobj = self.connection.cursor()

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("../../db.sqlite3")
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()
print("Database Objects DB1", db1)
print("Database Objects DB2", db2)

# Practical Singletone

'''В следующем коде объекты hc1 и hc2 являются экземплярами класса в Singleton. Серверы добавляются в инфраструктуру 
для проверки работоспособности с помощью метода addServer(). В начале выполняется, итерация проверки 
работоспособности для этих серверов. Затем метод changeServer() удаляет последний сервер и добавляет новый. А затем, 
когда снова запускается проверка во второй итерации то используется уже измененный список серверов. '''


class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

    @property
    def servers(self):
        return self._servers


hc1 = HealthCheck()
hc2 = HealthCheck()
hc1.addServer()
print("Schedule health check for servers (1)..")
for i in range(4):
    print("Checking ", hc1.servers[i])
hc2.changeServer()
print("Schedule health check for servers (2)..")
for i in range(4):
    print("Checking ", hc2.servers[i])
