try:
    number = int(input("Non-negative integer: "))
    if number < 0: print("Factorial is not defined for negatives.")
    else:
        answer = 1
        for value in range(2, number + 1): answer *= value
        print("Factorial:", answer)
except ValueError: print("Please enter a whole number.")
