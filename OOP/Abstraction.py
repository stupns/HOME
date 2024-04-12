from abc import ABC, abstractmethod

# 1. EXAMPLES
print('\n1. Examples')


class AbsClass(ABC):
    def print_val(self, x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


class TestClass(AbsClass):
    def task(self):
        print("We are inside test_class task")


class ExampleClass(AbsClass):
    def task(self):
        print("We are inside example_class task")


# object of test_class created
test_obj = TestClass()
test_obj.task()
test_obj.print_val(100)

# object of example_class created
example_obj = ExampleClass()
example_obj.task()
example_obj.print_val(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj, AbsClass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, AbsClass))

# 2. EXAMPLES
print('\n2. Examples')


class Bank(ABC):
    @staticmethod
    def branch(RD):
        print("Fees submitted : ", RD)

    @staticmethod
    @abstractmethod
    def bank(RD):
        pass


class Private(Bank):

    @staticmethod
    def bank(RD):
        print("Total RD Value here: ", RD)


class XXX(Bank):

    @staticmethod
    def bank(RD):
        print("Total RD Value here:", RD)


Private.bank(500)
XXX.bank(200)
XXX.branch(200)

# 3. EXAMPLES
print('\n3. Examples')


class Geometric(ABC):
    length = 1
    width = 1
    height = 1

    def volume(self):  # abstract method
        return self.length * self.width * self.height


class Rect(Geometric):
    length = 4
    width = 6
    height = 6

    def volume(self):
        return self.length * self.width * self.height


class Sphere(Geometric):
    radius = 8

    def volume(self):
        return 1.3 * 3.14 * self.radius * self.radius * self.radius


class Cube(Geometric):
    Edge = 5

    def volume(self):
        return self.Edge * self.Edge * self.Edge


class Triangle3D:
    length = 5
    width = 4

    def volume(self):
        return 0.5 * self.length * self.width


rr = Rect()
ss = Sphere()
cc = Cube()
tt = Triangle3D()

print("Volume of a rectangle:", rr.volume())
print("Volume of a circle:", ss.volume())
print("Volume of a square:", cc.volume())
print("Volume of a triangle:", tt.volume())
