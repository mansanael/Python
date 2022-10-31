class Car:
    brand = ""
    model = ""
    year = ""
    speed = ""
    mileage = ""

    def __int__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year


class ElectricCar(Car):
    battery_capacity = 0

    def __int__(self, brand: str, model: str, year: int, battery_capacity: int):
        super().__int__(brand, model, year)


class EngineCar(Car):
    engine_capacity = 0


car = Car()
car.year = 2022

electric_car = ElectricCar()
electric_car.battery_capacity = 20
electric_car.brand = 'Tesla'

c_engine_car = EngineCar()
c_engine_car.engine_capacity = 15
c_engine_car.brand = 'Toyota'
