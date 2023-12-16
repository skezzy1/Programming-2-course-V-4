class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed
    
my_car = Car("Toyota", "Camry", 2022)
for i in range(5):
    my_car.accelerate()
    current_speed = my_car.get_speed()
    print(f"Поточна швидкість: {current_speed} км/год")
for i in range(5):
    my_car.brake()
    current_speed = my_car.get_speed()
    print(f"Поточна швидкість: {current_speed} км/год")