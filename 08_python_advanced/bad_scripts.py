# This script demonstrates bad code formatting and style violations


def good_function(name, age):  # Incorrect spacing, bad function name casing
    if age > 18:
        print(
            "Welcome " + name
        )  # No indentation, missing spaces, bad string concatenation
    else:
        print("Sorry, " + name + " you are not allowed.")


def another_function():
    print("This function has inconsistent indentation.")  # Bad indentation


class MyClass:  # Class name should beMyClass (PascalCase)
    def __init__(self, x, y):
        self.x = x  # No space around operator
        self.y = y  # Inconsistent spacing

    def show_values(self):  # Extra spaces in parameter list
        print("X:", self.x, "Y:", self.y)  # Inconsistent spacing


elite = MyClass(10, 20)  # Poor variable naming
elite.show_values()

good_function("Alice", 17)  # Function name should be snake_case
