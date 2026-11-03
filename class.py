class car:  # Class attribute (shared by all cars)
    wheels = 4

# Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

#method(action)
    def display_info(self):
        print(f"{self.brand},{self.model} has {self.wheels} wheels")
my_car=car("toyato","carolla")
my_car.display_info()
