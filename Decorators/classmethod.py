class Fruit:
    name = 'Fruits'

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)


apple = Fruit()
berry = Fruit()

Fruit.printName()
apple.printName()
berry.printName()


# Alternative writing
class AltFruit:
    name = 'Fruits'

    def printName(cls):
        print('The name is:', cls.name)


AltFruit.printAge = classmethod(AltFruit.printName)  # use classmethod here
AltFruit.printAge()
