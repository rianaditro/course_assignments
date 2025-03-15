# This script demonstrates bad code formatting and style violations

import os, sys  # Multiple imports on one line (violates PEP 8)


def badFunction(name, age):  # Incorrect spacing, bad function name casing
    if age > 18:
        print(
            "Welcome " + name
        )  # No indentation, missing spaces, bad string concatenation
    else:
        print("Sorry, " + name + " you are not allowed.")  # Inconsistent indentation


def another_function():
    print("This function has inconsistent indentation.")  # Bad indentation


class Myclass:  # Class name should be MyClass (PascalCase)
    def __init__(self, x, y):
        self.x = x  # No space around operator
        self.y = y  # Inconsistent spacing

    def show_values(self):  # Extra spaces in parameter list
        print("X:", self.x, "Y:", self.y)  # Inconsistent spacing


myobj = Myclass(10, 20)  # Poor variable naming
myobj.show_values()

badFunction("Alice", 17)  # Function name should be snake_case
