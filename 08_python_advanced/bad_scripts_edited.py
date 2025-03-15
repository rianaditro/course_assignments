# This script demonstrates bad code formatting and style violations

# import os
# import sys


def welcome_user(name, age):  # Using snake_case for function name
    if age > 18:
        print("Welcome " + name)
    else:
        print("Sorry, " + name + " you are not allowed.")


def another_function():
    print("This function has consistent indentation.")


class MyClass:  # Using PascalCase for class name
    def __init__(self, x, y):
        self.x = x  # Added spaces around operator
        self.y = y  # Consistent spacing

    def show_values(self):  # Removed extra spaces in parameter list
        print("X:", self.x, "Y:", self.y)  # Fixed spacing


instance = MyClass(10, 20)  # Better variable naming
instance.show_values()
welcome_user("Alice", 17)
