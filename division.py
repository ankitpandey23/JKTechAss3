def divide(numbers):
    if numbers[-1] == 0:
        raise ValueError("Cannot divide by zero.")
    return round(numbers[0] / numbers[-1])
