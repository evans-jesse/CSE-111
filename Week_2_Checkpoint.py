"""
A manufacturing company needs a program that will help its employees pack
manufactured items into boxes for shipping. Write a Python program named
boxes.py that asks the user for two integers:  1) the number of manufactured
items and 2) the number of items that the user will pack per box. Your
program must compute and print the number of boxes necessary to hold the
items. This must be a whole number. Note that the last box may be packed
with fewer items than the other boxes.
"""
print("---------------\n\n")
import math
# Gather info
num_of_product = int(input("How many items have you made? "))
product_in_box = int(input("How many items will go in each box? "))
# Equation

boxes = math.ceil(num_of_product/product_in_box)

print(f"\nYou will need {boxes} boxes.")
print("\n\n---------------")