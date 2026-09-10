try:
    number = int(input("Enter an integer: "))
    prime = number > 1 and all(number % d for d in range(2, int(number ** 0.5) + 1))
    print("Prime" if prime else "Not prime")
except ValueError: print("Please enter a whole number.")
