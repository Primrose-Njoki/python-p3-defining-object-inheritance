class Vehicle:
    def __init__(self,wheel_size,wheel_number):
        self.wheel_size=wheel_size
        self.wheel_number=wheel_number
# instance methods
    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"

my_car = Vehicle(18, 4)
print(my_car.wheel_number)

print(my_car.go())  
print (my_car.fill_up_tank())