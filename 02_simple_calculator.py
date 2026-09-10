try:
    first = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ")
    second = float(input("Second number: "))
    if operator == "+": result = first + second
    elif operator == "-": result = first - second
    elif operator == "*": result = first * second
    elif operator == "/": result = first / second
    else: raise ValueError("Use +, -, *, or /")
    print("Result:", result)
except ValueError as error: print("Invalid input:", error)
except ZeroDivisionError: print("Cannot divide by zero.")
