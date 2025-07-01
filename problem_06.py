"""Practice Question: Vehicle System Simulation
You're building a system to simulate different types of vehicles.

🔧 Requirements:
1.Create a base class Vehicle with:

    A private attribute __fuel (amount of fuel in liters).

    A method set_fuel(fuel) to set fuel.

    A method get_fuel() to retrieve fuel.

    A method start_engine() that prints "Engine started".

2.Create a subclass Car that inherits from Vehicle:

    Overrides start_engine() to:

        Check if fuel is greater than 0.

        If yes, print "Car engine started".

        If not, print "Cannot start. No fuel."



🧪 Sample Output:
    Fuel level: 10
    Car engine started

[or]
    Fuel level: 0
    Cannot start. No fuel.

"""


