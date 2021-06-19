print("---------------\n\n")
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.

Please enter your age: 23
When you exercise to strengthen your heart, you should
keep your heart rate between 128 and 167 beats per minute.
"""

# Enter age
# 220 - age = max
# determine 65% of max and 85%
# print statement

# Get the age of person
age = int(input("Please enter your age: "))
max_heart = 220 - age

# Calculate percentages
sixty = max_heart * 0.65
eighty = max_heart * 0.85

# print the results
print("\nWhen you exercise to strengthen your heart, you should keep")
print(f"your heart rate between {round(sixty)} and {round(eighty)} beats per minute.")

print("\n\n---------------")