import math

print("Welcome to the velocity calculator. Please enter the following: ")

mass = float(input("Mass (in kg): "))
gravity = float(input("in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density_fluid = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 ofr cylinder): "))

c = ( 1 / 2) * density_fluid * cross_area * drag_constant # I didn't find the name of 'c' to use a better variable name for it.

print(f"\nThe inner value of c is: {c:.3f}\n")

velocity = math.sqrt((mass * gravity) / c) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass) * time))

print(f"The velocity after {time} seconds is: {velocity:.3f} m/s ")