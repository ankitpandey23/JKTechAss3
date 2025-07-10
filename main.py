import random
from add import add
from multiply import multiply
from division import divide

def get_valid_input():
    while True:
        try:
            user_input = input("Enter at least two non-zero integers separated by spaces: ")
            numbers = list(map(int, user_input.strip().split()))
            non_zero_numbers = [num for num in numbers if num != 0]
            if len(non_zero_numbers) >= 2:
                return non_zero_numbers
            else:
                print("Please enter at least two non-zero integers.")
        except ValueError:
            print("Invalid input. Please enter integers only.")

def ensure_even_sum(numbers):
    attempts = 0
    while add(numbers) % 2 != 0 and attempts < 3:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Sum is odd. Adding random number {rand_num} to the list.")
        numbers.append(rand_num)
        attempts += 1
    return numbers

def ensure_even_product(numbers):
    attempts = 0
    while multiply(numbers) % 2 != 0 and attempts < 3:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Product is odd. Adding random number {rand_num} to the list.")
        numbers.append(rand_num)
        attempts += 1
    return numbers

def ensure_non_zero_last(numbers):
    if numbers[-1] == 0:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Last number is zero. Replacing with random number {rand_num}.")
        numbers[-1] = rand_num
    return numbers

def main():
    numbers = get_valid_input()
    numbers = ensure_even_sum(numbers)
    numbers = ensure_even_product(numbers)
    numbers = ensure_non_zero_last(numbers)

    try:
        result = divide(numbers)
        print(f"Result of dividing first number by last number (rounded): {result}")
    except ValueError as e:
        print(f"Error during division: {e}")

if __name__ == "__main__":
    main()
