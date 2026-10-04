for i in range(1, 6):
    number = float(input(f"Enter number {i} (between 1 and 10): "))
    if 1 <= number <= 10:
        square = number ** 2
        print("Square:", square)
    else:
        print("Error: Number is out of range [1, 10]")