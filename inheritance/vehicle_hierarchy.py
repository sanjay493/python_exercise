class Vehicle:
    fuel_price = 100
    def __init__(self, vehicle_no, fuel_type):
        self.vehicle_no = vehicle_no
        self.fuel_type = fuel_type
    
    def fuel_cost(self,distance):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    mileage = 15
    def fuel_cost(self, distance):
        cost = (distance / self.mileage) * self.fuel_price
        return cost
    
class Truck(Vehicle):
    mileage = 5
    def fuel_cost(self, distance):
        cost = (distance / self.mileage) * self.fuel_price
        return cost


# Example usage:
car = Car("KA-01-1234", "Petrol")
truck = Truck("KA-02-5678", "Diesel")

distance = 150  # distance in kilometers
print(f"Fuel cost for car over {distance} km: {car.fuel_cost(distance)}")
print(f"Fuel cost for truck over {distance} km: {truck.fuel_cost(distance)}")

