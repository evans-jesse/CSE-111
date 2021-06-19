"""
v =   π w^2 a(w a + 2,540 d)
          10,000,000

v is the volume in milliliters,
π is the constant PI, the ratio of the circumference divided by the diameter of a circle (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14

The approximate volume is 24090.1 cubic cm.
"""
import math

print("---------------\n\n") # Make it look pretty

# Context
print("The size of a car tire in the United States is represented with three")
print("numbers like this: 205/60R15. The first number is the width of the tire")
print("in millimeters. The second number is the aspect ratio. The third number")
print("is the diameter in inches of the wheel that the tire fits.")

# loop
x = "y"
while x == "y":
    print("")
    # Gather the inputs
    w = int(input("Enter the width of the tire in mm (ex 205): "))
    a = int(input("Enter the aspect ratio of the tire (ex 60): "))
    d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    # do the equation
    v = (math.pi * w**2 * a * (w * a + 2540 * d))/10000000

    # print the result
    print(f"\nThe approximate volume of this tire is {v:.1f} cubic cm.\n")
    
    x = input("Would you like to test another tire? (y/n): ")

print("\nThanks for testing!")

print("\n\n---------------") # Make it look pretty