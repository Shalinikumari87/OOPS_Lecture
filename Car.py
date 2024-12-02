# Write a python class Car with attributes like make,model and year? Then create an object class Car.
# In the car class define a variable of the colour of the car .

class Car:
    
    def __init__(self,make,model,year,colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    

Car1= Car("Suzuki","ZXL",2020,"Blue")
print(Car1.make,Car1.model,Car1.year,Car1.colour)
Car2= Car("Honda","Suv",2021,"black")
print(Car2.make,Car2.model,Car2.year,Car2.colour)

 

