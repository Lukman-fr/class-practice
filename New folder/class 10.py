"""

# Check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Prompt the user to enter a year
try:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")

"""
from operator import truediv

"""
Write a Python program that checks whether a given year is a leap year. A year is a leap year if:
It is divisible by 4 but not by 100, or
It is divisible by 400.
Prompt the user to enter a year and print if it's a leap year or not.
"""
"""
def is_leap_year(year):
    if(year % 4 == 0 and year != 100) or (year % 400 == 0):
        return True
    return False


try:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year:")
    else:
        print(f"{year} is not leap year:")
except ValueError:
    print("invalid input. please enter a valid year ")

year = int(input())
"""

year = 2001
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("No Leap Year")








