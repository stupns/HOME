import pytest
"""
OOP Exercise 1: Create a Class with instance attributes.
Write a Python program to create a Vehicle class with max_speed, mileage, name and capacity instance attributes.
"""
"""
OOP Exercise 2: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
"""
"""
OOP Exercise 3: Class Inheritance, create func seating_capacity with arg: capacity. Func return string:
The seating capacity of a {self.name} is {capacity} passengers. Create duplicate func in Bus classes and give default
value of 50 
"""
"""
OOP Exercise 4: Define a property that must have the same value for every class instance (object).
Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.
Create class Car.
Expected Output: 
Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
"""
"""
OOP Exercise 5:
Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating
capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
You need to override the fare() method of a Vehicle class in Bus class.
"""
"""
OOP Exercise 6: Check type of an object
Write a program to determine which class a given Bus object belongs to.
"""
"""
OOP Exercise 7: Determine if school_bus is also an instance of the Vehicle class
"""
"""
OOP Exercise 8: Create variable age_car, and use decorator static_method. If age car is more > 5 year return string:
'It car is old' else 'It new car'. Print result for school_bus.
"""

"""
OOP Exercise 9: Create variable car_price, and use decorator classmethod. Add name car ['BMW','AUDI','MERSEDES'] return:
price * 20% for diff * 10%. Result need return in string format : 'Name car price'.
"""
"""
OOP Exercise 10: Create class Driver with init attributes first_name, last_name. Create method that return full_name.
Use decorator property and check how work program with changed variable.
"""
"""
OOP Exercise 11: Add decorator setter for method fullname to be able change variable instance 
"""


class Vehicle:
    # Class attribute
    color = 'White'

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f'The seating capacity of a {self.name} is {capacity} passengers.'

    def fare(self):
        return self.capacity * 100

    @staticmethod
    def age_car(age):
        if age > 5:
            return str('It car is old')
        else:
            return str('It new car')


    @classmethod
    def car_price(cls, name, price):
        expensive_brand = ['BMW', 'AUDI', 'MERSEDES']
        if name.upper() in expensive_brand:
            price += price * 20/100
        else:
            price += price * 10/100
        return f'{name} {price}'


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount


class Car(Vehicle):
    pass


class Driver:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split()
        self.first_name = first_name
        self.last_name = last_name


pytest.main()
