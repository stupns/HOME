import pytest

from TASKS.CLASSES.СLASSES import Vehicle, Bus, Car, Driver


@pytest.fixture
def vehicle():
    return Vehicle('Chevrolet', 220, 24, 2.0)


@pytest.fixture
def bus():
    return Bus('School Volvo', 180, 12, 2.5)


@pytest.fixture
def car():
    return Car('bmw', 240, 18, 2.0)


@pytest.fixture
def driver():
    return Driver('Ivan', 'Stupnytskyi')


def test_exercise1(vehicle):
    assert isinstance(vehicle, Vehicle)


def test_exercise2(bus):
    assert issubclass(Bus, Vehicle)
    assert isinstance(bus, Vehicle)


def test_exercise3(bus):
    bus_seating_capacity = bus.seating_capacity()
    assert bus_seating_capacity == 'The seating capacity of a School Volvo is 50 passengers.'


def test_exercise4(car):
    assert car.color == 'White'
    assert issubclass(Car, Vehicle)


def test_exercise5(bus):
    assert bus.fare() == 275.0


def test_exercise8(bus):
    assert bus.age_car(8) == 'It car is old'
    assert bus.age_car(4) == 'It new car'


def test_exercise9():
    assert Vehicle.car_price('bmw', 20000) == 'bmw 24000.0'
    assert Vehicle.car_price('chevrolet', 20000) == 'chevrolet 22000.0'


def test_exercise10(driver):
    assert driver.full_name == 'Ivan Stupnytskyi'
    driver.first_name = 'Serhii'
    assert driver.full_name == 'Serhii Stupnytskyi'


def test_exercise11(driver):
    driver.full_name = 'Igor Borovets'
    assert driver.full_name == 'Igor Borovets'
