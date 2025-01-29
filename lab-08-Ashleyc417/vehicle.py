class Vehicle():
    vehicle_count = 0
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1

    def display_vehicle_count(Vehicle):
       return Vehicle.vehicle_count


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type     


class Motorcycle(Car):
    def __init__(self, make, model, year, fuel_type, engine_capacity):
        super().__init__(make, model, year, fuel_type)
        self.engine_capacity = engine_capacity     
        self.__vin = None      # private
        self._color = None     # protected

    def set_color(self, color):
        self.color = color

    def set_vin(self, vin):
        self.__vin = vin

def count_up_to(n):
    current = 1
    while current <= n:
        yield current
        current += 1

def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
            

