try:
    count = int(input("How many terms? "))
    a, b = 0, 1
    for _ in range(max(0, count)):
        print(a, end=" ")
        a, b = b, a + b
    print()
except ValueError: print("Please enter a whole number.")
