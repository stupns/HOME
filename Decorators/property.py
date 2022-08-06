# Python program showing a use of property() function

class Geeks:
    def __init__(self):
        self._age = 0

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


# Python program showing the use of @property

class GeeksNew:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


# Example 3
class People:
    def __init__(self, __name):
        self.__name = ''

    def setname(self, name):
        print('setname() called')
        self.__name = name

    def getname(self):
        print('getname() called')
        return self.__name

    name = property(getname, setname)


# Example 4
class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return 3.1415 * self.r ** 2


# Example 5
class People2:
    def __init__(self):
        # __ private
        self.__name = ''
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError('negative age')
        self.__age = new_age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name.isalpha():
            raise ValueError('digits in name')
        self.__name = new_name


if __name__ == "__main__":
    mark = Geeks()
    mark.age = 10
    print(mark.age)
    print('\nExample 2:')

    mark = GeeksNew()
    mark.age = 19
    print(mark.age)
    print('\nExample 3:')

    obj = People('serhii')
    print(obj.__dict__)
    obj.setname('ivan')
    print(obj.__dict__)
    obj.__name = 'SeRHII'
    print(obj.__dict__)
    print('\nExample 4:')

    print(Circle(10).area)
    print('\nExample 5:')

    p = People2()
    p.age = 12
    p.name = 'Serhii'
    print(p.age, p.name)
