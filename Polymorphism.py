class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Creating instances of Car and Plane
my_car = Car()
my_plane = Plane()

# Demonstrating the move() method for each vehicle
print(my_car.move())   # Output: Driving 🚗
print(my_plane.move()) # Output: Flying ✈️
