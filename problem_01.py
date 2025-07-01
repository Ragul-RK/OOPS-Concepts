"""
A start_engine() method that prints "Engine started".
A subclass Car that overrides start_engine() to print "Car engine started".

✍️ Bonus: Add an attribute fuel to Vehicle, and in Car, check if fuel > 0 before starting the engine.

"""


class Vehicle:
    def __init__(self, fuel=0):
        self.fuel=fuel
    def start_engine(self):
        print("Engine started") 
    
class Car(Vehicle):
    def start_engine(self,brand):
        if self.fuel > 0:
            print("Car engine started")
        else:
            print("Cannot start engine, no fuel!")   
        
        
        
my_car = Vehicle()
my_car.start_engine()  
        
        
        
        
