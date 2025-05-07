# QUESTION:
# Frame a class Car with object variables car_id and car_name. Create two objects of Car class and assign name and id to them. Display both the car object details and also keep a track of how many car objects you have created by using class variable.



# CODE:
class Car:
    count = 0

    def __init__(self, car_id, car_name):
        self.car_id = car_id
        self.car_name = car_name
        Car.count += 1

    def __str__(self):
        return f"Car ID: {self.car_id}, Car Name: {self.car_name}"


car1 = Car(101, "Toyota")
car2 = Car(102, "Honda")

print(car1)
print(car2)

print(f"\nTotal Car objects created: {Car.count}")



# OUTPUT:
# Car ID: 101, Car Name: Toyota
# Car ID: 102, Car Name: Honda
#
# Total Car objects created: 2
