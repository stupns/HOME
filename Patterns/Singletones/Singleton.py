# classic creating singleton

"""В этом фрагменте кода мы переопределяем метод __new__ (специальный метод Python для создания объектов),
что бы управлять созданием объекта. Объект s создается с помощью метода __new__, но перед этим он проверяет,
существует ли уже созданный объект. Метод hasattr (специальный метод Python, позволяющий определить, имеет ли объект
определенное свойство), используется для проверки наличия у объекта cls свойства instance. При создание объекта s,
объект просто создается. В случае создания объекта s1, hasattr() обнаруживает, что у объекта уже существует свойство
instance, и, следовательно, s1 использует уже существующий экземпляр объекта (расположенный по адресу 0x10ba9db90). """

# class ClassicSingleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(ClassicSingleton, cls).__new__(cls)
#         return cls.instance
#
#
# print('\n' + f'Classic singleton: ')
# s = ClassicSingleton()
# print('Object created', s)
# s1 = ClassicSingleton()
# print('Object created', s1)
#
# # Deferred instance
#
# '''Одним из вариантов использования шаблона Singleton является отложенная инициализация. Например, в случае импорта
#  модулей мы можем автоматически создать объект, даже если он не нужен. Отложенное создание экземпляра гарантирует,
#   что объект создается, только тогда, когда он действительно необходим.
# В следующем примере кода, когда мы используем s = Singleton(), вызывается метод __init__, но при этом новый объект
# не будет создан. Фактическое создание объекта произойдет, когда мы используем Singleton.getInstance().'''
#
#
class DeferredSingleton:
    __instance = None

    def __init__(self):
        if not DeferredSingleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())
        self.new_variable = 1

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = DeferredSingleton()
        return cls.__instance

    def example_func(self):
        print(f'print {self.new_variable}')

#
print('\n' + f'Deffered singleton: ')

a2 = DeferredSingleton.getInstance()
a3 = DeferredSingleton.getInstance()
a4 = DeferredSingleton.getInstance()
a5 = DeferredSingleton.getInstance()



print(a3 == a4)
print(DeferredSingleton.__dict__)
# # Monostate singleton
#
# '''концепция основана на том что бы все объекты имели одно и то же состояние'''
#
#
# class Borg:
#     __shared_state = {"1": "2"}
#
#     def __init__(self):
#         self.x = 1
#         self.__dict__ = self.__shared_state
#         pass
#
#
# b = Borg()
# b1 = Borg()
# b.x = 4
# print("Borg Object 'b': ", b)  ## b and b1 are distinct objects
# print("Borg Object 'b1': ", b1)
# print("Object State 'b':", b.__dict__)  ## b and b1 share same state
# print("Object State 'b1':", b1.__dict__)
#
# # 2 method Monstate singleton
#
#
# class BorgNew(object):
#     _shared_state = {}
#
#     def __new__(cls, *args, **kwargs):
#         obj = super(BorgNew, cls).__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls._shared_state
#         return obj
#
#
# # Realization Singleton and Metaclass
#
# class MetaSingleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class Logger(metaclass=MetaSingleton):
#     pass
#
# logger1 = Logger()
# logger2 = Logger()
# print(logger1 == logger2)

# decorator singleton

# def singleton(cls):
#     '''Класс Singleton (один экземпляр)'''
#
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         return wrapper_singleton.instance
#
#     wrapper_singleton.instance = None
#     return wrapper_singleton
#
#
# @singleton
# class TheOne:
#     pass
#
#
# print('старт')
# first_one = TheOne()
# second_one = TheOne()
# print(id(first_one))
# print(id(second_one))
# print('конец')


