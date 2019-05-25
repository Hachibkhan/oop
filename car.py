class Car:

    def __init__(self, n, c):

        Car.name = n

        Car.color = c

    
    def start(self):

        print("name:", self.name)

        print("color:", self.color)

        print("Starting the engine.")


# creating a Car object

my_car1 = Car('Allion', 'White')

my_car1.start()

my_car2 = Car('Carolla', 'Red')

my_car2.start()

my_car3 = Car('Premio', 'Blue')

my_car3.start()

