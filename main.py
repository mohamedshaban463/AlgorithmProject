from NonRecursive import max_product_of_three as max_product_of_three_non_recursive
from Recursive import max_product_of_three as max_product_of_three_recursive

print("Enter comma-separated ints:")
numbers_input = input()

try:
    numbers = [int(x.strip()) for x in numbers_input.split(',')]
    while True:
        print("recursive:1\nnon-recursive:2")
        choice = input().strip()

        if choice == '1':
            print(max_product_of_three_recursive(numbers))
            break
        elif choice == '2':
            print(max_product_of_three_non_recursive(numbers))
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")
except ValueError:
    print("Invalid input. Please ensure you enter comma-separated integers.")