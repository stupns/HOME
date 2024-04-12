class Bug:
    def __init__(self):
        self.wings = 4


class Human:
    def __init__(self):
        self.legs = 2
        self.arms = 2


bob = Human()
tom = Bug()

print(tom.wings)
print(bob.arms)


class Plane:
    def __init__(self):
        self.wings = 2

        # fly
        self.drive()
        self.flaps()
        self.wheels()

    @staticmethod
    def drive():
        print('Accelerating')

    @staticmethod
    def flaps():
        print('Changing flaps')

    @staticmethod
    def wheels():
        print('Closing wheels')


ba = Plane()
