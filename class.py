"""
1. Class attributes: `total_cars` is a class attribute that keeps track of the total number of cars created.

2. Constructor method (`__init__`): Initializes the instance attributes (`brand`, `model`, `color`, `is_running`)
when a new `Car` object is created.

3. Instance methods: `start_engine()` and `stop_engine()` demonstrate behavior specific to each car instance.
They change the `is_running` attribute and print corresponding messages.

4. Instance method with conditional behavior: `honk()` checks if the engine is running before honking.
It prints different messages based on the engine's status.

5. Class method: `get_total_cars()` is a class method that returns the total number of cars created by accessing the
class attribute `total_cars`.

6. Static method: `get_vehicle_type()` is a static method that returns a generic vehicle type, which is the same for
all cars.

You can create instances of the `Car` class, call methods, and access attributes as follows:

"""


class Car:
    # Class attribute
    total_cars = 0

    # Constructor method (`__init__`): Initializes the instance attributes
    def __init__(self, brand, model, color):
        # Instance attributes
        self.brand = brand
        self.model = model
        self.color = color
        self.is_running = False
        Car.total_cars += 1

    def start_engine(self):
        self.is_running = True
        print(f"The {self.brand} {self.model}'s engine is now running.")

    def stop_engine(self):
        self.is_running = False
        print(f"The {self.brand} {self.model}'s engine has been stopped.")

    def honk(self):
        if self.is_running:
            print(f"The {self.brand} {self.model} honks loudly!")
        else:
            print("Please start the engine first.")

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    @staticmethod
    def get_vehicle_type():
        return "Car"


if __name__ == "__main__":
    """
    Instances of the `Car` class, call methods, and access attributes
    """
    # Create two car instances
    car1 = Car("Toyota", "Camry", "Blue")
    car2 = Car("Honda", "Accord", "Red")
    # car3 = Car("Honda", "Accord", "Red")

    # Call instance methods
    car1.start_engine()
    car2.start_engine()
    car1.honk()
    car2.honk()
    car1.stop_engine()
    car2.stop_engine()

    # Call class method
    print("Total cars:", Car.get_total_cars())

    # Call static method
    print("Vehicle type:", Car.get_vehicle_type())
