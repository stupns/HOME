# Python program to demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):
        self._a = 2  # Protected member


# Creating a derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)
        self._a = 3  # Modify the protected variable:
        print("Calling modified protected member outside class: ", self._a)


obj1 = Derived()
obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)

print('\nStarted Class with private members:')


# Python program to demonstrate private members
# Creating a Base class


# 2. Example 2
class NewBase:
    def __init__(self):
        self.a = "Not private variable"
        self.__c = "Private variable"


# Creating a derived class
class Derived(NewBase):
    def __init__(self):
        Base.__init__(self)  # Calling constructor of Base class
        print("Calling private member of base class: ")
        print(self.__c)


obj1 = NewBase()
print(obj1.a)

# Uncommenting print(obj1.c) will raise an AttributeError.
# Uncommenting obj2 = Derived() will also raise an
# AttributeError as private member of base class is called inside derived class

# 3. Example 3
print('\nExample 3:')


class Person:
    def __init__(self, name, age, height):
        self.name = name  # public
        self._age = age  # protected
        self.__height = height  # private


p1 = Person("John", 20, 170)

print(f'public: {p1.name}')  # public: can be accessed
print(f'protected: {p1._age}')  # protected: can be accessed but not advised
# print(p1.__height)  # private: will give AttributeError

# 4. Example 4
print('\nExample 4:')


class Phone:
    username = "Kate"                # public variable
    __serial_number = "11.22.33"     # private variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print("Ring-ring!")

    def __turn_on(self):        # private method
        self.__how_many_times_turned_on += 1
        print("Times was turned on: ", self.__how_many_times_turned_on)


my_phone = Phone()

# my_phone.__turn_on() # - not working
my_phone._Phone__turn_on()
print(f"Correct serial number is {my_phone._Phone__serial_number}")
my_phone._Phone__serial_number = "33.22.11"
print(f"New serial number is {my_phone._Phone__serial_number}")
