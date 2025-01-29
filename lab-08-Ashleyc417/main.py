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


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_capacity):
        super().__init__(make, model, year,)
        self.engine_capacity = engine_capacity     
        self.__vin = None      # private
        self._color = None     # protected

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self.color

    def set_vin(self, vin):
        self.__vin = vin

    def get_vin(self):
        return self.__vin

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
            

#Driver code
# Create instances of Vehicle, Car, and Motorcycle
vehicle1 = Vehicle("Toyota", "Camry", 2022)
car1 = Car("Tesla", "Model 3", 2023, "Electric")
motorcycle1 = Motorcycle("Honda", "CBR500R", 2021, 471)

# Demonstrate class variables and inheritance
vehicle1.display_vehicle_count()

# Demonstrate private and protected variables
motorcycle1.__vin = "ABC123"  # Attempt to set private variable (won't work)
motorcycle1.set_color("Red")  # Set protected variable
print(f"Motorcycle color: {motorcycle1._color}")
print(f"Motorcycle VIN: {motorcycle1.get_vin()}")  # Access private variable

# Demonstrate generator functions
print("Counting up to 5:")
for num in count_up_to(5):
    print(num, end=" ")

print("\nFibonacci sequence up to 50:")
for num in fibonacci(50):
    print(num, end=" ")

# Demonstrate class variables
vehicle2 = Vehicle("Ford", "F-150", 2022)
vehicle3 = Vehicle("Honda", "Civic", 2022)
vehicle2.display_vehicle_count()
