# Author: Austin Calloni
# Date: 6/17/2024
# Purpose: To get use input, validate it, and create an Automobile class object based off the user's input.
# File Name: M03 Lab.py

# Parent Vehicle Class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Child class that inherits Vehicle class.
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # pass the vehicle type to the parent class initializer
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Ensure user inputs a valid vehicle type.
def input_to_vehicle_type():
    while True:
        val = input("Please enter a vehicle type(car, truck, plane, boat, broomstick): ").lower()
        if val not in ["car", "truck", "plane", "boat", "broomstick"]:
            print("Invalid vehicle type. Accepted types are: 'car', 'truck', 'plane', 'boat', 'broomstick'")
            continue
        return val


# Ensure user inputs a valid door option
def validate_door_options():
    while True:
        try:
            val = int(input("Please enter a valid door option(2 or 4 doors): "))
            if val not in [2, 4]:
                print("Invalid door option. Accepted door options are: '2' or '4'")
                continue
        except ValueError:
            print("The value entered was not a number. Please enter '2' or '4'.")
            continue

        return val


# Ensure user inputs a valid roof option
def validate_roof_options():
    while True:
        val = input("Please enter a valid roof type(solid or sun roof): ").lower()
        if val not in ["solid", "sun roof"]:
            print("Invalid roof option. Accepted options are 'solid' or 'sun roof'")
            continue
        return val


# Ensure user inputs a valid year.
def validate_year_input():
    while True:
        try:
            val = int(input("Please enter a valid year: "))
            return val
        except ValueError:
            print("The year entered was not a valid number. Please enter a valid number.")
            continue


# Main entry point
def main():
    # Get user values to construct our automobile
    vehicle = Vehicle(input_to_vehicle_type())
    year = validate_year_input()
    make = input("Please enter a vehicle make: ")
    model = input("Please enter a vehicle model: ")
    door = int(validate_door_options())
    roof = validate_roof_options()

    # Construct or automobile
    automobile = Automobile(vehicle.vehicle_type, year, make, model, door, roof)

    # Print attributes out to user
    print(f"""Vehicle Type: {automobile.vehicle_type}
Year: {automobile.year}
Make: {automobile.make}
Model: {automobile.model}
Doors: {automobile.doors}
Roof: {automobile.roof}
    """)


# Guard clause for our main program.
if __name__ == "__main__":
    main()
