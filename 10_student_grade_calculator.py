try:
    mark = float(input("Enter mark (0-100): "))
    if not 0 <= mark <= 100: raise ValueError("Mark must be 0 to 100")
    grade = "A" if mark >= 90 else "B" if mark >= 75 else "C" if mark >= 60 else "D" if mark >= 40 else "F"
    print("Grade:", grade)
except ValueError as error: print("Invalid mark:", error)
