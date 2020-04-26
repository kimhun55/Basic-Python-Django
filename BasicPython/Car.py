class Car:
    # Properties
    color = ""
    brand = ""
    number_Of_wheel = 4
    number_Of_seats = 4
    maxspeed = 0

    # constructor
    def __init__(self, color, brand, number_Of_seats=4, number_Of_wheel=4, maxspeed=100):
        self.color = color
        self.brand = brand
        self.number_Of_wheel = number_Of_wheel
        self.number_Of_seats = number_Of_seats
        self.maxspeed = maxspeed

    # method
    def setcolor(self, x):
        self.color = x

    def setbrand(self, x):
        self.brand = x

    def setspeed(self, x):
        self.maxspeed = x

    def printdata(self):
        print("color :", self.color)
        print("brand :", self.brand)
        print("maxspeed :", self.maxspeed)

    # Decontructor
    def __del__(self):
        print()
