class Car:
    # Class attribute
    total_cars = 0

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
