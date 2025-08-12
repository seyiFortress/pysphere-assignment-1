import my_physics_library
import math

current = input("Enter the current (in A): ")
resistance = input("Enter the resistance (in ohms): ")

try:
    # Float values
    float_current = float(current)
    float_resistance = float(resistance)

    # Use voltage function from my_physics_library
    volt = my_physics_library.voltage(float_current, float_resistance)

    # Round up voltage to 2 decimal places
    voltage = math.ceil(volt * 100) / 100

    print(f"The voltage is: {voltage} volts")
except ValueError:
    print("Invalid value entered!!! ...Please enter a number")
