try:
    numbers = [float(input(f"Number {i}: ")) for i in range(1, 4)]
    print("Largest number:", max(numbers))
except ValueError: print("Please enter valid numbers.")
