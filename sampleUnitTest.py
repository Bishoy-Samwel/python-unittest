import pytest
from car import Car
from sample import car_speed


@pytest.fixture
def car():
    return Car()

def test_speed_property(car):
    car.speed = 50
    assert car.speed == 50

def test_car_speed_low(car):
    car.speed = 20
    assert car.car_speed() == "Level shall be Low"

def test_car_speed_normal(car):
    car.speed = 100
    assert car.car_speed() == "Level shall be Normal"

def test_car_speed_high(car):
    car.speed = 150
    assert car.car_speed() == "Level shall be High"

def test_car_speed_very_high(car):
    car.speed = 210
    assert car.car_speed() == "Level shall be V.High"

def test_car_speed_invalid_negative(car):
    car.speed = -10
    assert car.car_speed() == "Level shall be Invalid"

def test_car_speed_invalid_high(car):
    car.speed = 230
    assert car.car_speed() == "Level shall be Invalid"