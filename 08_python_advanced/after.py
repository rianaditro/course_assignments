import math


def calculate_area(radius):
    area = math.pi * radius**2
    return area


def calculate_circumference(radius):
    return 2 * math.pi * radius


def print_results(r):
    print("Radius: ", r)
    print("Area: ", calculate_area(r))
    print("Circumference:", calculate_circumference(r))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return calculate_area(self.radius)

    def circumference(self):
        return calculate_circumference(self.radius)

    def summary(self):
        print("Circle summary:")
        print_results(self.radius)


if __name__ == "__main__":
    r = input("Enter radius: ")
    c = Circle(float(r))
    c.summary()
