# create class dog
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'Dog {self.name} sitting now.')

    def roll_over(self):
        print(f'{self.name} rolled over!')


my_dog = Dog('Harry', 3)
print(f'My dog`s name is {my_dog.name} and he`s {my_dog.age} years old.')
my_dog.sit()


# create class Cars
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f'You cant roll back an odometer')

    def increment_odometr(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        pass


my_old_car = Car('subary', 'outback', 2004)
print(f'My old car: {my_old_car.get_descriptive_name()}')
my_old_car.update_odometer(20000)
my_old_car.read_odometer()
my_old_car.increment_odometr(5000)
my_old_car.read_odometer()

print('\n')
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.increment_odometr(10000)
# my_new_car.odometer_reading = 32   first method change value attribute classes
my_new_car.read_odometer()
print('\n')


# Успадкування


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size} - kWh battery.')

    def get_range(self):
        global range
        if self.battery_size >= 75:
            range = 260
        elif self.battery_size >= 100:
            range = 315
        print(f'This car can go about {range} miles on a full charge')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f'This car doesn`t need a gas tank')


myTeslaCar = ElectricCar('tesla', 'model S', '2020')
print(myTeslaCar.get_descriptive_name())
myTeslaCar.battery.describe_battery()
myTeslaCar.fill_gas_tank()
myTeslaCar.battery.get_range()
