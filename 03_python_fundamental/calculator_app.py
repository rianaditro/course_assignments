
def add(first_number:float, second_number: float) -> float:
    return first_number + second_number
    

def subtract(first_number:float, second_number: float):
    return first_number - second_number

def multiply(first_number:float, second_number: float):
    return first_number * second_number

def divide(first_number:float, second_number: float):
    if second_number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return first_number / second_number

while True:

    while True:
        try:
            first_number = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid number")

    while True:    
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ["+", "-", "*", "/"]:
            break
        else:
            print("Invalid operator")

    while True:
        try:
            second_number = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid number")

    match operator :
        case "+" :
            result = add(first_number, second_number)
            print(f"Result: {result}")
        case "-" :
            print(f"Result: {subtract(first_number, second_number)}")
        case "*" :
            print(f"Result: {multiply(first_number, second_number)}")
        case "/" :
            try :
                print(f"Result: {divide(first_number, second_number)}")
            except ZeroDivisionError as e:
                print(str(e))
        case _ :
            print("Invalid operator. Please choose from +, -, *, /.")